from winsound import Beep
import time

def sound (octave, syllable):
    if syllable == "C" : # 도
        return int(523 * 2 ** octave)
    elif syllable == "C#" or syllable == "Db" : # 도# or 레b
        return int(554 * 2 ** octave)
    
    elif syllable == "D" : # 레
        return int(587 * 2 ** octave)
    elif syllable == "D#" or syllable == "Eb" : # 레# or 미b
        return int(622 * 2 ** octave)
    
    elif syllable == "E" or syllable == "Fb" : # 미 or 파b
        return int(659 * 2 ** octave)
    
    elif syllable == "F" : # 파
        return 698 * 2 ** octave
    elif syllable == "F#" or syllable == "Gb" : # 파# or 솔b
        return int(740 * 2 ** octave)
    
    elif syllable == "G" : # 솔
        return int(784 * 2 ** octave)
    elif syllable == "G#" or syllable == "Ab" : # 솔# or 라b
        return int(830 * 2 ** octave)
    
    elif syllable == "A" : # 라
        return int(880 * 2 ** octave)
    elif syllable == "A#" or syllable == "Bb" : # 라# or 시b
        return int(932 * 2 ** octave)
    
    elif syllable == "B" : # 시
        return int(988 * 2 ** octave)



# ms = 400
# delay = 80
# int(1*ms)-delay
#------------------------------------------------
Beep(sound(-1, "Bb"), 345)#345
Beep(sound(0, "C"), 115)#115
Beep(sound(0, "Eb"), 345)#345
Beep(sound(0, "F"), 115)#115
Beep(sound(0, "G"), 461)#461
Beep(sound(0, "Eb"), 461)#461
#------------------------------------------------
Beep(sound(1, "C"), 922)#922
time.sleep(0.05)
Beep(sound(0, "Bb"), 922)#922
time.sleep(0.05)
#------------------------------------------------
Beep(sound(0, "G"), 461)#461
Beep(sound(0, "F"), 345)#345
Beep(sound(0, "G"), 115)#115
Beep(sound(0, "Eb"), 461)#461
Beep(sound(0, "C"), 345)#345
Beep(sound(0, "Eb"), 115)#115
#------------------------------------------------
Beep(sound(-1, "Bb"), 1844)#1844
time.sleep(0.05)
#------------------------------------------------
Beep(sound(-1, "Bb"), 345)#345
Beep(sound(0, "C"), 115)#115
Beep(sound(0, "Eb"), 345)#345
Beep(sound(0, "F"), 115)#115
Beep(sound(0, "G"), 461)#461
Beep(sound(0, "Eb"), 461)#461
#------------------------------------------------
Beep(sound(1, "C"), 922)#922
time.sleep(0.03)
Beep(sound(0, "Bb"), 922)#922
time.sleep(0.03)
#------------------------------------------------
Beep(sound(0, "G"), 345)
Beep(sound(0, "Ab"), 115)
Beep(sound(0, "F"), 345)
Beep(sound(0, "G"), 115)
Beep(sound(0, "F"), 345)
Beep(sound(0, "Eb"), 115)
time.sleep(0.01)
Beep(sound(0, "C"), 461)
time.sleep(0.01)
#------------------------------------------------
Beep(sound(0, "Eb"), 1844)
time.sleep(0.05)
#------------------------------------------------
for value in range (2):
    Beep(sound(0, "Bb"), 345)
    Beep(sound(1, "C"), 115)
    Beep(sound(0, "Bb"), 345)
    Beep(sound(1, "C"), 115)
    Beep(sound(0, "Bb"), 345)
    Beep(sound(1, "C"), 115)
    Beep(sound(0, "Bb"), 345)
    Beep(sound(1, "C"), 115)
    time.sleep(0.02)
#------------------------------------------------
    Beep(sound(-1, "Bb"), 461)
    time.sleep(0.01)
    Beep(sound(-1, "Bb"), 461)
    time.sleep(0.01)
    Beep(sound(-1, "Bb"), 922)
    time.sleep(0.01)
