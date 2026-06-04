
shopping_cart = []

while True:
    print('\n-- Shopping Cart --')
    print('1. Add item 2. View cart 3. Total Bill 4. Exit')
    choice = input('Choose an option: ')

    if choice == '1':
        name = input('item name: ')
        price = float(input('price: '))
        qty = int(input('quantity: '))
        shopping_cart.append({'name': name, 'price': price, 'quantity': qty})
        print(f'Added {qty} . {name} to cart.')
    
    elif choice == '2':
        if not shopping_cart:
            print('Your cart is empty.')
        else:
            print('Your cart contains:')
            for item in shopping_cart:
                print(f"{item['name']} . {item['quantity']} at ${item['price']} each")

    elif choice == '3':
        total = sum(item['price'] * item['quantity'] for item in shopping_cart)
        print(f'Total bill: ${total:.2f}')

    elif choice == '4':
        print('Exiting. Thank you for shopping!')
        break

    else:
        print('Invalid option. Please try again.')

