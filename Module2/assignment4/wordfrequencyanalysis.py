import string

# Opens gba.txt in read mode, creates rawText variable to store file, calls casefold to make every word lowercase.
with open('gba.txt', 'r') as file:
    rawText = file.read().casefold()

    # Created cleanText variable, calls translate method to replace text, creates translation table with empty arguments and removes punctuation using the third argument 
    cleanText = rawText.translate(str.maketrans('', '', string.punctuation))
    cleanText.split()
    print(cleanText)

    # Created textList and split cleanText into individual words in the list.
    textList = cleanText.split()
    print(textList)

    