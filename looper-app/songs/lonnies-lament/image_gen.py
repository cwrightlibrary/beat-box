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
    doubles = []
    voltas = []
    
    split_notes = notes.split(" ")
    for n in split_notes:
        if n[0] == "!":
            part.append(harmony.ChordSymbol(n[1:]))
        elif "[" in n:
            repeats = n.replace("[", "").split("]")
            n = ""
        elif "]" in n:
            voltas = n.replace("]", "").split("@")
        elif "|" in n:
            doubles = n.replace("|", "").split("&")
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
    
    for d in doubles:
        measures[int(d) - 1].rightBarline = bar.Barline("double")
    
    for r in repeats:
        if "s" in r:
            measures[int(r[0]) - 1].leftBarline = bar.Repeat(direction="start")
        if "e" in r:
            measures[int(r[0]) - 1].rightBarline = bar.Repeat(direction="end")
    
    new_voltas = []
    for v in voltas:
        if "-" in v:
            mv = v.split("-")
            new_voltas.append(mv)
        else:
            new_voltas.append(v)
    
    for v in new_voltas:
        if isinstance(v, list):
            new_v = v[0].split("i")
            while("" in new_v):
                new_v.remove("")
            repeat_number = int(new_v[0])
            start = int(new_v[1]) - 1
            end = int(v[1])
            measures[start].append(spanner.RepeatBracket(measures[start:end], number=repeat_number))
        else:
            new_v = v.split("i")
            while("" in new_v):
                new_v.remove("")
            repeat_number = int(new_v[0])
            vol = int(new_v[1]) - 1
            measures[vol].append(spanner.RepeatBracket(measures[vol], number=repeat_number))
    
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

# EXAMPLES
# c5/1 is middle C quarter note length
# !cmaj7 is a chord symbol for Cmaj7
# { starts a tie, } ends a tie
# ^ ends the current measure and starts a new line
# [2s]9e[ puts a start repeat on the 2nd measure, end repeat on the 9th measure
# ]i1i7-9@i2i10-12] puts a repeat bracket over measures 7-9 with a 1, and a bracket
# over 10-12 with a 2
# |12&20| puts double barlines on measures 12 and 20
info = ["Treble", C, "4/4"]
notes = "r/3 g4/.5 f4/.5 !cm7 e-4/1.5 d4/.25 c4/.25 !dm7 d4/.5 f4/1.5 !e-maj7"

music(info, notes, "Lonnie's Lament", False, False)