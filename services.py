# services.py: statistics

def calculate_statistics(inventory):
    # Function to calculate and display inventory statistics

    if not inventory:
        # Check if inventory is empty
        print('No products available.')
        return {}  # Return empty dictionary if no data

    # Initialize variables
    total_units = 0          # Total quantity of all products
    total_value = 0          # Total value (price * quantity)
    most_expensive = None    # Store most expensive product
    highest_stock = None     # Store product with highest quantity

    # Loop through all products
    for p in inventory:
        total_units += p['quantity']  # Add quantity
        total_value += p['price'] * p['quantity']  # Calculate total value

        # Check if current product is more expensive
        if most_expensive is None or p['price'] > most_expensive['price']:
            most_expensive = p

        # Check if current product has more stock
        if highest_stock is None or p['quantity'] > highest_stock['quantity']:
            highest_stock = p

    # Print results
    print('\n=== STATISTICS ===')
    print(f'Total units: {total_units}')
    print(f'Total value: ${total_value:.2f}')

    # Show most expensive product if exists
    if most_expensive:
        print(f'Most expensive: {most_expensive["name"]} (${most_expensive["price"]})')

    # Show product with highest stock if exists
    if highest_stock:
        print(f'Highest stock: {highest_stock["name"]} ({highest_stock["quantity"]})')

    # Return statistics as dictionary
    return {
        'total_units': total_units,
        'total_value': total_value
    }
