#AREA CALCULATOR

print("***************Area Calculator*******************")

print("""Press 1 to find the Area of Square
      Press 2 to find the Area of Rectangle
      press 3 to find the Area of Circle
      Press 4 to find the Area of Triangle""")

choice = int(input("Enter the your Choice: "))

if choice == 1:
    side = float(input("Enter the length of the one side: "))
    area = side**2 
    print("The area of the square is :", area)

elif choice == 2:
    length = float(input("Enter the length : "))
    Breadth = float(input("Enter the breadth : "))
    area = length*Breadth
    print("The area of the rectangle is : ", area)

elif choice == 3:
    radius = float(input("Enter the radius of the circle : "))    
    area = 3.14*radius*radius
    print("The area of the circle is :", area)

elif choice == 4:
    a = float(input("Enter the perimeter of the Triangle : "))
    b = float(input("Enter the perimeter of the Triangle : "))
    c = float(input("Enter the perimeter of the Triangle : "))
    perimeter = a + b + c
    print("The perimeter of the Triangle is : ", perimeter)

else:
    print("Wrong input")
