from midi_mapping import *
from note_lengths import *
from os.path import dirname, join, realpath
from scamp import *
from time import sleep

TEMPO = 113
SESSION = Session(tempo=TEMPO)
DRUMMER_SF = join(dirname(realpath(__file__)), "drum-kit.sf2")

DRUMMER = SESSION.new_part("Brush", soundfont=DRUMMER_SF)

TIME_SIGNATURE = [3, 4]

BEATS = [x for x in range(1, TIME_SIGNATURE[0] + 1)]
C_BEAT = 0

BARS = [x for x in range(1, TIME_SIGNATURE[1] + 1)]
C_BAR = 0

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


def jazz_pattern(beat, bar, drummer):
    if beat == 1:
        playnote([KICK, RIDE], quarter_note, 1, drummer)
    elif beat == 2:
        playnote([SNARE, RIDE], triplet_quarter_note * 2, 1, drummer)
        playnote([KICK, RIDE], triplet_quarter_note, 1, drummer)
    elif beat == 3:
        if bar == 2 or bar == 4:
            playnote([RIDE], triplet_quarter_note, 1, drummer)
            playnote([SNARE], triplet_quarter_note * 2, 0.35, drummer)
        else:
            playnote([RIDE], quarter_note, 1, drummer)
    elif beat == 4:
        if bar == 4:
            playnote([SNARE, RIDE], triplet_quarter_note * 2, 1, drummer)
            playnote([SNARE], triplet_quarter_note, 0.4, drummer)
        else:
            playnote([SNARE, RIDE], quarter_note, 1, drummer)


fork(play_bg, args=(DRUMMER,))
sleep(1)
while C_BEAT < len(BEATS):
    jazz_pattern(BEATS[C_BEAT], BARS[C_BAR], DRUMMER)
    C_BEAT += 1
    if C_BEAT == len(BEATS):
        C_BAR += 1
        C_BEAT = 0
    if C_BAR == len(BARS):
        C_BAR = 0
