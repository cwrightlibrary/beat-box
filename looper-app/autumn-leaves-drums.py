from libs.drum_gen import *
from os.path import dirname, join, realpath
from scamp import *
from time import sleep

TEMPO = 150

BEATS = [1, 2, 3, 4]
C_BEAT = 0
MEASURE = 1


def test_pattern(beat, measure, drummer):
    if beat == 1:
        playnote([KICK, RIDE], quarter_note, 1, drummer)
    elif beat == 2:
        playnote([SNARE, RIDE], triplet_quarter_note * 2, 1, drummer)
        playnote([KICK, RIDE], triplet_quarter_note, 1, drummer)
    elif beat == 3:
        playnote([RIDE], triplet_quarter_note, 1, drummer)
        playnote([SNARE], triplet_quarter_note * 2, 0.3, drummer)
    elif beat == 4:
        playnote([SNARE, RIDE], triplet_quarter_note * 2, 1, drummer)
        playnote([SNARE], triplet_quarter_note, 0.4, drummer)


def autumn_leaves_drums(beat, measure, drummer):
    if measure == 1:
        if beat == 1 or beat == 2 or beat == 3 or beat == 4:
            playnote([HI_HAT_PEDAL], quarter_note, 1, drummer)
    elif measure in [2, 4, 6, 8, 10, 12, 14, 16]:
        if beat == 1:
            playnote([None], quarter_note, 0, drummer)
        elif beat == 2:
            playnote([None], quarter_note, 0, drummer)
        elif beat == 3:
            playnote([KICK, RIDE, CRASH], quarter_note, 1, drummer)
        elif beat == 4:
            playnote([None], triplet_quarter_note * 2, 0, drummer)
            playnote([KICK, RIDE, CRASH], triplet_quarter_note, 1, drummer)
    elif measure in [3, 5, 7, 9, 11, 13, 15, 17]:
        if beat == 1 or beat == 2 or beat == 3 or beat == 4:
            drummer.end_note(KICK)
            drummer.end_note(RIDE)
            drummer.end_note(CRASH)
            playnote([None], quarter_note, 0, drummer)
    else:
        if beat == 1:
            playnote([KICK, RIDE], quarter_note, 1, drummer)
        elif beat == 2:
            playnote([SNARE, RIDE], triplet_quarter_note * 2, 1, drummer)
            playnote([KICK, RIDE], triplet_quarter_note, 1, drummer)
        elif beat == 3:
            playnote([RIDE], triplet_quarter_note, 1, drummer)
            playnote([SNARE], triplet_quarter_note * 2, 0.3, drummer)
        elif beat == 4:
            playnote([SNARE, RIDE], triplet_quarter_note * 2, 1, drummer)
            playnote([SNARE], triplet_quarter_note, 0.4, drummer)


info = [TEMPO, BEATS, C_BEAT, MEASURE]

play_pattern(info, autumn_leaves_drums, True)
