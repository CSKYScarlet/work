# https://musescore.com/user/29424327/scores/6488313
# https://web.mit.edu/music21/doc/moduleReference/moduleDynamics.html

from music21 import *
from os import *

s = stream.Score(id="mainScore")
s.append(tempo.MetronomeMark(number=65))
p0 = stream.Part(id="part0")
p1 = stream.Part(id="part1")

sm00 = stream.Measure()
ts_four_four = meter.TimeSignature("4/4")
sm00.insert(0, ts_four_four)
sm00.insert(0, key.KeySignature(-3))
sm00.insert(0, clef.TrebleClef())

sm01 = stream.Measure()
ts_four_four = meter.TimeSignature("4/4")
sm01.insert(0, ts_four_four)
sm01.insert(0, key.KeySignature(-3))
sm01.insert(0, clef.BassClef())

def note_def_sm00(note_value, quarter):
    sm00.append(chord.Chord(note_value, quarterLength = quarter))
def rest_def_sm00(quarter):
    sm00.append(note.Rest(quarterLength = quarter))
    
def note_def_sm01(note_value, quarter):
    sm01.append(chord.Chord(note_value, quarterLength = quarter))
def rest_def_sm01(quarter):
    sm01.append(note.Rest(quarterLength = quarter))
    
#------------------------------------------------------
sm00.append(dynamics.Dynamic("p"))
# 1
note_def_sm00("C6", 4)

# 2
note_def_sm00("B-5", 4)

# 3
note_def_sm00("E-6", 3)
note_def_sm00("E-6", 1)

# 4
note_def_sm00("B-5", 4)

# 5
note_def_sm00("C6", 4)

# 6
note_def_sm00("B-5", 4)

# 7
note_def_sm00("F6", 1)
note_def_sm00("E-6", 3)

# 8
rest_def_sm00(4)

sm00.append(dynamics.Dynamic("mp"))
# 9
note_def_sm00("C7", 4)

# 10
note_def_sm00("B-6", 4)

# 11
note_def_sm00("E-7", 3)
note_def_sm00("E-7", 1)

# 12
note_def_sm00("B-6", 4)

# 13
note_def_sm00("C7", 4)

# 14
note_def_sm00("B-6", 4)

# 15
note_def_sm00("F7", 1)
note_def_sm00("E-7", 3)

# 16
note_def_sm00("G7", 4)

sm00.append(dynamics.Dynamic("p"))
# 17
note_def_sm00(["G4", "G5"], 4)

# 18
note_def_sm00(["E-4", "E-5"], 4)

# 19
note_def_sm00(["B-4", "B-5"], 4)

# 20
note_def_sm00(["G4", "G5"], 3.75)
sm00.append(dynamics.Dynamic("mp"))
note_def_sm00("G4", 0.25)

# 21
note_def_sm00(["A-3", "A-4"], 4)

# 22
sm00.append(chord.Chord(["B-3", "B-4"], quarterLength = 2))
note_def_sm00(["G3", "G4"], 2)

# 23
note_def_sm00("A-4", 0.75)
note_def_sm00("G4", 0.25)
note_def_sm00("A-4", 0.5)
note_def_sm00("G4", 1)
note_def_sm00("F4", 1)
note_def_sm00("E-4", 0.5)

# 24
# diminuendo
note_def_sm00(["F3", "F4"], 3.5)
sm00.append(dynamics.Dynamic("p"))
rest_def_sm00(0.5)

# 25
sm00.append(dynamics.Dynamic("mp"))
note_def_sm00("E-4", 2)
note_def_sm00("F4", 2)

# 26
note_def_sm00("B-4", 2)
note_def_sm00("E-4", 2)

# 27
# diminuendo
note_def_sm00("F4", 3.75)
sm00.append(dynamics.Dynamic("p"))
note_def_sm00("G4", 0.25)

# 28
sm00.append(dynamics.Dynamic("mp"))
note_def_sm00(["A-4", "A-5"], 2)
note_def_sm00(["G4", "G5"], 2)

# 29
note_def_sm00(["B-4", "B-5"], 2)
note_def_sm00(["G4", "G5"], 1.75)
note_def_sm00("G4", 0.25)

