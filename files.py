import csv  # Module to work with CSV files
import os   # Module to interact with the operating system (files, paths)


def save_csv(inventory, path):
    # Function to save the inventory into a CSV file

    if not inventory:
        # Check if inventory is empty
        print("Inventory empty.")
        return "N"  # Return "N" if there is nothing to save

    try:
        # Open file in write mode
        with open(path, 'w', newline='', encoding='utf-8') as file:
            
            # Create a CSV writer with defined field names
            writer = csv.DictWriter(file, fieldnames=["name", "price", "quantity"])
            
            writer.writeheader()  # Write header row
            writer.writerows(inventory)  # Write all inventory data

        print(f"Saved in: {path}")  # Success message
        return "S"  # Return "S" if operation is successful

    except:
        # Catch any error during file writing
        print("Error saving file.")
        return "N"  # Return "N" if error occurs


def load_csv(path):
    # Function to load inventory from a CSV file with validation

    if not os.path.exists(path):
        # Check if file exists
        print("File not found.")
        return [], 0, "N"  # Return empty list, no errors, and status "N"

    valid = []   # List to store valid products
    errors = 0   # Counter for invalid rows

    try:
        # Open file in read mode
        with open(path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)  # Read CSV as dictionary

            # Validate header structure
            if reader.fieldnames != ['name', 'price', 'quantity']:
                print("Invalid format.")
                return [], 1, "N"

            # Iterate through each row
            for row in reader:
                try:
                    # Convert values to correct types
                    price = float(row['price'])
                    quantity = int(row['quantity'])

                    # Validate values (no negatives allowed)
                    if price < 0 or quantity < 0:
                        errors += 1
                        continue  # Skip invalid row

                    # Add valid product to list
                    valid.append({
                        "name": row['name'],
                        "price": price,
                        "quantity": quantity
                    })

                except:
                    # If conversion fails, count as error
                    errors += 1

        print(f'Loaded: {len(valid)}, Errors: {errors}')  # Summary
        return valid, errors, "S"  # Return valid data and success status

    except:
        # Catch any error during file reading
        print("Error loading file.")
        return [], 1, "N"  # Return error status
