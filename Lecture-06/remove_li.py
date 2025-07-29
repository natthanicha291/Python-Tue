fruits_with_duplicates = ['apple', 'banana', 'apple', 'orange', 'banana']
while 'apple' in fruits_with_duplicates:
    fruits_with_duplicates.remove('apple')
print(f"Fruits after removing: {fruits_with_duplicates}")