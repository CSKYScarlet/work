from music21 import note, stream
from music21 import *

s = stream.Score(id='mainScore')
s.append(tempo.MetronomeMark(number=156))
p0 = stream.Part(id='part0')
p1 = stream.Part(id='part1')

sm01 = stream.Measure()
tsThreeFour = meter.TimeSignature('3/4')
sm01.insert(0, tsThreeFour)
sm01.insert(0, key.KeySignature(3))
sm01.insert(0, clef.TrebleClef())

sm02 = stream.Measure()
tsThreeFour = meter.TimeSignature('3/4')
sm02.insert(0, tsThreeFour)
sm02.insert(0, key.KeySignature(3))
sm02.insert(0, clef.BassClef())

def note_def_sm01(note_value, quarter):
    sm01.append(chord.Chord(note_value, quarterLength = quarter))
def rest_def_sm01(quarter):
    sm01.append(note.Rest(quarterLength = quarter))
    
def note_def_sm02(note_value, quarter):
    sm02.append(chord.Chord(note_value, quarterLength = quarter))
def rest_def_sm02(quarter):
    sm02.append(note.Rest(quarterLength = quarter))

#----------------------------------------------
for repeat in range(2): # repeat
    for subrepeat in range(2):
        # 1
        note_def_sm01("C#4", 0.5)
        note_def_sm01("F#4", 0.5)
        note_def_sm01("A4", 0.5)
        note_def_sm01("G#4", 0.5)
        note_def_sm01("A4", 0.5)
        note_def_sm01("C#5", 0.5)

        # 2
        note_def_sm01("C#4", 0.5)
        note_def_sm01("F#4", 0.5)
        note_def_sm01("A4", 0.5)
        note_def_sm01("C#4", 0.5)
        note_def_sm01("G#4", 0.5)
        note_def_sm01("B4", 0.5)
    # to 4

# 5
note_def_sm01("F#4", 2)
note_def_sm01("F#4", 0.5)
note_def_sm01("G#4", 0.5)

# 6
note_def_sm01("A4", 1)
note_def_sm01("A4", 0.5)
note_def_sm01("B4", 0.5)
note_def_sm01("C#5", 1)

# 7
note_def_sm01("B4", 1.5)
note_def_sm01("C#5", 0.5)
note_def_sm01("A4", 1)

# 8
note_def_sm01("G#4", 1.5)
note_def_sm01("A4", 0.5)
note_def_sm01("G#4", 1)

# 9
note_def_sm01("F#4", 2)
note_def_sm01("F#4", 0.5)
note_def_sm01("G#4", 0.5)

# 10
note_def_sm01("A4", 1)
note_def_sm01("C#5", 1)
note_def_sm01("E5", 1)

# 11
note_def_sm01("F#5", 1.5)
note_def_sm01("G#5", 0.5)
note_def_sm01("E5", 1)

# 12
note_def_sm01("D#5", 1.5)
note_def_sm01("E5", 0.5)
note_def_sm01("D#5", 1)

# 13
note_def_sm01("C#5", 3)

# 14
rest_def_sm01(1)
note_def_sm01("C#5", 1)
note_def_sm01("E5", 1)

# 15
note_def_sm01("F#5", 1.5)
note_def_sm01("G#5", 0.5)
note_def_sm01("E5", 1)

# 16
note_def_sm01("D#5", 1.5)
note_def_sm01("C#5", 0.5)
note_def_sm01("B4", 1)

# 17
note_def_sm01("C#5", 1.5)
note_def_sm01("F#4", 0.5)
note_def_sm01("C#5", 1)

# 18
note_def_sm01("B4", 1)
note_def_sm01("A4", 1)
note_def_sm01("G#4", 1)

# 19
note_def_sm01("F#4", 2)
note_def_sm01("A4", 0.5)
note_def_sm01("C#5", 0.5)

# 20
note_def_sm01("B4", 2)
note_def_sm01("B4", 1)

# 21
note_def_sm01("A#4", 1.5)
note_def_sm01("G#4", 0.5)
note_def_sm01("A#4", 1)

# 22
note_def_sm01("F#4", 3)

# 23
note_def_sm01(["A3", "F#4"], 2)
note_def_sm01(["A3", "F#4"], 0.5)
note_def_sm01(["B3", "G#4"], 0.5)

