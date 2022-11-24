floor = 5

mainflag = True
baseflag = True
subflag = True

mainvalue = 0
basevalue = 0
subvalue = 0
while mainflag:
    mainvalue += 1
    basevalue = 0
    baseflag = True
    
    while baseflag:
        basevalue += 1
        subvalue = 0
        subflag = True
        
        while subflag:
            print("*", end="")
            subvalue += 1
            if subvalue == floor:
                subflag = False
        
        print("")
        if basevalue == floor:
            baseflag = False
            
    print("")
    
    if mainvalue == 3:
        mainflag = False