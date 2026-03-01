#Benajamin Zierdt-Thorson
#22FEB2026
#P2LAB2.py
#Cars and MPG Calculations

cars = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}
cars_keys = cars.keys()
print(cars_keys)

print (*cars, sep = ", ")

Car_name = input("Enter the car: ")
car_mpg = cars[Car_name]
print(f"The {Car_name} gets {car_mpg} miles per gallon.")

miles_driven = float(input(f"How many miles will you drive the {Car_name}? "))
gallons_needed = miles_driven / car_mpg
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {Car_name} {miles_driven} miles.")