# 24
note_def_sm01(["C#4", "A4"], 1)
note_def_sm01(["F#4", "A4"], 0.5)
note_def_sm01(["G#4", "B4"], 0.5)
note_def_sm01(["A4", "C#5"], 1)

# 25
note_def_sm01(["G#4", "B4"], 1.5)
note_def_sm01(["A4", "C#5"], 0.5)
note_def_sm01(["F#4", "A4"], 1)

# 26
note_def_sm01(["E4", "G#4"], 1.5)
note_def_sm01(["F#4", "A4"], 0.5)
note_def_sm01(["E4", "G#4"], 1)

# 27
note_def_sm01(["A3", "F#4"], 2)
note_def_sm01(["A3", "F#4"], 0.5)
note_def_sm01(["B3", "G#4"], 0.5)

# 28
note_def_sm01(["C#4", "A4"], 1)
note_def_sm01(["A4", "C#5"], 1)
note_def_sm01(["C#5", "E5"], 1)

# 29
note_def_sm01(["D5", "F#5"], 1.5)
note_def_sm01(["E5", "G#5"], 0.5)
note_def_sm01(["C#5", "E5"], 1)

# 30
note_def_sm01(["B4", "D#5"], 1.5)
note_def_sm01(["C#5", "E5"], 0.5)
note_def_sm01(["B4", "D#5"], 1)

# 31
note_def_sm01(["G#4", "C#5"], 3)

# 32
rest_def_sm01(1)
note_def_sm01(["G#4", "C#5"], 1)
note_def_sm01(["C#5", "E5"], 1)

# 33
note_def_sm01(["C#5", "F#5"], 1.5)
note_def_sm01(["E5", "G#5"], 0.5)
note_def_sm01(["C#5", "E5"], 1)

# 34
note_def_sm01(["B4", "D#5"], 1.5)
note_def_sm01(["G#4", "C#5"], 0.5)
note_def_sm01(["F#4", "B4"], 1)

# 35
note_def_sm01(["A4", "C#5"], 1.5)
note_def_sm01(["C#4", "F#4"], 0.5)
note_def_sm01(["A4", "C#5"], 1)

# 36
note_def_sm01(["F4", "B4"], 1)
note_def_sm01(["C#4", "A4"], 1)
note_def_sm01(["B3", "G#4"], 1)

# 37
note_def_sm01(["A3", "F#4"], 2)
note_def_sm01(["C#4", "A4"], 0.5)
note_def_sm01(["F#4", "C#5"], 0.5)

# 38
note_def_sm01(["G#4", "B4"], 1)
note_def_sm01(["F#4", "A4"], 1)
note_def_sm01(["E4", "G#4"], 1)

# 39
note_def_sm01(["A3", "F#4"], 5)

# 40
note_def_sm01("F#4", 0.5)
note_def_sm01("G#4", 0.5)

# natural to 52
for repeat in range(2):
    if repeat == 1 and subrepeat == 2:
            break
    for subrepeat in range(4): # to 48
        if repeat == 1 and subrepeat == 2:
            break # repeat 44 end
        # 41 # 43 # 45 # 47
        note_def_sm01("E4", 0.5)
        note_def_sm01("A4", 0.5)
        note_def_sm01("C5", 0.5)
        note_def_sm01("B4", 0.5)
        note_def_sm01("C5", 0.5)
        note_def_sm01("E5", 0.5)

        # 42 # 44 # 46 # 48
        note_def_sm01("E4", 0.5)
        note_def_sm01("A4", 0.5)
        note_def_sm01("C5", 0.5)
        note_def_sm01("E4", 0.5)
        note_def_sm01("B4", 0.5)
        note_def_sm01("D5", 0.5)

for repeat in range(2):
    # 49 # 51
    note_def_sm01("E4", 0.5)
    note_def_sm01("G#4", 0.5)
    note_def_sm01("C5", 0.5)
    note_def_sm01("B4", 0.5)
    note_def_sm01("C5", 0.5)
    note_def_sm01("E5", 0.5)

    # 50 # 52
    note_def_sm01("E4", 0.5)
    note_def_sm01("G#4", 0.5)
    note_def_sm01("C5", 0.5)
    note_def_sm01("E4", 0.5)
    note_def_sm01("B4", 0.5)
    note_def_sm01("D5", 0.5)

