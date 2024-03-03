print("=====================")
print("    Area Calculator 📐  ")
print("=====================")

print("""
1) Triangle
2) Rectangle
3) Square
4) Circle
5) Quit""")

response = int(input("Choose a shape: "))
if response == 1:
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    area = 0.5 * base * height
    print(f"The area of the triangle is {area}")
    
elif response == 2:
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = length * width
    print(f"The area of the rectangle is {area}")
    
elif response == 3:
    side = float(input("Enter the side: "))
    area = side * side
    print(f"The area of the square is {area}")
elif response == 4:
    radius = float(input("Enter the radius: "))
    area = 3.14159 * radius * radius
    print(f"The area of the circle is {area}")
