import requests

# Extract the session cookie from your provided cookie string
SESSION_COOKIE = "53616c7465645f5f21d949ecc8f0efe1356943db2961550011febc3bfe2aa679775e1eff69560c02fe75de41642e2bc8fffd41742a604c2badb8125db3bce12c"

# Define the URL for the input
url = "https://adventofcode.com/2024/day/9/input"

# Set up headers with the session cookie
headers = {"Cookie": f"session={SESSION_COOKIE}"}

# Make a GET request to fetch the content
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Save the content to a file named input.txt
    with open("input.txt", "w") as file:
        file.write(response.text)
    print("Input successfully saved to input.txt")
else:
    # Print error message if unable to fetch
    print(f"Failed to fetch input. HTTP Status Code: {response.status_code}")