sm01.append(key.KeySignature(-5))
for repeat in range(2):
    # 53
    note_def_sm01(["F4", "B-4"], 2)
    note_def_sm01(["F4", "B-4"], 0.5)
    note_def_sm01(["E-4", "C5"], 0.5)

    # 54
    note_def_sm01(["F4", "D-5"], 1)
    note_def_sm01(["B-4", "D-5"], 0.5)
    note_def_sm01(["C5", "E-5"], 0.5)
    note_def_sm01(["D-5", "F5"], 1)

    # 55
    note_def_sm01(["C5", "E-5"], 1.5)
    note_def_sm01(["D-5", "F5"], 0.5)
    note_def_sm01(["B-4", "D-5"], 1)

    # 56
    note_def_sm01(["A-4", "C5"], 1.5)
    note_def_sm01(["B-4", "D-5"], 0.5)
    note_def_sm01(["A-4", "C5"], 1)

    # 57
    note_def_sm01(["F4", "B-4"], 2)
    note_def_sm01(["F4", "B-4"], 0.5)
    note_def_sm01(["E-4", "C5"], 0.5)

    # 58
    note_def_sm01(["F4", "D-5"], 1)
    note_def_sm01(["D-5", "F5"], 1)
    note_def_sm01(["E-5", "A-5"], 1)

    # 59
    note_def_sm01(["F5", "B-5"], 1.5)
    note_def_sm01(["A-5", "C6"], 0.5)
    note_def_sm01(["F5", "A-5"], 1)

    # 60
    note_def_sm01(["E-5", "G5"], 1.5)
    note_def_sm01(["F5", "A-5"], 0.5)
    note_def_sm01(["E-5", "G5"], 1)

    # 61
    note_def_sm01(["C5", "F5"], 3)

    # 62
    rest_def_sm01(1)
    note_def_sm01(["C5", "F5"], 1)
    note_def_sm01(["F5", "A-5"], 1)

    # 63
    note_def_sm01(["F5", "B-5"], 1.5)
    note_def_sm01(["A-5", "C6"], 0.5)
    note_def_sm01(["F5", "A-5"], 1)

    # 64
    note_def_sm01(["E-5", "G5"], 1.5)
    note_def_sm01(["C5", "F5"], 0.5)
    note_def_sm01(["B-4", "E-5"], 1)

    # 65
    note_def_sm01(["D-5", "F5"], 1.5)
    note_def_sm01(["F4", "B-4"], 0.5)
    note_def_sm01(["D-5", "F5"], 1)

    # 66
    note_def_sm01(["A4", "E-5"], 1)
    note_def_sm01(["F4", "D-5"], 1)
    note_def_sm01(["E-4", "C5"], 1)

    # 67
    note_def_sm01(["D-4", "B-4"], 2)
    note_def_sm01(["B-4", "D-5"], 0.5)
    note_def_sm01(["D-5", "F5"], 0.5)

    if repeat == 1:
        break
    # 68
    note_def_sm01(["C5", "E-5"], 2)
    note_def_sm01(["C5", "E-5"], 1)

    # 69
    note_def_sm01(["B-4", "D5"], 1.5)
    note_def_sm01(["A-4", "C5"], 0.5)
    note_def_sm01(["B-4", "D5"], 1)

    # 70
    note_def_sm01(["F4", "B-4"], 3)
    
# 71
note_def_sm01(["C5", "E-5"], 1)
note_def_sm01(["B-4", "D-5"], 1)
note_def_sm01(["E-4", "C5"], 1)

# 72
note_def_sm01(["D-4", "B-4"], 5)

# 73
note_def_sm01("D4", 0.5)
note_def_sm01("F4", 0.5)

sm01.append(key.KeySignature(-2))
# 74
note_def_sm01("G4", 2)
note_def_sm01("G4", 0.5)
note_def_sm01("A4", 0.5)

# 75
note_def_sm01("B-4", 1)
note_def_sm01("B-4", 0.5)
note_def_sm01("C5", 0.5)
note_def_sm01("D5", 1)

# 76
note_def_sm01("C5", 1.5)
note_def_sm01("D5", 0.5)
note_def_sm01("B-4", 1)

# 77
note_def_sm01("A4", 1.5)
note_def_sm01("B-4", 0.5)
note_def_sm01("A4", 1)

# 78
note_def_sm01("G4", 2)
note_def_sm01("G4", 0.5)
note_def_sm01("A4", 0.5)

