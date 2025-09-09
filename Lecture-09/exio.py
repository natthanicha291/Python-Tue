filename = input('Enter filename: ')
try:
    with open(filename, 'r') as infile:
        content = infile.read()
        print(content)
        infile.close()
except IOError:
    print('An error occurred trying to read the file.')
    print('the file', filename)

print('End of the program')