floor = 5

mainflag = True
baseflag = True
subflag = True
mainvalue = 0
basevalue = 0
subflag = 0

while mainflag:
    mainvalue += 1
    basevalue = 0
    baseflag = True
    while baseflag:
        subvalue = 0
        subflag = True
        
        while subflag:
            if mainvalue == 1:
                if basevalue % 2 and\
                    subvalue % 2:
                        print(" ", end="")
                else:
                    print("*", end="")
                
            if mainvalue == 2:
                if basevalue == subvalue:
                    print(" ", end="")
                else:
                    print("*", end="")
            subvalue += 1
            if subvalue == floor:
                subflag = False
                
        print("")
        basevalue += 1
        if basevalue == floor:
            baseflag = False
    print("")
    if mainvalue == 2:
        mainflag = False