# 79
note_def_sm01("B-4", 1)
note_def_sm01("D5", 1)
note_def_sm01("F5", 1)

# 80
note_def_sm01("G5", 1.5)
note_def_sm01("A5", 0.5)
note_def_sm01("F5", 1)

# 81
note_def_sm01("E5", 1.5)
note_def_sm01("F5", 0.5)
note_def_sm01("E5", 1)

# 82
note_def_sm01("D5", 3)

# 83
rest_def_sm01(1)
note_def_sm01("D5", 1)
note_def_sm01("F5", 1)

# 84
note_def_sm01("G5", 1.5)
note_def_sm01("A5", 0.5)
note_def_sm01("F5", 1)

# 85
note_def_sm01("E5", 1.5)
note_def_sm01("D5", 0.5)
note_def_sm01("C5", 1)

# 86
note_def_sm01("D5", 1.5)
note_def_sm01("G4", 0.5)
note_def_sm01("D5", 1)

# 87
note_def_sm01("C5", 1)
note_def_sm01("B-4", 1)
note_def_sm01("A4", 1)

# 88
note_def_sm01("G4", 2)
note_def_sm01("B-4", 0.5)
note_def_sm01("D5", 0.5)

# 89
note_def_sm01("C5", 2)
note_def_sm01("C5", 1)

# 90
note_def_sm01("B4", 1.5)
note_def_sm01("A4", 0.5)
note_def_sm01("B4", 1)

# 91
note_def_sm01("G4", 3)

# 92
note_def_sm01(["D4", "G4"], 2)
note_def_sm01(["D4", "G4"], 0.5)
note_def_sm01(["C4", "A4"], 0.5)

# 93
note_def_sm01(["D4", "B-4"], 1)
note_def_sm01(["G4", "B-4"], 0.5)
note_def_sm01(["A4", "C5"], 0.5)
note_def_sm01(["B-4", "D5"], 1)

# 94
note_def_sm01(["A4", "C5"], 1.5)
note_def_sm01(["B-4", "D5"], 0.5)
note_def_sm01(["G4", "B-4"], 1)

# 95
note_def_sm01(["F4", "A4"], 1.5)
note_def_sm01(["G4", "B-4"], 0.5)
note_def_sm01(["F4", "A4"], 1)

# 96
note_def_sm01(["D4", "G4"], 2)
note_def_sm01(["D4", "G4"], 0.5)
note_def_sm01(["C4", "A4"], 0.5)

# 97
note_def_sm01(["D4", "B-4"], 1)
note_def_sm01(["B-4", "D5"], 1)
note_def_sm01(["D5", "F5"], 1)

# 98
note_def_sm01(["E-5", "G5"], 1.5)
note_def_sm01(["F5", "A5"], 0.5)
note_def_sm01(["D5", "F5"], 1)

# 99
note_def_sm01(["C5", "E5"], 1.5)
note_def_sm01(["D5", "F5"], 0.5)
note_def_sm01(["C5", "E5"], 1)

# 100
note_def_sm01(["A4", "D5"], 3)

# 101
rest_def_sm01(1)
note_def_sm01(["A4", "D5"], 1)
note_def_sm01(["D5", "F5"], 1)

# 102
note_def_sm01(["D5", "G5"], 1.5)
note_def_sm01(["F5", "A5"], 0.5)
note_def_sm01(["D5", "F5"], 1)

# 103
note_def_sm01(["C5", "E5"], 1.5)
note_def_sm01(["A4", "D5"], 0.5)
note_def_sm01(["G4", "C5"], 1)

# 104
note_def_sm01(["B-4", "D5"], 1.5)
note_def_sm01(["D4", "G4"], 0.5)
note_def_sm01(["B-4", "D5"], 1)

# 105
note_def_sm01(["F#4", "C5"], 1)
note_def_sm01(["D4", "B-4"], 1)
note_def_sm01(["C4", "A4"], 1)

# 106
note_def_sm01(["B-3", "G4"], 2)
note_def_sm01(["G4", "B-4"], 0.5)
note_def_sm01(["B-4", "D5"], 0.5)

# 107
note_def_sm01(["A4", "C5"], 1)
note_def_sm01(["G4", "B-4"], 1)
note_def_sm01(["C4", "A4"], 1)

