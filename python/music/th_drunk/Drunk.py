from music21 import *

s = stream.Score(id="mainScore")
s.append(tempo.MetronomeMark(number=120))
p0 = stream.Part(id = "part0")
p1 = stream.Part(id = "part1")
p2 = stream.Part(id = "part2")

sm00 = stream.Measure()
ts_four_four = meter.TimeSignature("4/4")
sm00.insert(0, ts_four_four)
sm00.insert(0, key.KeySignature(-1))
sm00.insert(0, clef.TrebleClef())

sm01 = stream.Measure()
ts_four_four = meter.TimeSignature("4/4")
sm01.insert(0, ts_four_four)
sm01.insert(0, key.KeySignature(-1))
sm01.insert(0, clef.TrebleClef())

sm02 = stream.Measure()
ts_four_four = meter.TimeSignature("4/4")
sm02.insert(0, ts_four_four)
sm02.insert(0, key.KeySignature(-1))
sm02.insert(0, clef.BassClef())

def note_def_sm00(note_value, quarter):
    sm00.append(chord.Chord(note_value, quarterLength = quarter))
def rest_def_sm00(quarter):
    sm00.append(note.Rest(quarterLength = quarter))
    
def note_def_sm01(note_value, quarter):
    sm01.append(chord.Chord(note_value, quarterLength = quarter))
def rest_def_sm01(quarter):
    sm01.append(note.Rest(quarterLength = quarter))
    
def note_def_sm02(note_value, quarter):
    sm02.append(chord.Chord(note_value, quarterLength = quarter))
def rest_def_sm02(quarter):
    sm02.append(note.Rest(quarterLength = quarter))
    
#---------------------------------------------------------------

# s1
rest_def_sm00(4)

# s2
rest_def_sm00(4)

# s3
rest_def_sm00(4)

# s4
rest_def_sm00(3)
note_def_sm00("A4", 0.5)
note_def_sm00("C5", 0.5)

for repeat in range(2):
    # s5
    note_def_sm00("D5", 3)
    note_def_sm00("C5", 0.5)
    note_def_sm00("D5", 0.5)

    # s6
    note_def_sm00("F5", 0.5)
    note_def_sm00("E5", 0.5)
    note_def_sm00("D5", 0.125)
    note_def_sm00("E5", 0.125)
    note_def_sm00("D5", 0.25)
    note_def_sm00("C5", 0.5)
    note_def_sm00("D5", 1)
    note_def_sm00("A4", 0.5)
    note_def_sm00("C5", 0.5)

    # s7
    note_def_sm00("D5", 2.5)
    note_def_sm00("D5", 0.5)
    note_def_sm00("E5", 0.5)
    note_def_sm00("F5", 0.5)

    # s8
    note_def_sm00("G5", 0.5)
    note_def_sm00("A5", 0.5)
    note_def_sm00("A5", 2)
    note_def_sm00("F5", 0.5)
    note_def_sm00("E5", 0.5)

    # s9
    note_def_sm00("D5", 3)
    note_def_sm00("C5", 0.5)
    note_def_sm00("D5", 0.5)

    if repeat == 1:
        break
    # s10
    note_def_sm00("F5", 0.5)
    note_def_sm00("E5", 0.5)
    note_def_sm00("D5", 0.125)
    note_def_sm00("E5", 0.125)
    note_def_sm00("D5", 0.25)
    note_def_sm00("C5", 0.5)
    note_def_sm00("D5", 1)
    note_def_sm00("C5", 0.5)
    note_def_sm00("G5", 0.5)

    # s11
    note_def_sm00("D5", 1)
    note_def_sm00("C5", 0.5)
    note_def_sm00("G5", 0.5)
    note_def_sm00("D5", 1)
    note_def_sm00("C5", 0.25)
    note_def_sm00("A4", 0.25)
    note_def_sm00(["A4", "C5"], 0.5)

    # s12
    note_def_sm00("D5", 0.5)
    note_def_sm00("D5", 2.5)
    note_def_sm00("A4", 0.5)
    note_def_sm00("C5", 0.5)

# s13
note_def_sm00("F5", 0.5)
note_def_sm00("E5", 0.5)
note_def_sm00("F5", 0.125)
note_def_sm00("E5", 0.125)
note_def_sm00("F5", 0.25)
note_def_sm00("G5", 0.5)
note_def_sm00("A5", 1)
note_def_sm00("A5", 0.5)
note_def_sm00("G5", 0.5)

