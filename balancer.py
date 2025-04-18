import sys

def interpret(chemical):
    # First we check for uppercase (C, H, O, P)
    chemint = [
        [], #Chemicals (Row 0)
        []  #Amounts   (Row 1)
    ]
    for j in range(len(chemical)): #Missing () interpretation.
        char = chemical[j]
        index = -1
        if char.isupper():
            chemint[0].append(char)
            chemint[1].append(1)
            index = index + 1
        if char.islower():
            chemint[0][index] = chemical[j-1:j]
        if char.isdigit():
            chemint[1][index] = int(char)
    return chemint

#######################################################################################################################

# Input should be a .txt file (chemprocess.txt) (CHEM1+CHEM2=CHEM3+CHEM4) or arguments (CHEM1 CHEM2 = CHEM3 CHEM4)
flag = 0
if len(sys.argv) > 1:
    for i in range(len(sys.argv)-1):
        # Locate the '=' to split the reaction between reagents and products
        if sys.argv[i+1] == '=':
            react = sys.argv[1:(i+1)]
            prod = sys.argv[(i+2):]
            flag = 1
    if flag == 0:
        sys.exit('\033[91mExpected error 2: Incorrect formula, no = found.\033[0m')
# Planning to add a way so it can loop multiple ways around so it can run a lot of formulas if used with a .txt file
# len(sys.argv) > 1 is therefore redundant until this part is added.
else:
    sys.exit('\033[91mExpected error 1: No arguments.\033[0m')

table1 = interpret(react[0])
print(table1[0])
print(table1[1])