# 30
note_def_sm00(["A-4", "A-5"], 0.75)
note_def_sm00(["G4", "G5"], 0.25)
note_def_sm00(["A-4", "A-5"], 0.5)
note_def_sm00(["G4", "G5"], 1)
note_def_sm00(["F4", "F5"], 1)
note_def_sm00(["E-4", "E-5"], 0.5)

# 31
# diminuendo
note_def_sm00(["F4", "F5"], 3.5)
sm00.append(dynamics.Dynamic("pp"))
rest_def_sm00(0.5)

# 32
# crescendo
sm00.append(dynamics.Dynamic("p"))
note_def_sm00(["E-3", "E-4"], 2)
note_def_sm00(["F3", "F4"], 2)

# 33
note_def_sm00(["B-3", "B-4"], 2)
note_def_sm00(["A-3", "A-4"], 0.75)
note_def_sm00(["G3", "G4"], 0.75)
note_def_sm00(["F3", "F4"], 0.5)

# 34
sm00.append(dynamics.Dynamic("mf"))
note_def_sm00("D5", 1)
note_def_sm00("B-4", 1)
a = chord.Chord(["G4", "G5"], quarterLength = 1)
a.articulations = [articulations.Accent()]
sm00.append(a)
a = chord.Chord(["B-4", "B-5"], quarterLength = 1)
a.articulations = [articulations.Accent()]
sm00.append(a)

# 35
a = chord.Chord(["F5", "F6"], quarterLength = 2)
a.articulations = [articulations.Accent()]
sm00.append(a)
note_def_sm00("G5", 1)
note_def_sm00("B-5", 1)

# 36
a = chord.Chord(["G5", "G6"], quarterLength = 2)
a.articulations = [articulations.Accent()]
sm00.append(a)
note_def_sm00("G5", 1)
note_def_sm00("B-5", 1)

# 37
note_def_sm00(["A-5", "A-6"], 0.75)
note_def_sm00(["G5", "G6"], 0.25)
note_def_sm00(["A-5", "A-6"],0.5)
note_def_sm00(["G5", "G6"], 1)
note_def_sm00(["F5", "F6"], 1)
note_def_sm00(["E-5", "E-6"], 0.5)

# 38
# decrescendo
note_def_sm00(["B-4", "B-5"], 4)
# crescendo
sm00.append(dynamics.Dynamic("pp"))

# 39
# crescendo
sm00.append(dynamics.Dynamic("mp"))
note_def_sm00(["E-4", "B-4", "E-5"], 1)
note_def_sm00(["F4", "F5"], 1)
note_def_sm00("E-4", 0.25)
note_def_sm00("G4", 0.25)
note_def_sm00("A-4", 0.25)
note_def_sm00("G4", 0.25)
note_def_sm00(["E-4", "E-5"], 1)

# 40
note_def_sm00(["G4", "B-4", "G5"], 1)
note_def_sm00(["F4", "C5", "F5"], 1)
for repeat in range(2):
    note_def_sm00("E-4", 0.25)
    note_def_sm00("F4", 0.25)
note_def_sm00(["F4", "F5"], 0.5)
note_def_sm00(["G4", "G5"], 0.5)

# 41
note_def_sm00(["A-4", "A-5"], 1)
note_def_sm00(["B-4", "B-5"], 3)
sm00.append(dynamics.Dynamic("mf"))# crescendo

# 42
sm00.append(dynamics.Dynamic("ff"))
note_def_sm00(["B4", "E-5", "B5"], 4 * 2)# fermata

# 43
sm00.append(dynamics.Dynamic("mp"))
note_def_sm00("C6", 4)

# 44
note_def_sm00("B-5", 4)

# 45
note_def_sm00("E-6", 3)
note_def_sm00("E-6", 1)

# 46
note_def_sm00("B-5", 4)

# 47
note_def_sm00("C6", 4)

# 48
note_def_sm00("B-5", 4)

# 49
note_def_sm00("F6", 1)
note_def_sm00("E-6", 3)

# 50
rest_def_sm00(4)

#------------------------------------------------------
sm01.append(dynamics.Dynamic("p"))
# s1
note_def_sm01(["A-2", "E-3"], 4)

# s2
note_def_sm01(["C3", "E-3"], 4)

# s3
note_def_sm01(["G2", "E-3"], 4)

# s4
note_def_sm01(["E-2", "G2"], 4)