# s14
note_def_sm00("F5", 1)
note_def_sm00("E5", 0.5)
note_def_sm00("D5", 0.5)
note_def_sm00("E5", 1)
note_def_sm00("A4", 0.5)
note_def_sm00("E5", 0.5)

# s15
note_def_sm00("E5", 0.25)
note_def_sm00("F5", 0.25)
note_def_sm00("D5", 1.5)
rest_def_sm00(1)

note_def_sm00("D6", 5)# to s16

# s17
note_def_sm00("A5", 1.5)
note_def_sm00("G5", 0.25)
note_def_sm00("A5", 0.25)
note_def_sm00("C6", 0.5)
note_def_sm00("B-5", 0.5)
note_def_sm00("A5", 0.5)
note_def_sm00("G5", 0.5)

# s18
note_def_sm00("F5", 2)
rest_def_sm00(2)

# s19
note_def_sm00("G5", 0.75)
note_def_sm00("A5", 1.25)
rest_def_sm00(1)
note_def_sm00("E5", 0.5)
note_def_sm00("G5", 0.5)

# s20
note_def_sm00("F5", 2)
rest_def_sm00(2)

# s21
note_def_sm00("A5", 1.5)
note_def_sm00("G5", 0.25)
note_def_sm00("A5", 0.25)
note_def_sm00("C6", 0.5)
note_def_sm00("B-5", 0.5)
note_def_sm00("A5", 0.5)
note_def_sm00("G5", 0.5)

# s22
note_def_sm00("F5", 1.5)
note_def_sm00("E5", 0.25)
note_def_sm00("F5", 0.25)
note_def_sm00("A5", 0.5)
note_def_sm00("G5", 0.5)
note_def_sm00("A5", 0.5)
note_def_sm00("C6", 0.5)

# s23
note_def_sm00("D6", 0.5)
note_def_sm00("D6", 0.5)
note_def_sm00("C6", 0.5)
note_def_sm00("A5", 0.25)
note_def_sm00("G5", 0.25)
note_def_sm00("A-5", 0.25)
note_def_sm00("A5", 0.25)
note_def_sm00("F5", 0.25)
note_def_sm00("E5", 0.25)
note_def_sm00("D5", 0.25)
note_def_sm00("C5", 0.75)

# s24
note_def_sm00("D4", 8)

#---------------------------------------------------------------

# 1
note_def_sm01("D4", 0.5)
note_def_sm01("D4", 0.5)
note_def_sm01("F4", 0.5)
note_def_sm01("G4", 0.25)
note_def_sm01("A-4", 0.25)
note_def_sm01("A4", 0.5)
note_def_sm01("A4", 0.5)
note_def_sm01("A4", 0.25)
note_def_sm01("G4", 0.25)
note_def_sm01("F4", 0.5)

# 2
note_def_sm01("D4", 0.5)
note_def_sm01("D4", 0.5)
note_def_sm01("D4", 0.5)
note_def_sm01("C4", 0.25)
note_def_sm01("A-3", 0.25)
note_def_sm01("A3", 0.25)
note_def_sm01("C4", 0.25)
note_def_sm01("A3", 0.5)
note_def_sm01("C4", 0.5)
note_def_sm01("D-4", 0.5)

# 3
note_def_sm01("D4", 0.5)
note_def_sm01("D4", 0.5)
note_def_sm01("F4", 0.5)
note_def_sm01("G4", 0.25)
note_def_sm01("A-4", 0.25)
note_def_sm01("A4", 0.5)
note_def_sm01("A4", 0.5)
note_def_sm01("A4", 0.25)
note_def_sm01("G4", 0.25)
note_def_sm01("A4", 0.5)

# 4
note_def_sm01("C5", 0.5)
note_def_sm01("C5", 0.5)
note_def_sm01("C5", 0.25)
note_def_sm01("A4", 0.25)
note_def_sm01("G4", 0.5)
note_def_sm01("A4", 0.5)
note_def_sm01("A4", 0.5)
note_def_sm01("A4", 0.5)
rest_def_sm01(0.5)

