from os.path import dirname, join, realpath
from scamp import *
from random import randint
from time import sleep

# Note lengths
whole_note = 4
half_note = 2
quarter_note = 1
eighth_note = 0.5
sixteenth_note = 0.25
triplet_quarter_note = 0.3333333333333333
triplet_eighth_note = 0.1666666666666667
triplet_sixteenth_note = 0.0833333333333333

input_names = ["w", "h", "q", "e", "s", "tq", "te", "ts"]
output_names = [whole_note, half_note, quarter_note, eighth_note, sixteenth_note, triplet_quarter_note, triplet_eighth_note, triplet_sixteenth_note]

# Instrument names
tap_snare = 27
acoustic_drum = 35
bass_drum_1 = 36
side_stick = 37
acoustic_snare = 38
hand_clap = 39
electric_snare = 40
low_floor_tom = 41
closed_hi_hat = 42
high_floor_tom = 43
pedal_hi_hat = 44
low_tom = 45
open_hi_hat = 46
low_mid_tom = 47
hi_mid_tom = 48
crash_cymbal_1 = 49
high_tom = 50
ride_cymbal_1 = 51
chinese_cymbal = 52
ride_bell = 53
tambourine = 54
splash_cymbal = 55
cowbell = 56
crash_cymbal_2 = 57
vibraslap = 58
ride_cymbal_2 = 59
hi_bongo = 60
low_bongo = 61
mute_hi_conga = 62
open_hi_conga = 63
low_conga = 64
high_timbale = 65
low_timbale = 66
high_agogo = 67
low_agogo = 68
cabasa = 69
maracas = 70
short_whistle = 71
long_whistle = 72
short_guiro = 73
long_guiro = 74
claves = 75
hi_wood_block = 76
low_wood_block = 77
mute_cuica = 78
open_cuica = 79
mute_triangle = 80
open_triangle = 81

rides = [ride_cymbal_1, ride_cymbal_2]
crashes = [crash_cymbal_1, crash_cymbal_2]

# Soundfonts
drum_soundfont = join(dirname(realpath(__file__)), "drum-kit.sf2")

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

# test_pattern = [
#     "r/h crash,ride,bass/q r/tq r/tq crash,ride,bass/tq",
#     "r/h crash,ride,bass/q r/tq r/tq crash,ride,bass/tq",
#     "r/h crash,ride,bass/q r/tq r/tq crash,ride,bass/tq",
#     "r/h crash,ride,bass/q r/tq r/tq crash,ride,bass/tq"
# ]
def parse_pattern(pattern: list):
    for m in pattern:
        notes = m.split(" ")
        for n in notes:
            to_play = []
            if "," in n.split("/")[0]:
                n_name = n.split("/")[0].split(",")
            else:
                n_name = [n.split("/")[0]]
            n_length_raw = n.split("/")[1]
            for l in range(len(input_names)):
                if input_names[l] == n_length_raw:
                    n_length = output_names[l]
            if n_name[0] == "r":
                pass
            else:
                to_play = []
                if "crash" in n_name:
                    chosen_crash = crashes[randint(0, 1)]
                    to_play.append(chosen_crash)
                if "ride" in n_name:
                    chosen_ride = rides[randint(0, 1)]
                    to_play.append(chosen_ride)
                if "bass" in n_name:
                    to_play.append(bass_drum_1)
                if "hatopen" in n_name:
                    to_play.append(open_hi_hat)
                if "hatclosed" in n_name:
                    to_play.append(closed_hi_hat)
                if "hatpedal" in n_name:
                    to_play.append(pedal_hi_hat)
                if "snare" in n_name:
                    to_play.append(tap_snare)
                if "stick" in n_name:
                    to_play.append(side_stick)


def play_pattern(info, pattern, brush):
    tempo, beats, c_beat, measure = info[0], info[1], info[2], info[3]
    
    session = Session(tempo=tempo)
    drummer = session.new_part("Brush", soundfont=drum_soundfont)
    
    if brush:
        fork(play_bg, args=(drummer,))
    
    while c_beat < len(beats):
        print(str(beats[c_beat]) + "/" + str(beats[-1]))
        print("measure:", str(measure))
        pattern(beats[c_beat], measure, drummer)
        c_beat += 1
        if c_beat == len(beats):
            measure += 1
            c_beat = 0
