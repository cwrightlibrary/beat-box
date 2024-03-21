from music21 import *
from os.path import dirname, join, realpath
from os import remove, rename

current_dir = dirname(realpath(__file__))

C = 0
G = 1
D = 2
A = 3
E = 4
B = 5
Cb = -7

F = -1
Bb = -2
Eb = -3
Ab = -4
Db = -5
Cs = 7

Gb = -6
Fs = 6



from music21 import *
from IPython.display import Image


def music(info: list, notes: str, song_name: str, midi=False, swing=False):
    s = stream.Score()
    part = stream.Part()
    if info[0] == "Treble":
        part.append(clef.TrebleClef())
    elif info[0] == "Bass":
        part.append(clef.BassClef)
    elif info[0] == "None":
        part.append(clef.NoClef())
    part.append(key.KeySignature(info[1]))
    part.append(meter.TimeSignature(info[2]))

    repeats = []
    voltas = []
    
    split_notes = notes.split(" ")
    for n in split_notes:
        if n[0] == "!":
            part.append(harmony.ChordSymbol(n[1:]))
        elif "[" in n:
            repeats = n.replace("[", "").split("]")
            n = ""
        elif "]" in n:
            voltas = n.replace("]", "").split("%")
        elif n == "^":
            part.append(layout.SystemLayout(isNew=True))
        else:
            is_chord = False
            is_tie = "none"
            note_and_length = n.split("/")
            if "(" in note_and_length[0]:
                is_chord = True
                chord_name = (
                    note_and_length[0].replace("(", "").replace(")", "").split("$")
                )
            else:
                note_name = note_and_length[0]
            if "{" in note_and_length[1]:
                is_tie = "start"
                note_and_length[1] = note_and_length[1].replace("{", "")
            if "}" in note_and_length[1]:
                is_tie = "stop"
                note_and_length[1] = note_and_length[1].replace("}", "")
            if "*" in note_and_length[1]:
                length_and_col = note_and_length[1].split("*")
                note_length = length_and_col[0]
                note_col = length_and_col[1]
            else:
                note_length = note_and_length[1]
                note_col = ""
            if note_length == "0.3":
                note_length = 0.333333333
            else:
                note_length = float(note_length)
            if is_chord:
                add_n = chord.Chord(chord_name, quarterLength=note_length)
            else:
                if note_name.lower() == "r":
                    add_n = note.Rest(quarterLength=note_length)
                else:
                    add_n = note.Note(note_name, quarterLength=note_length)
            if is_tie != "none":
                add_n.tie = tie.Tie(is_tie)
            if note_col != "":
                add_n.style.color = note_col
            
            if midi and swing:
                for n in part:
                    if isinstance(n, note.Note) or isinstance(n, note.Rest):
                        if n.duration.quarterLength == 0.5:
                            print(n.name, n.offset)
                            if ".75" in str(n.offset):
                                n.duration.quarterLength = 0.25
                            elif ".0" in str(n.offset) or ".5" in str(n.offset):
                                n.duration.quarterLength = 0.75
            part.append(add_n)

    measures = part.makeMeasures()
    
    for r in repeats:
        if "s" in r:
            measures[int(r[0]) - 1].leftBarline = bar.Repeat(direction="start")
        if "e" in r:
            measures[int(r[0]) - 1].rightBarline = bar.Repeat(direction="end")
    
    for v in voltas:
        if "-" in v:
            v = v.split("-")
        if isinstance(v, list):
            measures[mn - 1].append(spanner.RepeatBracket(measures[mn - 1], number=1))
        else:
            measures[int(v[1]) - 1].append(spanner.RepeatBracket(measures[int(v[1]) - 1], number=2))
    
    part = stream.Part()
    for m in measures:
        part.append(m)
    
    s.append(part)
    
    if midi:
        s.write("midi", join(current_dir, song_name + ".mid"))
    else:
        s.write("musicxml.png", join(current_dir, song_name + ".png"))
        remove(join(current_dir, song_name + ".musicxml"))
        rename(join(current_dir, song_name + "-1.png"), join(current_dir, song_name + ".png"))


info = ["Treble", G, "4/4"]
notes = "r/1 e4/1 f#4/1 g4/1 !am7 c5/4{ !d7 c5/1} d4/1 e4/1 f#4/1 !gmaj7 b4/2 b4/2{ ^"
notes += " !cmaj7 b4/1} c4/1 d4/1 e4/1 !f#m7b5 a4/4{ !b7 a4/1} b3/1 c#4/1 d#4/1 !em g4/4 ^"
notes += " r/1 e4/1 f#4/1 g4/1 !b7 a4/1 f#4/1 a4/1 g4/1 !em e4/4{ e4/1} r/1 d#4/1 e4/1 ^"

notes += " !f#m7b5 f#4/1 b3/1 f#4/2{ !b7b9 f#4/1} f#4/1 e4/1 f#4/1 !em g4/4{ g4/1} g4/1 f#4/1 g4/1 ^"
notes += " !am7 a4/4{ !d7 a4/1} d4/1 d5/1 c5/1 !gmaj7 b4/4{ b4/1} r/1 a#4/1 b4/1 ^"

notes += " !f#m7b5 c5/1 c5/1 a4/1 a4/1 !b7b9 f#4/3 c5/1 !em7 b4/2 !e-7 b4/2{ !dm7 b4/2{ !d-7 b4/1} e4/1 ^"
notes += " !cmaj7 a4/3 g4/1 !b7b9 f#4/2 g4/1 b3/1 !em e4/4 r/1 e4/1 f#4/1 g4/1"

notes += " [2s]9e[ ]7-9%10]"

music(info, notes, "Autumn Leaves", False, False)