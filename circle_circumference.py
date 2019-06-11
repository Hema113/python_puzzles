#find area of circle and circumference

PI=3.14 #Define PI as constant value

#This function find area of circle
def area_circle(r):
    return PI * r * r

#This function find circumference of circle
def circumference_circle(r):
    return PI * 2.0 * r

"""Get user input"""
r=float(input("Enter the circle radius:"))
print("Area of circle is:%.2f" %area_circle(r))
print("Circumference of circle is:%.2f"
        %circumference_circle(r))


