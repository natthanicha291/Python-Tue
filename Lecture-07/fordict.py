phonebook = {'Natee': '999-6666', 'Tae': '888-3333', 'Beam': '888-4444'}

phonebook['Peanut'] = [1, 3, 5]

elements = len(phonebook)
print('There ars ', elements, ' names in phonebook[key]')

phonebook['Peanut'][1] = 9
print(phonebook)