# Add a new product to the inventory
def add_product(inventory):

    # Ask for product name
    name = input('Product name: ').strip()

    # Validate name
    if not name:
        print('Name is required.')
        return

    # Check if product already exists
    if search_product(inventory, name):
        print('Product already exists. Use update.')
        return

    # Ask for price
    try:
        price = float(input('Price: '))
        if price <= 0:
            print('Price must be positive.')
            return
    except ValueError:
        print('Invalid number.')
        return

    # Ask for quantity
    try:
        quantity = int(input('Quantity: '))
        if quantity <= 0:
            print('Quantity must be positive.')
            return
    except ValueError:
        print('Invalid number.')
        return

    # Create product dictionary
    product = {
        'name': name,
        'price': price,
        'quantity': quantity
    }

    # Add product to inventory
    inventory.append(product)

    print(f'Product {name} added successfully.')


# Show all inventory
def show_inventory(inventory):

    # Check if inventory is empty
    if not inventory:
        print('Inventory is empty.')
        return

    print('\n=== INVENTORY ===')
    print('{:<25} {:>10} {:>10}'.format('PRODUCT', 'PRICE', 'QUANTITY'))
    print('-' * 50)

    total = 0

    # Loop through products
    for p in inventory:
        subtotal = p['price'] * p['quantity']
        total += subtotal

        print('{:<25} ${:>9.2f} {:>10}'.format(
            p['name'], p['price'], p['quantity']))

    print('-' * 50)
    print('TOTAL VALUE: ${:.2f}'.format(total))


# Search for a product by name
def search_product(inventory, name):

    name_lower = name.lower().strip()

    # Loop through inventory
    for product in inventory:
        if product['name'].lower() == name_lower:
            return product

    print(f'Product {name} not found.')
    return None


# Update product price or quantity
def update_product(inventory, name, new_price=None, new_quantity=None):

    # Find product
    product = search_product(inventory, name)

    if not product:
        return

    updated = "N"  # Track if something was updated

    # Update price
    if new_price is not None:
        if new_price <= 0:
            print('Price must be positive.')
            return

        product['price'] = new_price
        print(f'Price updated to ${new_price}')
        updated = "S"

    # Update quantity
    if new_quantity is not None:
        if new_quantity < 0:
            print('Quantity cannot be negative.')
            return

        product['quantity'] = new_quantity
        print(f'Quantity updated to {new_quantity}')
        updated = "S"

    # Final message
    if updated == "S":
        print(f'Product {name} updated.')
    else:
        print('No valid changes provided.')


# Delete a product
def delete_product(inventory, name):

    # Find product
    product = search_product(inventory, name)

    if not product:
        return

    # Ask confirmation using S/N
    confirm = input(f'Delete {name}? (S/N): ').strip().upper()

    if confirm == 'S':
        inventory.remove(product)
        print(f'Product {name} deleted.')
    else:
        print('Deletion canceled.')

