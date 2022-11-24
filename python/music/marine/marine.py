from music21 import note, stream
from music21 import *

s = stream.Score(id="mainScore")
s.append(tempo.MetronomeMark(number=130))
p0 = stream.Part(id="part0")

sm01 = stream.Measure()
tsFourFour = meter.TimeSignature("4/4")
sm01.insert(0, tsFourFour)
sm01.insert(0, key.KeySignature(-3))
sm01.insert(0, clef.TrebleClef())

def note_def_sm01(note_value, quarter):
    sm01.append(chord.Chord(note_value, quarterLength = quarter))
def rest_def_sm01(quarter):
    sm01.append(note.Rest(quarterLength = quarter))

#-------------------------------------------------------------------
# 1
note_def_sm01(["B-3"], 0.75)
note_def_sm01(["C4"], 0.25)
note_def_sm01(["E-4"], 0.75)
note_def_sm01(["F4"], 0.25)
note_def_sm01(["G4"], 1)
note_def_sm01(["E-4"], 1)

# 2
note_def_sm01(["C5"], 2)
note_def_sm01(["B-4"], 2)

# 3
note_def_sm01(["G4"], 1)
note_def_sm01(["F4"], 0.75)
note_def_sm01(["G4"], 0.25)
note_def_sm01(["E-4"], 1)
note_def_sm01(["C4"], 0.75)
note_def_sm01(["E-4"], 0.25)

# 4
note_def_sm01(["B-3"], 4)

# 5
note_def_sm01(["B-3"], 0.75)
note_def_sm01(["C4"], 0.25)
note_def_sm01(["E-4"], 0.75)
note_def_sm01(["F4"], 0.25)
note_def_sm01(["G4"], 1)
note_def_sm01(["E-4"], 1)

# 6
note_def_sm01(["C5"], 2)
note_def_sm01(["B-4"], 2)

# 7
note_def_sm01(["G4"], 0.75)
note_def_sm01(["G4"], 0.25)
note_def_sm01(["F4"], 0.75)
note_def_sm01(["G4"], 0.25)
note_def_sm01(["F4"], 0.75)
note_def_sm01(["E-4"], 0.25)
note_def_sm01(["C4"], 1)

# 8
note_def_sm01(["E-4"], 4)

for repeat in range(2): # to 12
    # 9
    for subrepeat in range(4):
        note_def_sm01(["B-4"], 0.75)
        note_def_sm01(["C5"], 0.25)
        
    # 10
    note_def_sm01(["B-3"], 1)
    note_def_sm01(["B-3"], 1)
    note_def_sm01(["B-3"], 2)
    
