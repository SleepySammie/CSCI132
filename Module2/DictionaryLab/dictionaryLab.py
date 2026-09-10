#1.1 Create a dictionary
contacts = {
    'Alice': '555-1234',
    'Bob': '555-5678',
    'Carmen': '555-8765'
    }
# print(contacts)
# print(type(contacts))

#1.2 Access Dictionary Values
# key = 'Alice'
# print(contacts[key])
# print(contacts['Bob'])

#1.3 Key Error
# print(contacts['alice'])

#1.4 Check using in operator
# if 'alice' in contacts:
#     print(contacts['alice'])
# else:
#     print('Not found')

#1.5 Safe access using get() method
# print(contacts.get('alice', 'Not found'))

#2.1 Add a new keyvalue pair
contacts['David'] = '555-0001'
contacts['alice'] = '333-2222'
# print(contacts)

#2.2 Update existing keyvalue pair
# contacts['Alice'] = '555-0000'
# print(contacts)

#2.3 Remove keyvalue pair using del
# del contacts['alice']
# print(contacts)

#2.4 Remove keyvalue pair using pop()
# removed = contacts.pop('steve', 'Error on key')
# print(removed)

#2.5 Getting all keys and values
# allKeys = contacts.keys()
# print(allKeys)
# print(type(allKeys))

# allValues = contacts.values()
# print(allValues)
# print(type(allValues))

# allItems = contacts.items()
# print(allItems)
# print(type(allItems))

#2.6 Iterate through the dictionary
for k in contacts.keys():
    print(k)

for v in contacts.values():
    print(v)

for i in contacts.items():
    print(i)

for k , v in contacts.items():
    print(f'The key {k}, The value {v}')