def float_point(FPnum):
    Enum = 0
    while FPnum >= 10:
        FPnum = FPnum / 10
        Enum += 1
        
    return str(round(FPnum, 2)) + "e" + str(Enum)

value = 1000
print(float_point(value))