# 108
note_def_sm01(["D4", "G4"], 5)

# 109
note_def_sm01("G4", 0.5)
note_def_sm01("A4", 0.5)

# 110
note_def_sm01("B-4", 2)
note_def_sm01("B-4", 0.5)
note_def_sm01("D5", 0.5)

# 111
note_def_sm01("C5", 1)
note_def_sm01("B-4", 1)
note_def_sm01("A4", 1)

# 112
note_def_sm01("G4", 5)

# 113
note_def_sm01("G3", 0.5)
note_def_sm01("A3", 0.5)

# 114
note_def_sm01("B-3", 2)
note_def_sm01("B-3", 0.5)
note_def_sm01("D4", 0.5)

s.append(tempo.MetronomeMark(number=140))
# 115
note_def_sm01("C4", 1)
note_def_sm01("B-3", 1)
note_def_sm01("A3", 1)

# 116 to 117
note_def_sm01("G3", 5)

#------------------------------------------
for repeat in range(2):
    # s1
    note_def_sm02(["A1", "C#2"], 0.5)
    note_def_sm02(["F#2", "A2"], 2.5)

    # s2
    note_def_sm02(["A1", "C#2"], 0.5)
    note_def_sm02(["C#2", "F#2"], 2)
    note_def_sm02("F#2", 1)

    # s3
    note_def_sm02("A3", 0.5)
    note_def_sm02("C#3", 0.5)
    note_def_sm02("G#3", 0.5)
    note_def_sm02("F#3", 0.5)
    note_def_sm02("A2", 0.5)
    
    # s4
    note_def_sm02(["A1", "C#2"], 0.5)
    note_def_sm02(["F#2", "A2"], 2.5)
    
# s5
note_def_sm02(["F#3", "A3", "C#4"], 1)
note_def_sm02("F3#", 1)
note_def_sm02("F3#", 0.5)
note_def_sm02("C3#", 0.5)

# s6
for repeat in range(3):
    note_def_sm02("F3#", 1)


# s7
note_def_sm02(["D3", "F#3", "B3"], 1)
note_def_sm02("F3#", 1)
note_def_sm02("F3#", 1)

# s8
note_def_sm02(["E3", "G#3", "B3"], 1)
note_def_sm02("E3", 1)
note_def_sm02("E3", 1)

# s9
note_def_sm02(["F#3", "A3", "C#4"], 1)
note_def_sm02("F3#", 0.5)
rest_def_sm02(0.5)
note_def_sm02("F3#", 0.5)
note_def_sm02("C#3", 0.5)
    
# s10
for repeat in range(3):
    note_def_sm02("F#3", 1)
    
# s11
note_def_sm02(["A3", "C#4", "E4"], 1)
note_def_sm02("A3", 1)
note_def_sm02("A3", 1)

# s12
note_def_sm02(["B3", "D#4", "F#4"], 1)
note_def_sm02("B3", 1)
note_def_sm02("B3", 1)

# s13
note_def_sm02(["C#4", "E4", "G#4"], 1)
note_def_sm02("C#4", 1)
note_def_sm02("C#4", 1)

# s14
note_def_sm02("G#3", 1)
note_def_sm02("C#4", 1)
note_def_sm02("C#4", 1)

# s15
note_def_sm02(["F#3", "A3", "C#4"], 1)
note_def_sm02("F#3", 1)
note_def_sm02("F#3", 1)

# s16
note_def_sm02(["F#3", "B3", "D#4"], 1)
note_def_sm02("F#3", 1)
note_def_sm02("F#3", 1)

# s17
note_def_sm02(["F#3", "A3", "C#4"], 1)
note_def_sm02("F#3", 1)
note_def_sm02("F#3", 1)

# s18
note_def_sm02(["F3", "G#3", "C#4"], 1)
note_def_sm02("F3", 1)
note_def_sm02("F3", 1)

# s19
note_def_sm02(["F#3", "A3", "D4"], 1)
note_def_sm02("F#3", 1)
note_def_sm02("F#3", 1)

# s20
note_def_sm02(["E3", "G#3", "B3"], 1)
note_def_sm02("E3", 1)
note_def_sm02("E3", 1)

# s21
note_def_sm02(["F#3", "A#3", "C#4"], 1)
note_def_sm02("F#3", 1)
note_def_sm02("F#3", 1)