# s5
note_def_sm01(["A-2", "E-3"], 4)

# s6
note_def_sm01(["C3", "E-3"], 4)

# s7
note_def_sm01(["G2", "E-3"], 2)
note_def_sm01("B-2", 2)

# s8
note_def_sm01(["B1", "E-3"], 4)

sm01.append(dynamics.Dynamic("mp"))
# s9
note_def_sm01(["A-2", "E-3"], 0.5)
for repeat in range(4):
    note_def_sm01("A-3", 0.25)
    note_def_sm01("A-2", 0.25)
    note_def_sm01("E-3", 0.25)
note_def_sm01("A-3", 0.25)
note_def_sm01("E-3", 0.25)

# s10
note_def_sm01(["C3", "E-3"], 0.5)
for repeat in range(4):
    note_def_sm01("A-3", 0.25)
    note_def_sm01("A-2", 0.25)
    note_def_sm01("E-3", 0.25)
note_def_sm01("A-3", 0.25)
note_def_sm01("E-3", 0.25)

# s11
note_def_sm01(["G2","E-3"], 0.5)
for repeat in range(4):
    note_def_sm01("G3", 0.25)
    note_def_sm01("G2", 0.25)
    note_def_sm01("E-3", 0.25)
note_def_sm01("G3", 0.25)
note_def_sm01("E-3", 0.25)

# s12
note_def_sm01(["E-2", "G2"], 0.5)
for repeat in range(4):
    note_def_sm01("E-3", 0.25)
    note_def_sm01("E-2", 0.25)
    note_def_sm01("B-2", 0.25)
note_def_sm01("E-3", 0.25)
note_def_sm01("B-2", 0.25)

# s13
note_def_sm01(["A-2", "E-3"], 0.5)
for repeat in range(4):
    note_def_sm01("A-3", 0.25)
    note_def_sm01("A-2", 0.25)
    note_def_sm01("E-3", 0.25)
note_def_sm01("A-3", 0.25)
note_def_sm01("E-3", 0.25)

# s14
note_def_sm01(["C3", "E-3"], 0.5)
for repeat in range(4):
    note_def_sm01("A-3", 0.25)
    note_def_sm01("A-2", 0.25)
    note_def_sm01("E-3", 0.25)
note_def_sm01("A-3", 0.25)
note_def_sm01("E-3", 0.25)

# s15
note_def_sm01(["G2", "E-3"], 0.5)
for repeat in range(2):
    note_def_sm01("G3", 0.25)
    note_def_sm01("G2", 0.25)
    note_def_sm01("E-3", 0.25)
note_def_sm01(["B-2", "B-3"], 0.5)
for repeat in range(2):
    note_def_sm01("B-3", 0.25)
    note_def_sm01("B-2", 0.25)
    note_def_sm01("E-3", 0.25)
    
# s16
note_def_sm01(["E-2", "E-3"], 0.5)
for repeat in range(4):
    note_def_sm01("E-3", 0.25)
    note_def_sm01("E-2", 0.25)
    note_def_sm01("B-2", 0.25)
note_def_sm01("E-3", 0.25)
note_def_sm01("B-2", 0.25)

sm01.append(dynamics.Dynamic("p"))
# s17
note_def_sm01(["E-1", "E-2"], 0.5)
for repeat in range(4):
    note_def_sm01("F3", 0.25)
    note_def_sm01("F2", 0.25)
    note_def_sm01("C3", 0.25)
note_def_sm01("F3", 0.25)
note_def_sm01("C3", 0.25)

# s18
note_def_sm01(["G1", "G2"], 0.5)
for repeat in range(4):
    note_def_sm01("G3", 0.25)
    note_def_sm01("G2", 0.25)
    note_def_sm01("E-3", 0.25)
note_def_sm01("G3", 0.25)
note_def_sm01("E-3", 0.25)

# s19
note_def_sm01(["D1", "D2"], 0.5)
for repeat in range(4):
    note_def_sm01("D3", 0.25)
    note_def_sm01("D2", 0.25)
    note_def_sm01("B-2", 0.25)
note_def_sm01("D3", 0.25)
note_def_sm01("B-2", 0.25)

