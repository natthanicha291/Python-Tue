phonebook = {'Natee': '999-6666', 'Tae': '888-3333', 'Beam': '888-4444', 'Peanut': "666-4987"}

heroesdict = {}
heroesdict['Hulk'] = '444-6498'
heroesdict['Ironman'] = '666-1234'
print(heroesdict.get('Halk', 'Key not found'))
print(heroesdict.get('Hulk', 'Key not found'))

for key, value in phonebook.items():
    print(key, value)

print(phonebook.keys())
print(phonebook.values())

print(phonebook.pop('Nat', 'Element not found'))
print(phonebook.pop('Natee', 'Element not found'))
print(phonebook)
print(phonebook.popitem)
print(phonebook)
phonebook.clear()
print('After clear')
print(phonebook)