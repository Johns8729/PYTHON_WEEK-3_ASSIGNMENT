from functions import *
from services import calculate_statistics
from files import save_csv, load_csv


# Merge inventories (combine existing + new)
def merge_inventory(current, new):

    # Loop through new products
    for n in new:
        found = "N"  # Track if product exists

        # Check if product already exists
        for c in current:
            if c['name'].lower() == n['name'].lower():
                c['quantity'] += n['quantity']  # Add quantity
                c['price'] = n['price']        # Update price
                found = "S"
                break

        # If not found → add new product
        if found == "N":
            current.append(n)

    print("Merge completed.")


def main():
    inventory = []

    # Control variable instead of while True
    running = "S"

    while running == "S":

        # Show menu
        print('\n=== MENU ===')
        print('1. Add')
        print('2. Show')
        print('3. Search')
        print('4. Update')
        print('5. Delete')
        print('6. Stats')
        print('7. Save CSV')
        print('8. Load CSV')
        print('9. Exit')

        option = input('Option: ').strip()

        # ADD PRODUCT
        if option == '1':
            add_product(inventory)

        # SHOW INVENTORY
        elif option == '2':
            show_inventory(inventory)

        # SEARCH PRODUCT
        elif option == '3':
            name = input('Name: ')
            product = search_product(inventory, name)

            if product:
                print(product)

        # UPDATE PRODUCT
        elif option == '4':
            name = input('Name: ')
            price = input('New price: ')
            quantity = input('New quantity: ')

            p = float(price) if price else None
            q = int(quantity) if quantity else None

            update_product(inventory, name, p, q)

        # DELETE PRODUCT
        elif option == '5':
            name = input('Name: ')
            delete_product(inventory, name)

        # SHOW STATISTICS
        elif option == '6':
            calculate_statistics(inventory)

        # SAVE CSV
        elif option == '7':
            path = input('File path: ') or 'inventory.csv'

            result = save_csv(inventory, path)

            if result == "S":
                print("Saved successfully.")
            else:
                print("Failed.")

        # LOAD CSV
        elif option == '8':
            path = input('File path: ')

            new, errors, status = load_csv(path)

            # If loading failed → stop this action
            if status == "N":
                print("Load canceled.")
            else:
                print(f'Errors: {errors}')

                if new:
                    choice = input('Overwrite? (S/N): ').upper()

                    # Replace inventory
                    if choice == 'S':
                        inventory = new
                        print("Inventory replaced.")

                    # Merge inventory
                    else:
                        merge_inventory(inventory, new)

        # EXIT PROGRAM
        elif option == '9':
            print('Exit...')
            running = "N"  # Stop program

        else:
            print('Invalid option.')

    # Final summary when program ends
    if inventory:
        print('\nFINAL SUMMARY')
        show_inventory(inventory)
        calculate_statistics(inventory)


# Run program
if __name__ == '__main__':
    main()
