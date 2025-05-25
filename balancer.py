import sys
import numpy as np

def enlist(chemical):
    chemlist = []
    for e in range(len(chemical)):
        char = chemical[e]
        index = -1  # Index starts -1 so it gives an accurate list value.
        if char.isupper(): # If the character is upper, add it to a new entry.
            chemlist.append(char)
            index = index + 1
        if char.islower(): # If the character is lower, assign it to the previous upper character.
            chemlist[index] = chemlist[index] + char
        if char.isdigit(): #
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
        [], # Amounts  (Row 1)
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

def gaussprep(chemdata):
    elempres = []
    for e in range(len(chemdata)): # ID all elements that are in the whole reaction.
        found = False
        key = f'chem{e}'
        for f in range(len(chemdata[key][0])): # Elements are allocated on row 0 of the dictionary entry.
            for g in range(len(elempres)):
                if chemdata[key][0][f] == elempres[g]:
                    found = True
                    break # The element is already on the list, so no need to keep looking, skip to the next one.
            if not found:
                elempres.append(chemdata[key][0][f]) # If not found, add it to the list.

    mtrx = []
    zeroA = []
    for e in range(len(elempres)): # Generate the matrix.
        mtrx.append([]) # Add 1 new line to the matrix.
        for f in range(len(chemdata)):
            found = False
            key = f'chem{f}'
            for g in range(len(chemdata[key][0])):
                if chemdata[key][0][g] == elempres[e]:
                    mtrx[e].append(chemdata[key][1][g]*chemdata[key][2]) #If found, add with the ID multiplier.
                    found = True
                    break
            if not found:
                mtrx[e].append(0) # If not found, add a 0.

    for e in range(len(chemdata)):
        zeroA.append(0)

    return mtrx,elempres,zeroA
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

datachem = {} # Create and store all chemicals in readable dictionaries with enmark() and enlist().
for i in range(len(react)):
    key = f'chem{i}'
    datachem[key] = enmark(enlist(react[i]))
    datachem[key].append(1) # IDs as a reactant.
for i in range(len(prod)):
    key = f'chem{i+len(react)}'
    datachem[key] = enmark(enlist(prod[i]))
    datachem[key].append(-1) # IDs as a product.

print(f'\nFollowing tables generated:') # FOR TESTING
for i in range(len(datachem)):
    key = f'chem{i}'
    print(f'{datachem[key]}')

print(f'\nMatrix: {gaussprep(datachem)[0]}') # FOR TESTING
print(f'Index: {gaussprep(datachem)[1]}')  # FOR TESTING
print(f'Zero matrix: {gaussprep(datachem)[2]}')  # FOR TESTING