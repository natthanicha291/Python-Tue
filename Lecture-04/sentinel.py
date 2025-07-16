keep_going = 'y'

while keep_going == "y":
    price = float(input('Enter the item is wholesale cost: '))
    # another = float(input('Enter the item is wholesale cost:'))

    retail_price = price * 2.5

    print(f'The retail price is: ${retail_price:.2f}')

    keep_going = input('Do you have another item? (y/n): ')

    