def main():
    groceries = ['Apples', 'Oranges', 'Bananas', 'Grapes', 'Lemons']

    myList = []
    myList.append('Chips')

    print(groceries[0:])

    newG = groceries[1:3]
    print(newG)

    #adding
    groceries.append('Chips')
    groceries.insert(3, 'Cookies')
    print(groceries)

    x = groceries.pop()
    print(x)
    print(groceries)

    #mutable
    groceries[2] = 'Cereal'
    print(groceries)

    #immutable
    finalG = tuple(groceries)
    print(finalG)
    finalG[1] = 'Bananas'
    print(finalG)

main()