for repeat in range(2):
    # 5
    note_def_sm01("D4", 0.5)
    note_def_sm01("D4", 0.5)
    note_def_sm01("F4", 0.5)
    note_def_sm01("G4", 0.25)
    note_def_sm01("A-4", 0.25)
    note_def_sm01("A4", 0.5)
    note_def_sm01("A4", 0.5)
    note_def_sm01("A4", 0.25)
    note_def_sm01("G4", 0.25)
    note_def_sm01("F4", 0.5)

    # 6
    note_def_sm01("D4", 0.5)
    note_def_sm01("D4", 0.5)
    note_def_sm01("D4", 0.5)
    note_def_sm01("C4", 0.25)
    note_def_sm01("A-3", 0.25)
    note_def_sm01("A3", 0.25)
    note_def_sm01("C4", 0.25)
    note_def_sm01("A3", 0.5)
    note_def_sm01("C4", 0.5)
    note_def_sm01("D-4", 0.5)

    # 7
    note_def_sm01("D4", 0.5)
    note_def_sm01("D4", 0.5)
    note_def_sm01("F4", 0.5)
    note_def_sm01("G4", 0.25)
    note_def_sm01("A-4", 0.25)
    note_def_sm01("A4", 0.5)
    note_def_sm01("A4", 0.5)
    note_def_sm01("A4", 0.25)
    note_def_sm01("G4", 0.25)
    note_def_sm01("A4", 0.5)

    # 8
    note_def_sm01("C5", 0.5)
    note_def_sm01("C5", 0.5)
    note_def_sm01("C5", 0.25)
    note_def_sm01("A4", 0.25)
    note_def_sm01("G4", 0.5)
    note_def_sm01("A4", 0.5)
    note_def_sm01("A4", 0.5)
    note_def_sm01("A4", 1)

    # 9
    note_def_sm01("D4", 0.5)
    note_def_sm01("D4", 0.5)
    note_def_sm01("F4", 0.5)
    note_def_sm01("G4", 0.25)
    note_def_sm01("A-4", 0.25)
    note_def_sm01("A4", 0.5)
    note_def_sm01("A4", 0.5)
    note_def_sm01("A4", 0.25)
    note_def_sm01("G4", 0.25)
    note_def_sm01("F4", 0.5)

    if repeat == 1:
        break
    # 10
    note_def_sm01("D4", 0.5)
    note_def_sm01("D4", 0.5)
    note_def_sm01("D4", 0.5)
    note_def_sm01("C4", 0.25)
    note_def_sm01("A-3", 0.25)
    note_def_sm01("A3", 0.25)
    note_def_sm01("C4", 0.25)
    note_def_sm01("A3", 0.5)
    note_def_sm01("C4", 0.5)
    note_def_sm01("D-4", 0.5)

    # 11
    note_def_sm01("D4", 0.5)
    note_def_sm01("D4", 0.5)
    note_def_sm01("F4", 0.5)
    note_def_sm01("E4", 0.25)
    note_def_sm01("D4", 0.25)
    note_def_sm01("C4", 0.5)
    note_def_sm01("C4", 0.5)
    note_def_sm01("C4", 1)

    # 12
    rest_def_sm01(0.25)
    note_def_sm01("C5", 0.75)
    note_def_sm01("C5", 0.5)
    note_def_sm01("A4", 0.25)
    note_def_sm01("G4", 0.25)
    note_def_sm01("A-4", 0.25)
    note_def_sm01("A4", 0.25)
    note_def_sm01("F4", 0.25)
    note_def_sm01("E4", 0.25)
    note_def_sm01("D4", 0.5)
    note_def_sm01("C4", 0.5)
    
# 13
note_def_sm01("D4", 0.5)
note_def_sm01("D4", 0.5)
note_def_sm01("D4", 0.5)
note_def_sm01("C4", 0.25)
note_def_sm01("A-3", 0.25)
note_def_sm01("A3", 0.25)
note_def_sm01("C4", 0.25)
note_def_sm01("A3", 0.5)
note_def_sm01("C4", 0.5)
note_def_sm01("E4", 0.5)

# 14
note_def_sm01("D4", 0.5)
note_def_sm01("D4", 0.5)
note_def_sm01("D4", 0.5)
note_def_sm01("E4", 0.25)
note_def_sm01("F4", 0.25)
note_def_sm01("G4", 0.5)
note_def_sm01("G4", 0.5)
note_def_sm01("G4", 0.25)
note_def_sm01("E4", 0.25)
note_def_sm01("C4", 0.5)

# 15
note_def_sm01("D4", 0.5)
note_def_sm01("D4", 0.5)
note_def_sm01("D4", 0.25)
note_def_sm01("E4", 0.25)
note_def_sm01("F4", 0.25)
note_def_sm01("A4", 0.25)
note_def_sm01("C5", 0.25)
note_def_sm01("A4", 0.25)
note_def_sm01("C5", 0.25)
note_def_sm01("D-5", 0.25)
note_def_sm01("A4", 0.5)
note_def_sm01("C5", 0.5)

