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
    chemchar = [
        [], # Elements (Row 0)
        []  # Amounts  (Row 1)
    ]
    for e in range(len(chemlist)):
        found = False
        char = chemlist[e]
        for f in range(len(chemchar[0])):
            if char == chemchar[0][f]: # If the element is already in the list, add 1 to the amount.
                chemchar[1][f] = chemchar[1][f] + 1
                found = True
                break # If found, exit the loop.
        if not found: # If after all iterations the element is not in the list, add it to the list and 1 to the amount.
            chemchar[0].append(char)
            chemchar[1].append(1)
    return chemchar

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

# Store in a dictionary.
datachem = {}
for i in range(len(react)):
    key = f'reac{i}'
    datachem[key] = enmark(enlist(react[i]))
for i in range(len(prod)):
    key = f'prod{i}'
    datachem[key] = enmark(enlist(prod[i]))