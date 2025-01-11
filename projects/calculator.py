def calculator():
    history = []  # List to store calculation history

    while True:
        print("\nSelect operation:")
        print("1.Add      : +")
        print("2.Subtract : -")
        print("3.Multiply : *")
        print("4.Divide   : /")
        print("5.Power    : ^")
        print("6.Remainder: %")
        print("7.Terminate: #")
        print("8.Reset    : $")
        print("9.History  : ?")
        
        choice = input("Enter choice (+, -, *, /, ^, %, #, $, ?): ")

        # Terminate the program
        if choice == "#":
            print("Terminating the program. Goodbye!")
            break
        
        # Reset history
        elif choice == "$":
            history = []
            print("History has been reset.")
        
        # Display history
        elif choice == "?":
            if history:
                print("Calculation History:")
                for record in history:
                    print(record)
            else:
                print("No history available.")
        
        # Perform calculations
        elif choice in ['+', '-', '*', '/', '^', '%']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                
                if choice == '+':
                    result = num1 + num2
                    operation = f"{num1} + {num2} = {result}"
                elif choice == '-':
                    result = num1 - num2
                    operation = f"{num1} - {num2} = {result}"
                elif choice == '*':
                    result = num1 * num2
                    operation = f"{num1} * {num2} = {result}"
                elif choice == '/':
                    if num2 != 0:
                        result = num1 / num2
                        operation = f"{num1} / {num2} = {result}"
                    else:
                        operation = "Error: Division by zero."
                elif choice == '^':
                    result = num1 ** num2
                    operation = f"{num1} ^ {num2} = {result}"
                elif choice == '%':
                    result = num1 % num2
                    operation = f"{num1} % {num2} = {result}"

                # Save valid operations to history
                if "Error" not in operation:
                    history.append(operation)
                
                print(operation)

            except ValueError:
                print("Invalid input. Please enter numeric values.")
        
        # Invalid option
        else:
            print("Invalid choice. Please try again.")

# Run the calculator
calculator()