# 16
note_def_sm01("D5", 1.5)
note_def_sm01("C5", 0.25)
note_def_sm01("D5", 0.25)
note_def_sm01("F5", 0.5)
note_def_sm01("E5", 0.5)
note_def_sm01("D5", 0.5)
note_def_sm01("C5", 0.5)

# 17
note_def_sm01("C5", 1.5)
note_def_sm01("B-4", 0.25)
note_def_sm01("C5", 0.25)
note_def_sm01("A4", 1)
note_def_sm01("A4", 0.5)
note_def_sm01("C5", 0.5)

# 18
note_def_sm01("D5", 1.5)
note_def_sm01("C5", 0.25)
note_def_sm01("D5", 0.25)
note_def_sm01("A5", 0.5)
note_def_sm01("G5", 0.5)
note_def_sm01("F5", 0.5)
note_def_sm01("E5", 0.5)

# 19
note_def_sm01("E5", 0.75)
note_def_sm01("F5", 0.75)
note_def_sm01("B5", 0.125)
note_def_sm01("C6", 0.375)
note_def_sm01("A5", 1)
note_def_sm01("A4", 0.5)
note_def_sm01("C5", 0.5)

# 20
note_def_sm01("D5", 1.5)
note_def_sm01("C5", 0.25)
note_def_sm01("D5", 0.25)
note_def_sm01("F5", 0.5)
note_def_sm01("E5", 0.5)
note_def_sm01("D5", 0.5)
note_def_sm01("C5", 0.5)

# 21
note_def_sm01("C5", 1.5)
note_def_sm01("B-4", 0.25)
note_def_sm01("C5", 0.25)
note_def_sm01("A4", 1)
note_def_sm01("A4", 0.5)
note_def_sm01("C5", 0.5)

# 22
note_def_sm01("D5", 1.5)
note_def_sm01("C5", 0.25)
note_def_sm01("D5", 0.25)
note_def_sm01("F5", 0.5)
note_def_sm01("E5", 0.5)
note_def_sm01("D5", 0.5)
note_def_sm01("C5", 0.5)

# 23
note_def_sm01("D5", 2)
rest_def_sm01(2)

# 24
note_def_sm01("A3", 8)

#---------------------------------------------------------------

# b1
note_def_sm02("D2", 0.75)
note_def_sm02("D3", 0.25)
note_def_sm02("C3", 0.25)
note_def_sm02("D3", 0.25)
note_def_sm02("D2", 0.5)
note_def_sm02("C2", 0.5)
note_def_sm02("C3", 0.5)
note_def_sm02("C2", 0.5)
note_def_sm02("C3", 0.5)

# b2
note_def_sm02("B-1", 0.75)
note_def_sm02("A2", 0.25)
note_def_sm02("B-2", 0.5)
note_def_sm02("G2", 0.25)
note_def_sm02("B-2", 0.25)
note_def_sm02("C3", 0.25)
note_def_sm02("C2", 0.25)
note_def_sm02("C2", 0.5)
note_def_sm02("F2", 0.5)
note_def_sm02("E2", 0.5)

# b3
note_def_sm02("D2", 0.75)
note_def_sm02("D3", 0.25)
note_def_sm02("C3", 0.25)
note_def_sm02("D3", 0.25)
note_def_sm02("D2", 0.5)
note_def_sm02("C2", 0.5)
note_def_sm02("C3", 0.5)
note_def_sm02("C2", 0.5)
note_def_sm02("C3", 0.5)

# b4
note_def_sm02("B-1", 0.75)
note_def_sm02("A2", 0.25)
note_def_sm02("B-2", 0.5)
note_def_sm02("G2", 0.25)
note_def_sm02("B-2", 0.25)
note_def_sm02("G2", 0.25)
note_def_sm02("A2", 0.25)
note_def_sm02("F2", 0.25)
note_def_sm02("C2", 0.25)
note_def_sm02("A1", 0.5)
note_def_sm02("E2", 0.5)

