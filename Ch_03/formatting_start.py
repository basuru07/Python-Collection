from datetime import datetime

def main():
    # Get current date and time
    now = datetime.now()

    #### Date Formatting ####
    # Format the date in different ways
    print("Current year (short):", now.strftime("%y"))
    print("Current year (full):", now.strftime("%Y"))
    print("Current weekday (abbreviated):", now.strftime("%a"))
    print("Current weekday (full):", now.strftime("%A"))
    print("Current month (abbreviated):", now.strftime("%b"))
    print("Current month (full):", now.strftime("%B"))
    print("Day of the month:", now.strftime("%d"))
    print("Current date and time (locale):", now.strftime("%c"))
    print("Current date (locale):", now.strftime("%x"))
    print("Current time (locale):", now.strftime("%X"))

    #### Time Formatting ####
    # Format the time in different ways
    print("12-hour format (HH:MM:SS AM/PM):", now.strftime("%I:%M:%S %p"))
    print("24-hour format (HH:MM:SS):", now.strftime("%H:%M:%S"))
    print("Minutes:", now.strftime("%M"))
    print("Seconds:", now.strftime("%S"))

if __name__ == "__main__":
    main()
