# Example file for working with date information
# LinkedIn Learning Python course by Joe Marini
import datetime

def main():
    ## DATE OBJECTS
    # Get today's date from the simple today() method from the date class
    today_date = datetime.date.today()
    print("Today's date:", today_date)

    # print out the date's individual components
    print("Year:", today_date.year)
    print("Month:", today_date.month)
    print("Day:", today_date.day)

    # retrieve today's weekday (0=Monday, 6=Sunday)
    print("Weekday (0=Monday, 6=Sunday):", today_date.weekday())

    ## DATETIME OBJECTS
    # Get today's date from the datetime class
    current_datetime = datetime.datetime.today()
    print("Today's datetime:", current_datetime)

    # Get the current time
    current_time = datetime.datetime.now().time()
    print("Current time:", current_time)

if __name__ == "__main__":
    main()