# s22
for repeat in range(3):
    note_def_sm02("F#3", 1)
    
# s23
note_def_sm02(["F#3", "A3", "C#4"], 1)
note_def_sm02("F#3", 1)
note_def_sm02("F#3", 0.5)
note_def_sm02("C#3", 0.5)

# s24
for repeat in range(3):
    note_def_sm02("F#3", 1)
    
# s25
note_def_sm02(["D3", "F#3", "B3"], 1)
note_def_sm02("F#3", 1)
note_def_sm02("F#3", 1)

# s26
note_def_sm02(["E3", "G#3", "B3"], 1)
note_def_sm02("E3", 1)
note_def_sm02("E3", 1)

# s27
note_def_sm02(["F#3", "A3", "C#4"], 1)
note_def_sm02("F#3", 1)
note_def_sm02("F#3", 0.5)
note_def_sm02("C#3", 0.5)

# s28
for repeat in range(3):
    note_def_sm02("F#3", 1)
    
# s29
note_def_sm02(["A3", "C#4", "E4"], 1)
note_def_sm02("A3", 1)
note_def_sm02("A3", 1)

# s30
note_def_sm02(["B3", "D#4", "F#4"], 1)
note_def_sm02("B3", 1)
note_def_sm02("B3", 1)

# s31
note_def_sm02(["C#4", "E4", "G#4"], 1)
note_def_sm02("C#4", 1)
note_def_sm02("C#4", 1)
    
# s32
note_def_sm02("G#3", 1)
note_def_sm02("C#4", 1)
note_def_sm02("C#4", 1)

# s33
note_def_sm02(["F#3", "A3", "C#4"], 1)
note_def_sm02("F#3", 1)
note_def_sm02("F#3", 1)

# s34
note_def_sm02(["F#3", "B3", "D#4"], 1)
note_def_sm02("F#3", 1)
note_def_sm02("F#3", 1)

# s35
note_def_sm02(["F#3", "A3", "C#4"], 1)
note_def_sm02("F#3", 1)
note_def_sm02("F#3", 1)

# s36
note_def_sm02(["F3", "G#3", "C#4"], 1)
note_def_sm02("F3", 1)
note_def_sm02("F3", 1)

# s37
note_def_sm02(["F#3", "A3", "D#4"], 1)
note_def_sm02("F#3", 1)
note_def_sm02("F#3", 1)

# s38
note_def_sm02(["E3", "G#3", "B3"], 1)
note_def_sm02("E3", 1)
note_def_sm02("E3", 1)

# s39
note_def_sm02(["F#3", "A3", "C#4"], 1)
note_def_sm02("F#3", 1)
note_def_sm02("F#3", 1)

# s40
for repeat in range(3):
    note_def_sm02("F#3", 1)

for baserepeat in range(2):
    # s41 to s43
    for repeat in range(3):
        note_def_sm02(["C3", "F3", "A3"], 2)
        note_def_sm02(["C3", "F3", "A3"], 1)
        
    # s44
    note_def_sm02(["C3", "F3", "A3"], 2)
    note_def_sm02(["D3", "G3", "B3"], 1)

    if baserepeat == 1:
        break
    # s45 to s47
    for repeat in range(3):
        for subrepeat in range(3):
            note_def_sm02(["E3", "A3", "C4"], 1)

    # s48
    note_def_sm02(["E3", "A3", "C4"], 2)
    note_def_sm02(["D3", "G3", "B3"], 1)
    
# s49 to s50
for repeat in range(2):
    for subrepeat in range(3):
        note_def_sm02(["E3", "G#3", "C4"], 1)
        
# s51
note_def_sm02(["E3", "G#3", "C4"], 2)
note_def_sm02(["E3", "G#3", "C4"], 1)

# s52
note_def_sm02(["E3", "G#3", "C4"], 2)
note_def_sm02(["E4", "G#4"], 1)

