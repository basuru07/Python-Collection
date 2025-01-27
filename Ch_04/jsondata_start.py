import urllib.request
import json

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)
    
    # Now we can access the contents of the JSON like any other Python object
    events = theJSON['features']

    # Output the number of events, plus the magnitude and each event name
    print(f"Number of events: {len(events)}\n")
    
    for event in events:
        # Get the magnitude and place of each event
        magnitude = event['properties']['mag']
        place = event['properties']['place']
        print(f"Event: {place}, Magnitude: {magnitude}")

        # Print the events that only have a magnitude greater than 4
        if magnitude > 4:
            print(f"  Magnitude > 4: {place}, Magnitude: {magnitude}")
        
        # Print only the events where at least 1 person reported feeling something
        felt_reports = event['properties']['felt']
        if felt_reports and felt_reports > 0:
            print(f"  Felt by {felt_reports} people: {place}, Magnitude: {magnitude}")

def main():
    # Define a variable to hold the source URL
    # In this case, we'll use the free data feed from the USGS
    urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

    # Open the URL and read the data
    with urllib.request.urlopen(urlData) as webUrl:
        data = webUrl.read().decode('utf-8')
        print(f"Result code: {webUrl.getcode()}")

        # Now print the results
        printResults(data)

if __name__ == "__main__":
    main()
