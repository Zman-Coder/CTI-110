#Benajamin Zierdt-Thorson
#P1HW1.py
#Multiplication and Addition
print("-----Calculating Exponent-----")

base_value = int(input("Enter an integer as the base value: "))
exponent_value = int(input("Enter an integer as the exponent: "))
result = base_value ** exponent_value
print(f"{base_value} raised to the power of {exponent_value} is {result} !!")  

print("----Addition and Subtraction-----")
starting_value = int(input("Enter a starting integer: "))
add_value = int(input("Enter an integer to add: "))
subtract_value = int(input("Enter an integer to subtract: "))
final_result = starting_value + add_value - subtract_value
print(f"{starting_value} + {add_value} - {subtract_value} is equal to {final_result}")

