# Define a dictionary to store food items and their quantities
food_items = {
    "chips": 10,
    "soda": 20,
    "candy": 15,
}

# Function to display available food items
def display_menu():
    print("Available Food Items:")
    for item, quantity in food_items.items():
        print(f"{item}: {quantity} available")

# Function to dispense a food item
def dispense_item(item, quantity):
    if item in food_items and food_items[item] >= quantity:
        food_items[item] -= quantity
        print(f"Dispensing {quantity} {item}(s)")
    else:
        print("Sorry, the item is unavailable or the quantity is insufficient.")

# Main program loop
while True:
    display_menu()
    user_choice = input("Enter the item you want or 'q' to quit: ").lower()
    
    if user_choice == 'q':
        print("Thank you for using the Food ATM. Have a great day!")
        break
    
    quantity = int(input("Enter the quantity: "))
    
    dispense_item(user_choice, quantity)
