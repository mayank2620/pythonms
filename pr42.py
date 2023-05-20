# Get user input for the sides
side1 = float(input("Enter the first side of the triangle: "))
side2 = float(input("Enter the second side of the triangle: "))
side3 = float(input("Enter the third side of the triangle: "))

# Check if the input forms a valid triangle
if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    # Determine the type of the triangle
    if side1 == side2 == side3:
        print("The triangle is equilateral")
    elif side1 == side2 or side2 == side3 or side1 == side3:
        if side1**2 + side2**2 == side3**2 or side2**2 + side3**2 == side1**2 or side1**2 + side3**2 == side2**2:
            print("The triangle is isosceles and right-angled")
        else:
            print("The triangle is isosceles")
    elif side1**2 + side2**2 == side3**2 or side2**2 + side3**2 == side1**2 or side1**2 + side3**2 == side2**2:
        print("The triangle is right-angled")
    else:
        print("The triangle is scalene")
else:
    print("The input does not form a valid triangle")