sm02.append(key.KeySignature(-5))
for repeat in range(2):
    # s53
    note_def_sm02(["F3", "B-3", "D-4"], 1)
    note_def_sm02("B-3", 1)
    note_def_sm02("B-3", 0.5)
    note_def_sm02("F3", 0.5)

    # s54
    note_def_sm02("B-3", 1)
    note_def_sm02("B-3", 1)
    note_def_sm02("B-3", 0.5)
    rest_def_sm02(0.5)

    # s55
    note_def_sm02(["D-3", "G-3", "B-3"], 1)
    note_def_sm02("G-3", 1)
    note_def_sm02("G-3", 1)

    # s56
    note_def_sm02(["E-3", "A-3", "C4"], 1)
    note_def_sm02("A-3", 1)
    note_def_sm02("A-3", 1)

    # s57
    note_def_sm02(["F3", "B-3", "D-4"], 1)
    note_def_sm02("B-3", 1)
    note_def_sm02("B-3", 1)

    # s58
    for subrepeat in range(3):
        note_def_sm02("B-3", 1)
        
    # s59
    note_def_sm02(["A-3", "D-4", "F4"], 1)
    note_def_sm02("D-4", 1)
    note_def_sm02("D-4", 1)

    # s60
    note_def_sm02(["B-3", "E-4", "G4"], 1)
    note_def_sm02("E-4", 1)
    note_def_sm02("E-4", 1)

    # s61
    note_def_sm02(["C4", "F4", "A4"], 1)
    note_def_sm02("F4", 1)
    note_def_sm02("F4", 1)

    # s62
    note_def_sm02("C4", 1)
    note_def_sm02("F4", 1)
    note_def_sm02("F4", 1)

    # s63
    note_def_sm02(["F3", "B-3", "D-4"], 1)
    note_def_sm02("B-3", 1)
    note_def_sm02("B-3", 1)

    # s64
    note_def_sm02(["G3", "B-3", "E-4"], 1)
    note_def_sm02("B-3", 1)
    note_def_sm02("B-3", 1)

    # s65
    note_def_sm02(["F3", "B-3", "D-4"], 1)
    note_def_sm02("B-3", 1)
    note_def_sm02("B-3", 1)

    # s66
    note_def_sm02(["F3", "A3", "C4"], 1)
    note_def_sm02("A3", 1)
    note_def_sm02("A3", 1)

    # s67
    note_def_sm02(["D-3", "F3", "B-3"], 1)
    note_def_sm02("F3", 1)
    note_def_sm02("F3", 1)

    if repeat == 1:
        break
    # s68
    note_def_sm02(["E-3", "A-3", "C4"], 1)
    note_def_sm02("A-3", 1)
    note_def_sm02("A-3", 1)

    # s69
    note_def_sm02(["F3", "B-3", "D4"], 1)
    note_def_sm02("B-3", 1)
    note_def_sm02("B-3", 1)

    # s70
    for subrepeat in range(3):
        note_def_sm02("B-3", 1)
        
# s71
note_def_sm02(["E-3", "A-3", "C4"], 1)
note_def_sm02("A-3", 1)
note_def_sm02("A-3", 1)

# s72 s73
note_def_sm02(["F3", "B-3"], 6)

sm02.append(key.KeySignature(-2))
# s74
note_def_sm02(["D3", "G3", "B-3"], 1)
note_def_sm02("G3", 1)
note_def_sm02("G3", 0.5)
note_def_sm02("D3", 0.5)

# s75
for repeat in range(3):
    note_def_sm02("G3", 1)
    
# s76
note_def_sm02(["B-2", "E-3", "G3"], 1)
note_def_sm02("E-3", 1)
note_def_sm02("E-3", 1)

# s77
note_def_sm02(["C3", "F3", "A3"], 1)
note_def_sm02("F3", 1)
note_def_sm02("F3", 1)

# s78
note_def_sm02(["D3", "G3", "B-3"], 1)
note_def_sm02("G3", 1)
note_def_sm02("G3", 0.5)
note_def_sm02("D3", 0.5)

# s79
for repeat in range(3):
    note_def_sm02("G3", 1)
    
# s80
note_def_sm02(["F3", "B-3", "D4"], 1)
note_def_sm02("B-3", 1)
note_def_sm02("B-3", 1)

# s81
note_def_sm02(["G3", "C4", "E4"], 1)
note_def_sm02("C4", 1)
note_def_sm02("C4", 1)

# s82
note_def_sm02(["A3", "D4", "F4"], 1)
note_def_sm02("D4", 1)
note_def_sm02("D4", 1)

# s83
note_def_sm02("A3", 1)
note_def_sm02("D4", 1)
note_def_sm02("D4", 1)

# s84
note_def_sm02(["D3", "G3", "B-3"], 1)
note_def_sm02("G3", 1)
note_def_sm02("G3", 1)

