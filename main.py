#This is where the main script will go

#options for statements
ifs = []
whiles = []
fors = []

with open('testInput.py') as f:
    for line in f:
        if '#' in line:
            line = line.split('#')[0]
        if 'if' in line:
            ifs.append(line)
        if 'while' in line:
            whiles.append(line)
        if 'for' in line:
            fors.append(line)

print(ifs)
print(whiles)
print(fors)

#split ifs between if and :
ifConds = [ ifs[i].split('if')[1].split(':')[0].lstrip() for i in range(len(ifs)) ]
#split whiles between while and :
whileConds = [ whiles[i].split('while')[1].split(':')[0].lstrip() for i in range(len(whiles)) ]
#split fors between for and :


print(ifConds)
print(whileConds)
