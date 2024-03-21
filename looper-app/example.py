from libs.image_gen import *

# EXAMPLES
# c5/1 is middle C quarter note length
# !cmaj7 is a chord symbol for Cmaj7
# { starts a tie, } ends a tie
# ^ ends the current measure and starts a new line
# [2s]9e[ puts a start repeat on the 2nd measure, end repeat on the 9th measure
# ]i1i7-9@i2i10-12] puts a repeat bracket over measures 7-9 with a 1, and a bracket
# over 10-12 with a 2
# |12&20| puts double barlines on measures 12 and 20

info = ["Treble", G, "4/4"]
notes = "r/1 e4/1 f#4/1 g4/1 !am7 c5/4{ !d7 c5/1} d4/1 e4/1 f#4/1 !gmaj7 b4/2 b4/2{ ^"
notes += " !cmaj7 b4/1} c4/1 d4/1 e4/1 !f#m7b5 a4/4{ !b7 a4/1} b3/1 c#4/1 d#4/1 !em g4/4 ^"
notes += " r/1 e4/1 f#4/1 g4/1 !b7 a4/1 f#4/1 a4/1 g4/1 !em e4/4{ e4/1} r/1 d#4/1 e4/1 ^"

notes += " !f#m7b5 f#4/1 b3/1 f#4/2{ !b7b9 f#4/1} f#4/1 e4/1 f#4/1 !em g4/4{ g4/1} g4/1 f#4/1 g4/1 ^"
notes += " !am7 a4/4{ !d7 a4/1} d4/1 d5/1 c5/1 !gmaj7 b4/4{ b4/1} r/1 a#4/1 b4/1 ^"

notes += " !f#m7b5 c5/1 c5/1 a4/1 a4/1 !b7b9 f#4/3 c5/1 !em7 b4/2 !e-7 b4/2{ !dm7 b4/2{ !d-7 b4/1} e4/1 ^"
notes += " !cmaj7 a4/3 g4/1 !b7b9 f#4/2 g4/1 b3/1 !em e4/4 r/1 e4/1 f#4/1 g4/1"

notes += " [2s]9e[ ]i1i7-9@i2i10-12] |12&20|"

music(info, notes, "example", False, False)
