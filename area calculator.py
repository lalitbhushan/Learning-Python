print("********AREA CALCULATOR******")
print("""press 1 to get area of square
press 2 to get area of rectangle 
press 3 to get area of circle
press 4 to get area of triangle""")

choice=int(input("enter a number 1 to 4:"))

if choice == 1:
    side = float(input("enter the length of one side"))
    area = side*side
    print("the area of square is", area)

elif choice == 2:
    lenght=float(input("enter the lenght of rectangle"))
    width=float(input("enter the width of rectangle"))
    area = lenght*width
    print("area of rectangle is", area)

elif choice == 3:
    radius = float(input("enter the radius of circle"))
    area = ((22/7)*(radius**2))
    print("area of circle is:",area)

elif choice == 4:
    base = float(input("enter the base of triangle:"))
    height = float(input("enter the height of the triangle"))
    area = 0.5*base*height
    print("area of the triangle", area)

else :
      print("invalid input")
