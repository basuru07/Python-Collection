#
# Example file for working with conditional statements
# LinkedIn Learning Python course by Joe Marini
#

def main():
    x, y = 10, 100

    # Conditional flow uses if, elif, else
    if x < y:
        print(f"{x} is less than {y}")
    elif x == y:
        print(f"{x} is equal to {y}")
    else:
        print(f"{x} is greater than {y}")

    # Conditional statements let you use "a if C else b"
    result = "x is less than y" if x < y else "x is not less than y"
    print(result)

    # match-case makes it easy to compare multiple values
    value = "one"
    match value:
        case "one":
            print("The value is one")
        case "two":
            print("The value is two")
        case _:
            print("The value is something else")




if __name__ == "__main__":
    main()
