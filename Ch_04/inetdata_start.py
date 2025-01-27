import requests

def main():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url)  # Send an HTTP GET request to the URL

    if response.status_code == 200:  # Check if the request was successful
        data = response.json()  # Parse the JSON data returned by the server
        print(data)
    else:
        print(f"Error: Unable to retrieve data. Status code: {response.status_code}")

if __name__ == "__main__":
    main()
