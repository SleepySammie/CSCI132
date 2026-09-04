import string

def getTextList():
    # Opens gba.txt in read mode, creates rawText variable to store file, calls casefold to make every word lowercase.
    with open('gba.txt', 'r') as file:
        rawText = file.read().casefold()

        # Created cleanText variable, calls translate method to replace text, creates translation table with empty arguments and removes punctuation using the third argument.
        cleanText = rawText.translate(str.maketrans('', '', string.punctuation))
        cleanText.split()

        # Created textList and split cleanText into individual words in the list.
        textList = cleanText.split()
        return (textList)

def getTextDictionary():
    # Created an empty dictionary and iterated over the list, if word is in the dictionary then the value is increased by 1, else the dictionary assigns the key the value 1.
    textDict = {}

    for word in getTextList():
        if word in textDict:
            textDict[word] += 1
        else:
            textDict[word] = 1

    return (textDict)

def main():
    # Print statement
    Count = getTextDictionary()
    print(Count)

main()