for repeat in range(2):
    # b5
    note_def_sm02("D2", 0.75)
    note_def_sm02("D3", 0.25)
    note_def_sm02("C3", 0.25)
    note_def_sm02("D3", 0.25)
    note_def_sm02("D2", 0.5)
    note_def_sm02("C2", 0.5)
    note_def_sm02("C3", 0.5)
    note_def_sm02("C2", 0.5)
    note_def_sm02("C3", 0.5)

    # b6
    note_def_sm02("B-1", 0.75)
    note_def_sm02("A2", 0.25)
    note_def_sm02("B-2", 0.5)
    note_def_sm02("G2", 0.25)
    note_def_sm02("B-2", 0.25)
    note_def_sm02("C3", 0.25)
    note_def_sm02("C2", 0.25)
    note_def_sm02("C2", 0.5)
    note_def_sm02("F2", 0.5)
    note_def_sm02("E2", 0.5)

    # b7
    note_def_sm02("D2", 0.75)
    note_def_sm02("D3", 0.25)
    note_def_sm02("C3", 0.25)
    note_def_sm02("D3", 0.25)
    note_def_sm02("D2", 0.5)
    note_def_sm02("C2", 0.5)
    note_def_sm02("C3", 0.5)
    note_def_sm02("C2", 0.5)
    note_def_sm02("C3", 0.5)

    # b8
    note_def_sm02("B-1", 0.75)
    note_def_sm02("A2", 0.25)
    note_def_sm02("B-2", 0.5)
    note_def_sm02("F2", 0.25)
    note_def_sm02("G2", 0.25)
    note_def_sm02("A2", 0.25)
    note_def_sm02("G2", 0.25)
    note_def_sm02("E2", 0.5)
    note_def_sm02("A1", 0.5)
    note_def_sm02("C2", 0.5)

    # b9
    note_def_sm02("D2", 0.75)
    note_def_sm02("D3", 0.25)
    note_def_sm02("C3", 0.25)
    note_def_sm02("D3", 0.25)
    note_def_sm02("D2", 0.5)
    note_def_sm02("C2", 0.5)
    note_def_sm02("C3", 0.5)
    note_def_sm02("C2", 0.5)
    note_def_sm02("C3", 0.5)

    if repeat == 1:
        break
    # b10
    note_def_sm02("B-1", 0.75)
    note_def_sm02("A2", 0.25)
    note_def_sm02("B-2", 0.5)
    note_def_sm02("G2", 0.25)
    note_def_sm02("B-2", 0.25)
    note_def_sm02("C3", 0.25)
    note_def_sm02("C2", 0.25)
    note_def_sm02("C2", 0.5)
    note_def_sm02("F2", 0.5)
    note_def_sm02("E2", 0.5)

    # b11
    note_def_sm02("G1", 0.75)
    note_def_sm02("G1", 0.25)
    note_def_sm02("F2", 0.25)
    note_def_sm02("G-2", 0.25)
    note_def_sm02("G2", 0.5)
    note_def_sm02("A2", 0.25)
    note_def_sm02("A2", 0.25)
    note_def_sm02("A1", 0.5)
    note_def_sm02("C2", 0.5)
    note_def_sm02("A1", 0.5)

    # b12
    note_def_sm02("D2", 0.75)
    note_def_sm02("D2", 0.25)
    note_def_sm02("G2", 0.5)
    note_def_sm02("A2", 0.25)
    note_def_sm02("C3", 0.25)
    note_def_sm02("D3", 0.25)
    note_def_sm02("D3", 0.25)
    note_def_sm02("C3", 0.25)
    note_def_sm02("A2", 0.25)
    note_def_sm02("G2", 0.25)
    note_def_sm02("F2", 0.25)
    note_def_sm02("A1", 0.5)
    
# b13
note_def_sm02("B-1", 0.75)
note_def_sm02("A2", 0.25)
note_def_sm02("B-2", 0.5)
note_def_sm02("G2", 0.25)
note_def_sm02("B-2", 0.25)
note_def_sm02("C3", 0.25)
note_def_sm02("C2", 0.25)
note_def_sm02("C2", 0.5)
note_def_sm02("F2", 0.5)
note_def_sm02("E2", 0.5)

# b14
note_def_sm02("G1", 0.75)
note_def_sm02("G1", 0.25)
note_def_sm02("E2", 0.25)
note_def_sm02("F2", 0.25)
note_def_sm02("G2", 0.5)
note_def_sm02("A2", 0.25)
note_def_sm02("A2", 0.25)
note_def_sm02("A1", 0.5)
note_def_sm02("E2", 0.5)
note_def_sm02("A1", 0.5)