# s85
note_def_sm02(["E3", "G3", "C4"], 1)
note_def_sm02("G3", 1)
note_def_sm02("G3", 1)

# s86
note_def_sm02(["D3", "G3", "B-3"], 1)
note_def_sm02("G3", 1)
note_def_sm02("G3", 1)

# s87
note_def_sm02(["D3", "F#3", "A3"], 1)
note_def_sm02("F#3", 1)
note_def_sm02("F#3", 1)

# s88
note_def_sm02(["B-2", "E-3", "G3"], 1)
note_def_sm02("E-3", 1)
note_def_sm02("E-3", 1)

# s89
note_def_sm02(["C3", "F3", "A3"], 1)
note_def_sm02("F3", 1)
note_def_sm02("F3", 1)

# s90
note_def_sm02(["D3", "G3", "B3"], 1)
note_def_sm02("G3", 1)
note_def_sm02("G3", 1)

# s91
for repeat in range(3):
    note_def_sm02("G3", 1)
    
# s92
note_def_sm02(["D3", "G3", "B-3"], 1)
note_def_sm02("G3", 1)
note_def_sm02("G3", 0.5)
note_def_sm02("D3", 0.5)

# s93
for repeat in range(3):
    note_def_sm02("G3", 1)
    
# s94
note_def_sm02(["B-2", "E-3", "G3"], 1)
note_def_sm02("E-3", 1)
note_def_sm02("E-3", 1)

# s95
note_def_sm02(["C3", "F3", "A3"], 1)
note_def_sm02("F3", 1)
note_def_sm02("F3", 1)

# s96
note_def_sm02(["D3", "G3", "B-3"], 1)
note_def_sm02("G3", 1)
note_def_sm02("G3", 0.5)
note_def_sm02("D3", 0.5)

# s97
for repeat in range(3):
    note_def_sm02("G3", 1)
    
# s98
note_def_sm02(["F3", "B-3", "D4"], 1)
note_def_sm02("B-3", 1)
note_def_sm02("B-3", 1)

# s99
note_def_sm02(["G3", "C4", "E4"], 1)
note_def_sm02("C4", 1)
note_def_sm02("C4", 1)

# s100
note_def_sm02(["A3", "D4", "F4"], 1)
note_def_sm02("D4", 1)
note_def_sm02("D4", 1)

# s101
note_def_sm02("A3", 1)
note_def_sm02("D4", 1)
note_def_sm02("D4", 1)

# s102
note_def_sm02(["D3", "G3", "B-3"], 1)
note_def_sm02("G3", 1)
note_def_sm02("G3", 1)

# s103
note_def_sm02(["E3", "G3", "C4"], 1)
note_def_sm02("G3", 1)
note_def_sm02("G3", 1)

# s104
note_def_sm02(["D3", "G3", "B-3"], 1)
note_def_sm02("G3", 1)
note_def_sm02("G3", 1)

# s105
note_def_sm02(["D3", "F#3", "A3"], 1)
note_def_sm02("F#3", 1)
note_def_sm02("F#3", 1)

# s106
note_def_sm02(["B-2", "E-3", "G3"], 1)
note_def_sm02("E-3", 1)
note_def_sm02("E-3", 1)

# s107
note_def_sm02(["C3", "F3", "A3"], 1)
note_def_sm02("F3", 1)
note_def_sm02("F3", 1)

# s108 to s109
note_def_sm02(["D3", "G3", "B-3"], 6)

# s110
note_def_sm02(["E-3", "G3", "B-3", "E-3"], 3)

# s111
note_def_sm02(["F3", "A3", "C4", "F4"], 3)

# s112 to 113
note_def_sm02(["G3", "B-3", "D4", "G4"], 6)

# s114
note_def_sm02(["E-2", "G2", "B-2", "E-3"], 3)

s.append(tempo.MetronomeMark(number=140))
# s115
note_def_sm02(["F2", "A2", "C3", "F3"], 3)

# s116 to 117
note_def_sm02(["G2", "B-2", "D3", "G3"], 6)

#-----------------------------------------------

p0.append(sm01)
p1.append(sm02)
s.insert(0, p0)
s.insert(0, p1)

s.show("midi")

s.write("midi", fp="th1110.midi")
s.write("xml", fp="th1110.xml")