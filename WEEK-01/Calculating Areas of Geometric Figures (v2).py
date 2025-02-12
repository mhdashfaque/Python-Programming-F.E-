'''
AIM: 2. Calculating Areas of Geometric Figures (v2)*-
Write a MENU DRIVEN python program to calculate areas of any geometric figures
like circle, rectangle and triangle.

Hint:

Circle: area = π * r^2
Rectangle: area = length * width
Triangle: area = 0.5 * base * height

NAME: SHAIKH MOHD ASHFAQUE
'''

# Menu-driven program to calculate the area of different geometric figures

while True:
    # Display the menu
    print("\nChoose a geometric figure to calculate the area:")
    print("1. Circle")
    print("2. Rectangle")
    print("3. Triangle")
    print("4. Exit")

    # Get the user's choice
    choice = input("Enter the number corresponding to the shape (1-4): ")

    # Exit the program if the user selects 4
    if choice == '4':
        print("Exiting the program. Goodbye!")
        break

    # Calculate area based on the user's choice
    if choice == '1':
        # Circle: area = π * r^2
        radius = float(input("Enter the radius of the circle: "))
        area = 3.14159 * radius ** 2
        print(f"The area of the circle is {area:.2f} square units.")

    elif choice == '2':
        # Rectangle: area = length * width
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        area = length * width
        print(f"The area of the rectangle is {area:.2f} square units.")

    elif choice == '3':
        # Triangle: area = 0.5 * base * height
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = 0.5 * base * height
        print(f"The area of the triangle is {area:.2f} square units.")

    else:
        print("Invalid choice! Please enter a valid option (1-4).")
