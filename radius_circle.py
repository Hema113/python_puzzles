#Find radius of circle
#useing math package

import math
def radius_circle(area):
    rad=math.sqrt((area/math.pi)) #find radius using formula
    return rad

#Get user input

if __name__ == "__main__":
    area=int(input("Enter the area of circle:"))
    print("Radius of circle%f" %radius_circle(area))