#------------------------------------------------
for value in range (2):
    Beep(sound(-1, "Bb"), 345)#345
    Beep(sound(0, "C"), 115)#115
    time.sleep(0.02)
    Beep(sound(0, "Eb"), 345)#345
    time.sleep(0.02)
    Beep(sound(0, "F"), 115)#115
    time.sleep(0.02)
    Beep(sound(0, "G"), 461)#461
    time.sleep(0.02)
    Beep(sound(0, "Eb"), 461)#461
    #------------------------------------------------
    Beep(sound(1, "C"), 922)#922
    time.sleep(0.05)
    Beep(sound(0, "Bb"), 922)#922
    time.sleep(0.05)
    #------------------------------------------------
    Beep(sound(0, "G"), 461)#461
    Beep(sound(0, "F"), 345)#345
    Beep(sound(0, "G"), 115)#115
    Beep(sound(0, "Eb"), 461)#461
    Beep(sound(0, "C"), 345)#345
    Beep(sound(0, "Eb"), 115)#115
    #------------------------------------------------
    Beep(sound(-1, "Bb"), 1844)#1844
    time.sleep(0.05)
    #------------------------------------------------
    Beep(sound(-1, "Bb"), 345)#345
    Beep(sound(0, "C"), 115)#115
    Beep(sound(0, "Eb"), 345)#345
    Beep(sound(0, "F"), 115)#115
    Beep(sound(0, "G"), 461)#461
    Beep(sound(0, "Eb"), 461)#461
    time.sleep(0.03)
    #------------------------------------------------
    Beep(sound(1, "C"), 922)#922
    time.sleep(0.05)
    Beep(sound(0, "Bb"), 922)#922
    time.sleep(0.05)
    #------------------------------------------------
    Beep(sound(0, "G"), 345)
    Beep(sound(0, "Ab"), 115)
    Beep(sound(0, "F"), 345)
    Beep(sound(0, "G"), 115)
    Beep(sound(0, "F"), 345)
    Beep(sound(0, "Eb"), 115)
    time.sleep(0.01)
    Beep(sound(0, "C"), 461)
    time.sleep(0.01)
    #------------------------------------------------
    Beep(sound(0, "Eb"), 1844)
    time.sleep(0.03)
    #------------------------------------------------
    Beep(sound(0, "G"), 461)
    time.sleep(0.01)
    Beep(sound(0, "G"), 345)
    time.sleep(0.01)
    Beep(sound(0, "G"), 115)
    time.sleep(0.01)
    Beep(sound(0, "G"), 345)
    time.sleep(0.01)
    Beep(sound(0, "G"), 115)
    Beep(sound(0, "F"), 345)
    Beep(sound(0, "Eb"), 115)
    time.sleep(0.01)
    #------------------------------------------------
    Beep(sound(0, "G"), 461)
    Beep(sound(0, "F"), 345)
    Beep(sound(0, "Eb"), 115)
    Beep(sound(0, "G"), 345)
    time.sleep(0.01)
    Beep(sound(0, "G"), 115+461)
    #------------------------------------------------
    Beep(sound(1, "C"), 461)
    time.sleep(0.01)
    Beep(sound(1, "C"), 345)
    time.sleep(0.01)
    Beep(sound(1, "C"), 115)
    time.sleep(0.01)
    Beep(sound(1, "C"), 345)
    time.sleep(0.01)
    Beep(sound(1, "C"), 115)
    Beep(sound(0, "Bb"), 345)
    Beep(sound(0, "G"), 115)
    time.sleep(0.01)
    #------------------------------------------------
    Beep(sound(1, "C"), 461)
    Beep(sound(0, "Bb"), 345)
    Beep(sound(0, "G"), 115)
    Beep(sound(1, "C"), 345)
    time.sleep(0.01)
    Beep(sound(1, "C"), 115+461)
    #------------------------------------------------
    Beep(sound(1, "C"), 461)
    time.sleep(0.01)
    Beep(sound(1, "C"), 345)
    time.sleep(0.01)
    Beep(sound(1, "C"), 115)
    time.sleep(0.01)
    Beep(sound(1, "C"), 345)
    time.sleep(0.01)
    Beep(sound(1, "C"), 115)
    Beep(sound(0, "Bb"), 345)
    Beep(sound(0, "G"), 115)
    time.sleep(0.03)
    #------------------------------------------------
    Beep(sound(1, "C"), 1844)# 6:2
    time.sleep(0.03)
    #------------------------------------------------
    Beep(sound(1, "Eb"), 461)
    time.sleep(0.01)
    Beep(sound(1, "D"), 461)
    time.sleep(0.01)
    Beep(sound(1, "C"), 461)
    time.sleep(0.01)
    Beep(sound(0, "Bb"), 345)
    Beep(sound(0, "G"), 115)
    time.sleep(0.01)
    #------------------------------------------------
    Beep(sound(1, "C"), 1844)
    time.sleep(0.03)
    #------------------------------------------------
    for value in range (2):
        Beep(sound(1, "C"), 461)
        Beep(sound(0, "Bb"), 345)
        Beep(sound(0, "G"), 115)
        Beep(sound(1, "C"), 345)
        time.sleep(0.01)
        Beep(sound(1, "C"), 115+461)
        time.sleep(0.02)
    #------------------------------------------------
    Beep(sound(1, "C"), 100)
    Beep(sound(1, "C"), 100)
    Beep(sound(1, "C"), 100)
    time.sleep(0.02)
    Beep(sound(0, "Bb"), 100)
    Beep(sound(0, "Bb"), 100)
    Beep(sound(0, "Bb"), 100)
    time.sleep(0.02)
    Beep(sound(0, "G"), 100)
    Beep(sound(0, "G"), 100)
    Beep(sound(0, "G"), 100)
    time.sleep(0.02)
    Beep(sound(0, "F"), 100)
    Beep(sound(0, "F"), 100)
    Beep(sound(0, "F"), 100)
    #------------------------------------------------
    for value in range (2):
        Beep(sound(0, "Eb"), 461)
        Beep(sound(0, "C"), 345)
        Beep(sound(-1, "Bb"), 115)
        Beep(sound(0, "Eb"), 345)
        time.sleep(0.01)
        Beep(sound(0, "Eb"), 115+461)
        time.sleep(0.02)
#------------------------------------------------
Beep(sound(1, "C"), 600)
time.sleep(0.3)
Beep(sound(1, "C"), 600)
time.sleep(0.3)
#------------------------------------------------
Beep(sound(1, "C"), 922)
time.sleep(0.05)
Beep(sound(1, "D"), 922)
time.sleep(0.05)
#------------------------------------------------
Beep(sound(1, "Eb"), 1844)