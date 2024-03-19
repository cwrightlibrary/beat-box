from midi_mapping import *
from note_lengths import *
from os.path import dirname, join, realpath
from scamp import *
from time import sleep

TEMPO = 90
SESSION = Session(tempo=TEMPO)
DRUMMER_SF = join(dirname(realpath(__file__)), "drum-kit.sf2")
PIANO_SF = join(dirname(realpath(__file__)), "steinway.sf2")

DRUMMER = SESSION.new_part("Brush", soundfont=DRUMMER_SF)
PIANO = SESSION.new_part("Piano", soundfont=PIANO_SF)

BEATS = [1, 2, 3, 4]
C_BEAT = 0

BRUSH_SWIRLS = electric_snare
HI_HAT_CLOSED = closed_hi_hat
HI_HAT_OPEN = open_hi_hat
HI_HAT_PEDAL = pedal_hi_hat
KICK = bass_drum_1
RIDE = ride_cymbal_1
SNARE = tap_snare
HI_HAT_PEDAL = pedal_hi_hat
NO_INSTRUMENT = None


def play_bg(drummer):
    while True:
        drummer.play_note(BRUSH_SWIRLS, 1, 4)


def playnote(drum_note, length, volume, drummer):
    if len(drum_note) == 1 or (len(drum_note) == 2 and None in drum_note):
        if len(drum_note) == 1 and drum_note[0] == None:
            drummer.play_note(electric_snare, 0, length, silent=True)
        else:
            drummer.play_note(drum_note[0], volume, length)
    elif len(drum_note) > 1:
        if None in drum_note:
            temp_notes = []
            for n in drum_note:
                if n != None:
                    temp_notes.append(n)
            if len(temp_notes) == 0:
                drummer.play_note(electric_snare, 0, length, silent=True)
            elif len(temp_notes) > 1:
                drummer.play_chord(temp_notes, volume, length)
            else:
                drummer.play_note(temp_notes[0], volume, length)
        else:
            drummer.play_chord(drum_note, volume, length)


def jazz_pattern(note, drummer):
    if note == 1:
        playnote([KICK, RIDE], quarter_note, 1, drummer)
    elif note == 2:
        playnote([SNARE, RIDE], triplet_quarter_note * 2, 1, drummer)
        playnote([KICK, RIDE], triplet_quarter_note, 1, drummer)
    elif note == 3:
        playnote([RIDE], triplet_quarter_note, 1, drummer)
        playnote([SNARE], triplet_quarter_note * 2, 0.3, drummer)
    elif note == 4:
        playnote([SNARE, RIDE], triplet_quarter_note * 2, 1, drummer)
        playnote([SNARE], triplet_quarter_note, 0.4, drummer)


def chords(note, piano):
    if note == 1:
        piano.play_chord([60, 64, 67, 71], 0.8, quarter_note)
    elif note == 2:
        piano.play_chord([64, 67, 71, 74], 0.8, quarter_note)
    elif note == 3:
        piano.play_chord([60, 64, 67, 71], 0.8, quarter_note)
    elif note == 4:
        piano.play_chord([64, 67, 71, 74], 0.8, quarter_note)


fork(play_bg, args=(DRUMMER,))
sleep(1)
while C_BEAT < len(BEATS):
    print(str(BEATS[C_BEAT]))
    fork(chords, args=(BEATS[C_BEAT], PIANO,))
    jazz_pattern(BEATS[C_BEAT], DRUMMER)
    C_BEAT += 1
    if C_BEAT == len(BEATS):
        C_BEAT = 0