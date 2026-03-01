# Benjamin Zierdt-Thorson
# 01MAR2026
# P2HW1.py
# Budget 2.0

print("This program calculates and displays travel expenses")

budget_value = float(input("Enter Budget: "))
print()

destination_value = input("Enter your travel destination: ")
print()

gas_value = float(input("How much do you think you will spend on gas? "))
print()

hotel_value = float(input("Approximately, how much will you need for accommodation/hotel? "))
print()

food_value = float(input("Last, how much do you need for food? "))
print()

print("-----------Travel Expenses-----------")

print(f"{'Location:':<20}{destination_value}")
print(f"{'Initial Budget:':<20}${budget_value:,.2f}")
print(f"{'Fuel:':<20}${gas_value:,.2f}")
print(f"{'Accommodation:':<20}${hotel_value:,.2f}")
print(f"{'Food:':<20}${food_value:,.2f}")

total_expenses = gas_value + hotel_value + food_value
remaining_balance = budget_value - total_expenses

print("-" * 39)
print()
print(f"{'Remaining Balance:':<20}${remaining_balance:,.2f}")
