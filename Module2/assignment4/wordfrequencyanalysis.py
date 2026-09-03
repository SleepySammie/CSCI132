import string

# Opens gba.txt in read mode, creates rawText variable to store file, calls casefold to make every word lowercase.
with open('gba.txt', 'r') as file:
    rawText = file.read().casefold()
    print(rawText)