for DSrepeat in range(2):
    # 13
    note_def_sm01(["B-3"], 0.75)
    note_def_sm01(["C4"], 0.25)
    note_def_sm01(["E-4"], 0.75)
    note_def_sm01(["F4"], 0.25)
    note_def_sm01(["G4"], 1)
    note_def_sm01(["E-4"], 1)

    # 14
    note_def_sm01(["C5"], 2)
    note_def_sm01(["B-4"], 2)

    # 15
    note_def_sm01(["G4"], 1)
    note_def_sm01(["F4"], 0.75)
    note_def_sm01(["G4"], 0.25)
    note_def_sm01(["E-4"], 1)
    note_def_sm01(["C4"], 0.75)
    note_def_sm01(["E-4"], 0.25)

    # 16
    note_def_sm01(["B-3"], 4)

    # 17
    note_def_sm01(["B-3"], 0.75)
    note_def_sm01(["C4"], 0.25)
    note_def_sm01(["E-4"], 0.75)
    note_def_sm01(["F4"], 0.25)
    note_def_sm01(["G4"], 1)
    note_def_sm01(["E-4"], 1)

    # 18
    note_def_sm01(["C5"], 2)
    note_def_sm01(["B-4"], 2)

    # 19
    note_def_sm01(["G4"], 0.75)
    note_def_sm01(["G4"], 0.25)
    note_def_sm01(["F4"], 0.75)
    note_def_sm01(["G4"], 0.25)
    note_def_sm01(["F4"], 0.75)
    note_def_sm01(["E-4"], 0.25)
    note_def_sm01(["C4"], 1)

    # 20
    note_def_sm01(["E-4"], 4)

    # 21
    note_def_sm01(["G4"], 1)
    note_def_sm01(["G4"], 0.75)
    note_def_sm01(["G4"], 0.25)
    note_def_sm01(["G4"], 0.75)
    note_def_sm01(["G4"], 0.25)
    note_def_sm01(["F4"], 0.75)
    note_def_sm01(["E-4"], 0.25)

    # 22
    note_def_sm01(["G4"], 1)
    note_def_sm01(["F4"], 0.75)
    note_def_sm01(["E-4"], 0.25)
    note_def_sm01(["G4"], 0.75)
    note_def_sm01(["G4"], 1.25)

    # 23
    note_def_sm01(["C5"], 1)
    note_def_sm01(["C5"], 0.75)
    note_def_sm01(["C5"], 0.25)
    note_def_sm01(["C5"], 0.75)
    note_def_sm01(["C5"], 0.25)
    note_def_sm01(["B-4"], 0.75)
    note_def_sm01(["G4"], 0.25)

    # 24
    note_def_sm01(["C5"], 1)
    note_def_sm01(["B-4"], 0.75)
    note_def_sm01(["G4"], 0.25)
    note_def_sm01(["C5"], 0.75)
    note_def_sm01(["C5"], 1.25)

    # 25
    note_def_sm01(["C5"], 1)
    note_def_sm01(["C5"], 0.75)
    note_def_sm01(["C5"], 0.25)
    note_def_sm01(["C5"], 1)
    note_def_sm01(["B-4"], 0.75)
    note_def_sm01(["G4"], 0.25)

    # 26
    note_def_sm01(["C5"], 4)

    # 27
    note_def_sm01(["E-5"], 1)
    note_def_sm01(["D5"], 1)
    note_def_sm01(["C5"], 1)
    note_def_sm01(["B-4"], 0.75)
    note_def_sm01(["G4"], 0.25)

    # 28
    note_def_sm01(["C5"], 4)

    for repeat in range(2): # to 30
        # 29
        note_def_sm01(["C5"], 1)
        note_def_sm01(["B-4"], 0.75)
        note_def_sm01(["G4"], 0.25)
        note_def_sm01(["C5"], 0.75)
        note_def_sm01(["C5"], 1.25)
        
    # 31
    for repeat in range(3):
        note_def_sm01(["C5"], 1 / 3)
    for repeat in range(3):
        note_def_sm01(["B-4"], 1 / 3)
    for repeat in range(3):
        note_def_sm01(["G4"], 1 / 3)
    for repeat in range(3):
        note_def_sm01(["F4"], 1 / 3)
        
    # 32
    for repeat in range(2):
        note_def_sm01(["E-4"], 1)
        note_def_sm01(["C4"], 0.75)
        note_def_sm01(["B-3"], 0.25)
        note_def_sm01(["E-4"], 0.75)
        note_def_sm01(["E-4"], 1.25)
    
# 33
for subrepeat in range(2):
    note_def_sm01(["C5"], 1 / 3)
    note_def_sm01(["C5"], 1 / 3)
    note_def_sm01(["C5"], (1 / 3) + 1)
    
# 34
note_def_sm01(["C5"], 2)
note_def_sm01(["D5"], 2)

# 35
note_def_sm01(["E-5"], 4)

#-------------------------------------------------------------------

p0.append(sm01)
s.insert(0, p0)

s.show("midi")

s.write("midi", fp="marine.midi")
s.write("xml", fp="marine.xml")
# 1q2w3e4r