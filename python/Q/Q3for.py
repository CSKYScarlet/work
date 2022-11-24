floor = 5

for mainvalue in range(2):
    for basevalue in range(floor):
        for subvalue in range(floor):
            if mainvalue == 0:
                if basevalue % 2 and\
                    subvalue % 2:
                     print(" ", end="")
                else:
                    print("*", end="")
                    
            if mainvalue == 1:
                if basevalue == subvalue:
                    print(" ", end="")
                else:
                    print("*", end="")
        print("")
    print("")