# s20
# crescendo
note_def_sm01(["E-1", "E-2"], 0.5)
for repeat in range(4):
    note_def_sm01("E-3", 0.25)
    if repeat == 3:
        sm01.append(dynamics.Dynamic("mp"))
    note_def_sm01("E-2", 0.25)
    note_def_sm01("B-2", 0.25)
note_def_sm01("E-3", 0.25)
note_def_sm01("B-2", 0.25)

# s21
note_def_sm01(["F1","F2"], 0.5)
for repeat in range(4):
    note_def_sm01("F3", 0.25)
    note_def_sm01("F2", 0.25)
    note_def_sm01("C3", 0.25)
note_def_sm01("F3", 0.25)
note_def_sm01("C3", 0.25)

# s22
note_def_sm01(["C1", "C2"], 0.5)
for repeat in range(4):
    note_def_sm01("C3", 0.25)
    note_def_sm01("C2", 0.25)
    note_def_sm01("G2", 0.25)
note_def_sm01("C3", 0.25)
note_def_sm01(["G2", "G4"], 0.25)

# s23
note_def_sm01(["E-1", "E-2"], 0.5)
for repeat in range(4):
    note_def_sm01("E-3", 0.25)
    note_def_sm01("E-2", 0.25)
    note_def_sm01("B-2", 0.25)
note_def_sm01("E-3", 0.25)
note_def_sm01("B-2", 0.25)

# s24
# diminuendo
note_def_sm01(["B-1", "B-0"], 0.5)
for repeat in range(4):
    note_def_sm01("B-2", 0.25)
    if repeat == 3:
        sm01.append(dynamics.Dynamic("p"))
    note_def_sm01("B-1", 0.25)
    note_def_sm01("F2", 0.25)
note_def_sm01("B-2", 0.25)
note_def_sm01("F2", 0.25)

# s25
sm01.append(dynamics.Dynamic("mp"))
note_def_sm01(["C2", "C3"], 0.5)
for repeat in range(4):
    note_def_sm01("C3", 0.25)
    note_def_sm01("C2", 0.25)
    note_def_sm01("G2", 0.25)
note_def_sm01("C3", 0.25)
note_def_sm01("G2", 0.25)

# s26
note_def_sm01(["G1", "G2"], 0.5)
for repeat in range(2):
    note_def_sm01("G2", 0.25)
    note_def_sm01("G1", 0.25)
    note_def_sm01("D2", 0.25)
for repeat in range(2):
    note_def_sm01("B-2", 0.25)
    note_def_sm01("B-1", 0.25)
    note_def_sm01("E-2", 0.25)
note_def_sm01("B-2", 0.25)
note_def_sm01("E-2", 0.25)

# s27
# diminuendo
note_def_sm01(["G1", "G2"], 0.5)
for repeat in range(4):
    note_def_sm01("G2", 0.25)
    if repeat == 3:
        sm01.append(dynamics.Dynamic("p"))
    note_def_sm01("G1", 0.25)
    note_def_sm01("D2", 0.25)
note_def_sm01("G2", 0.25)
note_def_sm01("D2", 0.25)

# s28
sm01.append(dynamics.Dynamic("mp"))
note_def_sm01(["F1", "F2"], 0.5)
for repeat in range(4):
    note_def_sm01("F3", 0.25)
    note_def_sm01("F2", 0.25)
    note_def_sm01("C3", 0.25)
note_def_sm01("F3", 0.25)
note_def_sm01("C3", 0.25)

# s29
note_def_sm01(["C2", "C3"], 0.5)
for repeat in range(4):
    note_def_sm01("C3", 0.25)
    note_def_sm01("C2", 0.25)
    note_def_sm01("G2", 0.25)
note_def_sm01("C3", 0.25)
note_def_sm01("G2", 0.25)

# s30
note_def_sm01(["E-1", "E-2"], 0.5)
for repeat in range(4):
    note_def_sm01("E-3", 0.25)
    note_def_sm01("E-2", 0.25)
    note_def_sm01("B-2", 0.25)
note_def_sm01("E-3", 0.25)
note_def_sm01("B-2", 0.25)

# s31
# diminuendo
note_def_sm01(["B-0", "B-1"], 0.5)
for repeat in range(4):
    note_def_sm01("B-2", 0.25)
    if repeat == 3:
        sm01.append(dynamics.Dynamic("pp"))
    note_def_sm01("B-1", 0.25)
    note_def_sm01("F2", 0.25)
