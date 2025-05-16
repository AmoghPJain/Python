import requests

base_url = "https://jsonplaceholder.typicode.com"  # mock API for testing


def test_get():
    """Tests the GET request to retrieve data."""
    print("\nTesting GET request...")
    try:
        response = requests.get(f"{base_url}/posts/1")  # Get a specific post (ID 1)
        response.raise_for_status()  # Raise an exception for bad status codes
        data = response.json()
        print("Response status code:", response.status_code)
        print("Response data:", data)  # Print the retrieved data

    except requests.exceptions.RequestException as e:
        print("Error during GET request:", e)


def test_post():
    """Tests the POST request to create new data."""
    print("\nTesting POST request...")
    new_data = {
        "title": "My New Post",
        "body": "This is the content of my new post.",
        "userId": 1
    }
    print(type(new_data))
    try:
        response = requests.post(f"{base_url}/posts", json=new_data)  # Send the new data as JSON
        response.raise_for_status()
        data = response.json()
        print("Response status code:", response.status_code)
        print("Response data:", data)  # Print the created data (often includes a new ID)
    except requests.exceptions.RequestException as e:
        print("Error during POST request:", e)



def test_put():
    """Tests the PUT request to update existing data."""
    print("\nTesting PUT request...")
    updated_data = {
        "id": 0,  # Important:  The ID of the resource to update
        "title": "Updated Post Title",
        "body": "This is the updated content.",
        "userId": 1
    }
    try:
        response = requests.put(f"{base_url}/posts/1", json=updated_data)  # Update post with ID 1
        response.raise_for_status()
        data = response.json()
        print("Response status code:", response.status_code)
        print("Response data:", data)  # Print the updated data
    except requests.exceptions.RequestException as e:
        print("Error during PUT request:", e)



def test_delete():
    """Tests the DELETE request to remove data."""
    print("\nTesting DELETE request...")
    try:
        response = requests.delete(f"{base_url}/posts/1")  # Delete post with ID 1
        response.raise_for_status()
        print("Response status code:", response.status_code)  #  200 or 204 (No Content) is expected
        # Note:  The mock API often returns the *original* data, not confirmation of deletion.
        #        A real API might return an empty body or a success message.
    except requests.exceptions.RequestException as e:
        print("Error during DELETE request:", e)



if __name__ == "__main__":
    # Run the test functions

    test_get()
    test_post()
    test_put()
    test_delete()


print("\n-----------------------------------------------------\n")

# news api

import requests     # used to get data from APIs
import json     # To parse json data

print(category:=input("Enter the news category you want to read:"))
url = f"https://newsapi.org/v2/everything?q={category}&from=2025-03-26&sortBy=publishedAt&apiKey=67b3017057924f2fb678268e8dfbb2c8"

response=requests.get(url).json()  # to get response from the url and converts the JSON response (from the API) into a Python dictionary for easier manipulation.
print(response)     # response.text returns the imported data from the url

print("\n")

articles=response["articles"]   # articles is an array

for article in articles:
    print("\nTitle:",article["title"])
    print("Description:",article["title"])
