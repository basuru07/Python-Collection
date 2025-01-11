name = str(input("Enter the Name: "))
def printme(name):
    print("Hello, " + name)
    
    
printme(name)



r = float(input("Enter the r value: "))

# circumference of a circle
def circumference(r):
    circumferences = 2 * 3.14 * r
    print("Circumference: " + str(circumferences))  

# area of a circle
def area(r):
    areas = 3.14*r*r
    print("Area: " + str(areas))

# call the funtion    
circumference(r)
area(r)