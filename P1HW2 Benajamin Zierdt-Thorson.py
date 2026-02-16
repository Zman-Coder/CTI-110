#Benajamin Zierdt-Thorson
#15FEB2026
#P1HW2.py
#Budget
#Pseudocode (logic)
print("This program calculates and displays travel expenses")
budget_value = int(input("Enter Budget: "))
destination_value = input("Enter your travel destination: ")
gas_value = int(input("How much do you think you will spend on gas? "))
hotel_value = int(input("Approximately, how much will you need for accomodation/hotel? "))
food_value = int(input("Last, how much do you need for food? "))
print("-----Travel Expenses-----")
print(f"Destination: {destination_value}")
print(f"Budget: ${budget_value}")
print(f"Fuel: ${gas_value}")
print(f"Accommodation: ${hotel_value}")
print(f"Food: ${food_value}")
total_expenses = (gas_value + hotel_value + food_value) - budget_value
print(f'Remaining Balance: ${total_expenses}')