# b15
note_def_sm02("D2", 0.75)
note_def_sm02("D2", 0.25)
note_def_sm02("A2", 0.5)
note_def_sm02("C3", 0.25)
note_def_sm02("D-3", 0.25)
note_def_sm02("D3", 0.25)
note_def_sm02("D3", 0.25)
note_def_sm02("C3", 0.25)
note_def_sm02("A2", 0.25)
note_def_sm02("G2", 0.5)
note_def_sm02("A1", 0.5)

# b16
note_def_sm02("B-1", 0.25)
note_def_sm02("B-2", 0.5)
note_def_sm02("B-2", 0.75)
note_def_sm02("B-1", 0.25)
note_def_sm02("B-1", 0.25)
rest_def_sm02(0.25)
note_def_sm02("B-2", 0.25)
note_def_sm02("B-1", 0.5)
note_def_sm02("F2", 0.5)
note_def_sm02("B-1", 0.5)

# b17
note_def_sm02("A1", 0.25)
note_def_sm02("A2", 0.5)
note_def_sm02("A2", 0.75)
note_def_sm02("A1", 0.25)
note_def_sm02("A1", 0.25)
rest_def_sm02(0.25)
note_def_sm02("A2", 0.25)
note_def_sm02("A1", 0.5)
note_def_sm02("E2", 0.5)
note_def_sm02("A1", 0.5)

# b18
note_def_sm02("G1", 0.25)
note_def_sm02("G2", 0.5)
note_def_sm02("G2", 0.75)
note_def_sm02("G1", 0.25)
note_def_sm02("G1", 0.25)
rest_def_sm02(0.25)
note_def_sm02("D2", 0.25)
note_def_sm02("B-1", 0.25)
note_def_sm02("C2", 0.25)
note_def_sm02("D2", 0.5)
note_def_sm02("G2", 0.5)

# b19
note_def_sm02("A1", 0.25)
note_def_sm02("A2", 0.5)
note_def_sm02("A1", 0.25)
note_def_sm02("A2", 0.5)
note_def_sm02("A1", 0.25)
note_def_sm02("G2", 0.25)
note_def_sm02("A2", 0.5)
note_def_sm02("F2", 0.25)
note_def_sm02("G2", 0.25)
note_def_sm02("E2", 0.25)
note_def_sm02("F2", 0.25)
note_def_sm02("A1", 0.5)

# b20
note_def_sm02("B-1", 0.25)
note_def_sm02("B-2", 0.5)
note_def_sm02("B-2", 0.75)
note_def_sm02("B-1", 0.25)
note_def_sm02("B-1", 0.25)
rest_def_sm02(0.25)
note_def_sm02("B-2", 0.25)
note_def_sm02("B-1", 0.5)
note_def_sm02("F2", 0.5)
note_def_sm02("B-1", 0.5)

# b21
note_def_sm02("A1", 0.25)
note_def_sm02("A2", 0.5)
note_def_sm02("A2", 0.75)
note_def_sm02("A1", 0.25)
note_def_sm02("A1", 0.25)
rest_def_sm02(0.25)
note_def_sm02("A2", 0.25)
note_def_sm02("A1", 0.5)
note_def_sm02("E2", 0.5)
note_def_sm02("A1", 0.5)

# b22
note_def_sm02("B-1", 0.25)
note_def_sm02("B-2", 0.5)
note_def_sm02("B-2", 0.75)
note_def_sm02("B-1", 0.25)
note_def_sm02("C2", 0.25)
rest_def_sm02(0.25)
note_def_sm02("C3", 0.25)
note_def_sm02("C2", 0.25)
note_def_sm02("C2", 0.25)
note_def_sm02("G2", 0.5)
note_def_sm02("E2", 0.5)

# b23
note_def_sm02("D2", 0.75)
note_def_sm02("D2", 0.5)
note_def_sm02("F2", 0.25)
note_def_sm02("A-2", 0.25)
note_def_sm02("A2", 0.25)
note_def_sm02("C3", 0.25)
note_def_sm02("D3", 0.25)
note_def_sm02("A2", 0.25)
note_def_sm02("G2", 0.25)
note_def_sm02("F2", 0.25)
note_def_sm02("D2", 0.25)
note_def_sm02("C2", 0.5)

# b24
note_def_sm02("D2", 8)

#---------------------------------------------------------------
p0.append(sm00)
p1.append(sm01)
p2.append(sm02)
s.insert(0, p0)
s.insert(0, p1)
s.insert(0, p2)

s.show("midi")
s.show("text")

s.write("midi", fp="Drunk.midi")
s.write("xml", fp="Drunk.xml")