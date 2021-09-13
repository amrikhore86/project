import datetime
print("1. Area of Circle\n2. Circumference of Circle\n3. Area of rectangle\n4. Perimeter of a rectangle\n5. Display current year , month and day\n6. Display current time with current date\n0. To EXIT\nEnter your choice : \n")
def circle_area(r):
    return round((3.14*r*r),2)
def circle_circumference(r):
    return round((2*3.14*r),2)
def rectangle_area(l,b):
    return round((l*b),2)
def rectangle_perimeter(l,b):
    return round((2*(l+b)),2)
def date():
    x=datetime.datetime.now()
    return (x.strftime("%Y %B %d"))
def time():
    x=datetime.datetime.now()
    return (x.strftime("%I:%M %p , %d %B"))
choice=int(input())
if choice==1:
    r=float(input("Radius of Circle : "))
    print(circle_area(r))
elif choice==2:
    r=float(input("Radius of Circle : "))
    print(circle_circumference(r))
elif choice==3:
    l=float(input("Enter the length of the rectangle : "))
    b=float(input("Enter the breadth of the rectangle : "))
    print(rectangle_area(l,b))
elif choice==4:
    l=float(input("Enter the length of the rectangle : "))
    b=float(input("Enter the breadth of the rectangle : "))
    print(rectangle_perimeter(l,b))
elif choice==5:
    print(date())
elif choice==6:
    print(time())
elif choice==0:
    exit()
else:
    print("Wrong Choice Input")