note_def_sm01("B-2", 0.25)
note_def_sm01("F2", 0.25)

# s32
# crescendo
sm01.append(dynamics.Dynamic("p"))
note_def_sm01(["C2", "C3"], 0.5)
for repeat in range(4):
    note_def_sm01("C3", 0.25)
    note_def_sm01("C2", 0.25)
    note_def_sm01("G2", 0.25)
note_def_sm01("C3", 0.25)
note_def_sm01("G2", 0.25)

# s33
note_def_sm01(["G1", "G2"], 0.5)
for repeat in range(2):
    note_def_sm01("G2", 0.25)
    note_def_sm01("G1", 0.25)
    note_def_sm01("D2", 0.25)
for repeat in range(2):
    note_def_sm01("B-2", 0.25)
    note_def_sm01("B-1", 0.25)
    note_def_sm01("E-2", 0.25)
note_def_sm01("B-2", 0.25)
note_def_sm01("E-2", 0.25)

# s34
sm01.append(dynamics.Dynamic("mf"))
note_def_sm01(["G1", "G2"], 0.5)
for repeat in range(4):
    note_def_sm01("G2", 0.25)
    note_def_sm01("G1", 0.25)
    note_def_sm01("D2", 0.25)
note_def_sm01("G2", 0.25)
note_def_sm01("D2", 0.25)

# s35
note_def_sm01(["C2", "C3"], 0.5)
for repeat in range(2):
    note_def_sm01(["C3", "F4"], 0.25)
    note_def_sm01(["C2", "D4"], 0.25)
    note_def_sm01(["G2", "E-4"], 0.25)
note_def_sm01(["C3", "G4"], 0.25)
note_def_sm01(["C2", "A-4"], 0.25)
note_def_sm01(["G2", "G4"], 0.25)
note_def_sm01(["C3", "F4"], 0.25)
note_def_sm01(["C2", "B-4"], 0.25)
note_def_sm01(["G2", "D4"], 0.25)
note_def_sm01(["C3", "C4"], 0.25)
note_def_sm01(["G2", "B-3"], 0.25)

# s36
note_def_sm01(["B-0", "B-1"], 0.5)
note_def_sm01(["B-2", "C5"], 0.25)
note_def_sm01(["B-1", "F4"], 0.25)
note_def_sm01(["F2", "G4"], 0.25)
note_def_sm01(["B-2", "C5"], 0.25)
note_def_sm01(["B-1", "F4"], 0.25)
note_def_sm01(["F2", "G4"], 0.25)
note_def_sm01(["B-2", "G4"], 0.25)
note_def_sm01(["B-1", "A-4"], 0.25)
note_def_sm01(["F2", "G4"], 0.25)
note_def_sm01(["B-2", "F4"], 0.25)
note_def_sm01(["B-1", "B-4"], 0.25)
note_def_sm01(["F2", "E-4"], 0.25)
note_def_sm01(["B-2", "D4"], 0.25)
note_def_sm01(["F2", "C4"], 0.25)

# s37
note_def_sm01(["E-1", "E2"], 0.5)
for repeat in range(4):
    note_def_sm01("E-3", 0.25)
    note_def_sm01("E-2", 0.25)
    note_def_sm01("B-2", 0.25)
note_def_sm01("E-3", 0.25)
note_def_sm01("B-2", 0.25)

# s38
# decrescendo
note_def_sm01(["B-0", "B-1"], 0.5)
note_def_sm01(["B-2", "E-5"], 0.25)
note_def_sm01(["B-1", "A-4"], 0.25)
note_def_sm01(["F2", "F4"], 0.25)
note_def_sm01(["B-2", "C5"], 0.25)
note_def_sm01(["B-1", "F4"], 0.25)
note_def_sm01("F2", 0.25)
sm01.append(dynamics.Dynamic("pp"))
# crescendo
note_def_sm01(["B-2", "F4"], 0.25)
note_def_sm01("B-1", 0.25)
note_def_sm01(["F2", "F4"], 0.25)
note_def_sm01(["B-2", "G4"], 0.25)
note_def_sm01(["B-1", "A-4", "A-5"], 0.25)
note_def_sm01("F2", 0.25)
note_def_sm01(["B-2", "G4", "G5"], 0.25)
note_def_sm01("F2", 0.25)

