#This is where the main script will go

l = []

with open('testInput.py') as f:
    for line in f:
        l.append(line)

print(l)
