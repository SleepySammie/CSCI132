#part1

# f = open('roster.txt', 'w')
# f.close()

with open('roster.txt', 'w') as rosterFile:
    rosterFile.write('Alice\n')
    rosterFile.write('Bob\n')
    rosterFile.write('Fred\n')


names = ['Moe\n', 'Larry\n', 'Curly\n']
with open('roster.txt', 'a') as rosterFile:
    rosterFile.writelines(names)

# print('Done writing')

# reads

# with open('roster.txt', 'r') as rosterFile:
#     contents = rosterFile.readlines()

# print(contents)
# print(type(contents))

# read one line at a time

# with open('roster.txt', 'r') as rosterFile:
#     for line in rosterFile:
#         print(line.strip())

with open('scores.txt', 'r') as scoresFile:
    allScores = scoresFile.readlines()
    intScores = []
    for s in allScores:
        intScores.append(int(s.strip()))

total = 0
for item in intScores:
    total += item

print(intScores)
print(total)
print(f'The average is {total / len(intScores)}')