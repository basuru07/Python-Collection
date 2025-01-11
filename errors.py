num = input("Enter a Number :")

try:
    num = int(num)
except:
    num = -1
    
    if num > 0:
        print("Wrong Number")
    else:
        print("Not a Number")    
        
 
 
        
try:
    r = float(input("Enter the radius (r) value: "))  # Attempt to convert input to float

    def circumference(r):
        circumferences = 2 * 3.14 * r
        print(f"Circumference: {circumferences:.2f}")  # Format to 2 decimal places

    circumference(r)

except ValueError:  # Handle invalid input
    print("Error: Please enter a valid numeric value for the radius.")
        