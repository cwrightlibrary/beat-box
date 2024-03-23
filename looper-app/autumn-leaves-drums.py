from libs.drum_gen import *
from os.path import dirname, join, realpath
from scamp import *
from time import sleep

TEMPO = 150

BEATS = [1, 2, 3, 4]
C_BEAT = 0
MEASURE = C_BEAT


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


def autumn_leaves_drums(measure, drum):
    pass


info = [TEMPO, BEATS, C_BEAT, MEASURE]
test_pattern = [
    "r/h-0 crash,ride,bass/q-1 r/tq-0 r/tq-0 crash,ride,bass/tq-1",
    "r/h-0 crash,ride,bass/q-1 r/tq-0 r/tq-0 crash,ride,bass/tq-1",
    "r/h-0 crash,ride,bass/q-1 r/tq-0 r/tq-0 crash,ride,bass/tq-1",
    "r/h-0 crash,ride,bass/q-1 r/tq-0 r/tq-0 crash,ride,bass/tq-1"
]

parse_pattern(test_pattern)

# play_pattern(info, test_pattern, True)
