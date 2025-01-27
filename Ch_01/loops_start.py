
def main():
    x = 0

    # Define a while loop
    print("While loop example:")
    while x < 5:
        print(f"x is currently: {x}")
        x += 1

    # Define a for loop
    print("\nFor loop example:")
    for i in range(5):
        print(f"i is: {i}")

    # Use a for loop over a collection
    print("\nFor loop over a collection:")
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for day in days:
        print(day)

    # Use the break and continue statements
    print("\nUsing break and continue:")
    for i in range(10):
        if i == 7:
            print("Breaking at i =", i)
            break
        if i % 2 == 0:
            print(f"Skipping even number: {i}")
            continue
        print(f"Odd number: {i}")

    # Using the enumerate() function to get index
    print("\nUsing enumerate():")
    for index, day in enumerate(days):
        print(f"Day {index + 1}: {day}")

if __name__ == "__main__":
    main()
