'''
AIM: 3.Developing Conversion Utilities: Develop any converter
such as Rupees to dollar,temperature convertor, inch to feet etc.

Hint:

dollars = rupees / 82.00
fahrenheit = (celsius * 9/5) + 32
feet = inches / 12

NAME: SHAIKH MOHD ASHFAQUE
'''
# Display the menu of available converters
print("Choose a conversion utility:")
print("1. Rupees to Dollars")
print("2. Celsius to Fahrenheit")
print("3. Inches to Feet")

# Get the user's choice
choice = input("Enter the number corresponding to the conversion: ")

# Perform conversion based on the user's choice
if choice == '1':
    # Rupees to Dollars: 1 USD = 82.00 INR (you can change this value based on the current rate)
    rupees = float(input("Enter the amount in Rupees: "))
    dollars = rupees / 82.00
    print(f"{rupees} Rupees is equal to {dollars:.2f} Dollars.")

elif choice == '2':
    # Celsius to Fahrenheit: (Celsius * 9/5) + 32
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} Celsius is equal to {fahrenheit:.2f} Fahrenheit.")

elif choice == '3':
    # Inches to Feet: 1 foot = 12 inches
    inches = float(input("Enter the length in inches: "))
    feet = inches / 12
    print(f"{inches} inches is equal to {feet:.2f} feet.")

else:
    print("Invalid choice! Please enter 1, 2, or 3.")
