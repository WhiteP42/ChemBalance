import sys

def enlist(chemical):
    chemlist = []
    for e in range(len(chemical)):
        char = chemical[e]
        index = -1  # Index starts -1 so it gives an accurate list value.
        if char.isupper():
            chemlist.append(char)
            index = index + 1
        if char.islower():
            chemlist[index] = chemlist[index] + char
        if char.isdigit():
            iteration = 0
            amount = int(chemical[e]) - 1
            for j in range(amount):
                chemlist.append(chemlist[index])
            iteration = iteration + 1
            index = index + iteration
    return chemlist

def enmark(chemlist):
    return

#######################################################################################################################

# Input should be a .txt file (chemprocess.txt) (CHEM1+CHEM2=CHEM3+CHEM4) or arguments (CHEM1 CHEM2 = CHEM3 CHEM4)
# Parenthesis should be substituted by < >. Ex: Al2<SO4>3 for Al2(SO4)3.

flag = 0
if len(sys.argv) > 1:
    for i in range(len(sys.argv) - 1):
        # Locate the '=' to split the reaction between reagents and products.
        if sys.argv[i+1] == '=':
            react = sys.argv[1:(i + 1)]
            prod = sys.argv[(i + 2):]
            flag = 1
    if flag == 0:
        sys.exit('\033[91mExpected error 2: Incorrect formula, no = found.\033[0m')
# Planning to add a way so it can loop multiple ways around so it can run a lot of formulas if used with a .txt file
# len(sys.argv) > 1 is therefore redundant until this part is added.
else:
    sys.exit('\033[91mExpected error 1: No arguments.\033[0m')

datachem = {} # Set a dictionary to store chemicals and amounts.
