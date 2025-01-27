# Define a basic function
def fun1():
    print("I know my Knowledge")

# Function that takes arguments
def fun2(name):
    print(f"Hello, {name}! Welcome to learning Python.")

# Function that returns a value
def fun3(x, y):
    return x + y

# Function with default value for an argument
def fun4(greeting="Hi"):
    print(f"{greeting}, how are you?")

# Function with variable number of arguments
def fun5(*args):
    print("You passed the following arguments:")
    for arg in args:
        print(arg)



# Call the basic function
fun1()

# Call the function that takes arguments
fun2("Alice")

# Call the function that returns a value
result = fun3(10, 20)
print(f"The sum of 10 and 20 is: {result}")

# Call the function with a default value for an argument
fun4()
fun4("Hello")

# Call the function with a variable number of arguments
fun5("apple", "banana", "cherry")
