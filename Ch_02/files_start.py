# Read and write files using the built-in Python file methods
# LinkedIn Learning Python course by Joe Marini

def main():  
    # Open a file for writing and create it if it doesn't exist
    with open("example.txt", "w") as file:
        # write some lines of data to the file
        file.write("Hello, world!\n")
        file.write("Python is awesome!\n")
    
    # Open the file for appending text to the end
    with open("example.txt", "a") as file:
        file.write("Appended text!\n")
    
    # Open the file back up and read the contents
    with open("example.txt", "r") as file:
        content = file.read()
        print(content)

if __name__ == "__main__":
    main()
