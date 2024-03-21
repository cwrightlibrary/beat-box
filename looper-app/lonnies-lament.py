from libs.image_gen import *
from libs.midi_mapping import *
from libs.note_lengths import *
from libs.looper import *

info = ["Treble", C, "4/4"]
notes = "r/3 g4/.5 f4/.5 !cm7 e-4/1.5 d4/.25 c4/.25 !dm7 d4/.5 f4/1.5 !e-maj7"

music(info, notes, "Lonnie's Lament", False, False)
