phonebook = {'Natee': '999-6666', 'Tae': '888-3333', 'Beam': '888-4444'}
print(phonebook)

print(phonebook['Natee'])
print(phonebook.get('Beam'))

key = 'Pluto'
if key in phonebook:
    print(phonebook['Pluto'])
else:
    print(key + ' not in phonebook')

phonebook['Simpson'] = '999-1234'
phonebook['Pluto'] = '888-5684'
phonebook['Tae'] = '888-7694'
print(phonebook)

del phonebook['Simpson']
print(phonebook)