# s39
sm01.append(dynamics.Dynamic("mp"))
# crescendo
note_def_sm01(["G2", "G3"], 0.5)
for repeat in range(4):
    note_def_sm01("G3", 0.25)
    note_def_sm01("G2", 0.25)
    note_def_sm01("E-3", 0.25)
note_def_sm01("G3", 0.25)
note_def_sm01("E-3", 0.25)

# s40
note_def_sm01(["F2", "F3"], 0.5)
for repeat in range(4):
    note_def_sm01("F3", 0.25)
    note_def_sm01("F2", 0.25)
    note_def_sm01("C3", 0.25)
note_def_sm01("F3", 0.25)
note_def_sm01("C3", 0.25)

# s41
note_def_sm01(["D1", "D2", "D5"], 0.5)
for repeat in range(3):
    note_def_sm01(["D3", "D5"], 0.5)
sm01.append(dynamics.Dynamic("mf"))
# crescendo
note_def_sm01(["E-1", "E-2", "E-5"], 0.5)
for repeat in range(3):
    note_def_sm01(["E-3", "E-5"], 0.5)
    
# s42
sm01.append(dynamics.Dynamic("ff"))
note_def_sm01(["B1", "B2"], 4 * 2)# fermata

# s43
sm01.append(dynamics.Dynamic("mp"))
note_def_sm01(["A-2", "E-3"], 0.5)
for repeat in range(4):
    note_def_sm01("A-3", 0.25)
    note_def_sm01("A-2", 0.25)
    note_def_sm01("E-3", 0.25)
note_def_sm01("A-3", 0.25)
note_def_sm01("E-3", 0.25)

# s44
note_def_sm01(["C3", "E-3"], 0.5)
for repeat in range(4):
    note_def_sm01("A-3", 0.25)
    note_def_sm01("A-2", 0.25)
    note_def_sm01("E-3", 0.25)
note_def_sm01("A-3", 0.25)
note_def_sm01("E-3", 0.25)

# s45
note_def_sm01(["G2", "E-3"], 0.5)
for repeat in range(4):
    note_def_sm01("G3", 0.25)
    note_def_sm01("G2", 0.25)
    note_def_sm01("E-3", 0.25)
note_def_sm01("G3", 0.25)
note_def_sm01("E-3", 0.25)

# s46
note_def_sm01(["E-2", "G2"], 0.5)
for repeat in range(4):
    note_def_sm01("E-3", 0.25)
    note_def_sm01("E-2", 0.25)
    note_def_sm01("B-2", 0.25)
note_def_sm01("E-3", 0.25)
note_def_sm01("B-2", 0.25)

# s47
note_def_sm01(["A-2", "E-3"], 0.5)
for repeat in range(4):
    note_def_sm01("A-3", 0.25)
    note_def_sm01("A-2", 0.25)
    note_def_sm01("E-3", 0.25)
note_def_sm01("A-3", 0.25)
note_def_sm01("E-3", 0.25)

# s48
note_def_sm01(["C3", "E-3"], 0.5)
for repeat in range(4):
    note_def_sm01("A-3", 0.25)
    note_def_sm01("A-2", 0.25)
    note_def_sm01("E-3", 0.25)
note_def_sm01("A-3", 0.25)
note_def_sm01("E-3", 0.25)

# s49
note_def_sm01(["G2", "E-3"], 0.5)
for repeat in range(2):
    note_def_sm01("G3", 0.25)
    note_def_sm01("G2", 0.25)
    note_def_sm01("E-3", 0.25)
note_def_sm01(["B-2", "B-3"], 0.5)
for repeat in range(2):
    note_def_sm01("B-3", 0.25)
    note_def_sm01("B-2", 0.25)
    note_def_sm01("E-3", 0.25)

# s50
sm01.append(dynamics.Dynamic("p"))
note_def_sm01(["B1", "E-3"], 4 * 2)

#------------------------------------------------------

p0.append(sm00)
p1.append(sm01)
s.insert(0, p0)
s.insert(0, p1)

# s.show("midi")
s.show("text")
system("Deep-Stone_Lullaby.mp3")

# s.write("midi", fp="Deep-Stone_Lullaby.midi")
# s.write("xml", fp="Deep-Stone_Lullaby.xml")