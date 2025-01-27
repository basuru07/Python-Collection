#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

# Errors can happen in programs, and we need a clean way to handle them
def divide_numbers(a, b):
    try:
        result = a / b  # This will raise an error if b is zero
        print(f"The result of {a} divided by {b} is: {result}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
def main():
    divide_numbers(10, 2)  # No error
    divide_numbers(10, 0)  # This will cause a ZeroDivisionError
    divide_numbers("10", 2)  # This will cause a TypeError

if __name__ == "__main__":
    main()
