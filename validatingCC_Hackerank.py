import re
numOfCredits = int(input())

for i in range(numOfCredits):
    cc = input()
    #matches starting 4 5 6  then 0 to 9 x3 times then 0 to 1 - and 0-9 4 times and repeat by 3
    valid = r"[456][0-9]{3}(-?[0-9]{4}){3}$"
    # matches digits group and looks ahead if any repeating
    repeating = r"(([0-9])(?!\2{3})){16}"
    if re.match(valid,cc):
        if re.match(repeating,cc.replace("-","")):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")