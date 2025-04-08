import requests

# URL of the web page
url = 'http://206.189.185.109:8070/flag11-cookie'  # Replace with the URL of the page you're interested in

# Send a GET request to the URL
# response = requests.get(url)

# cookies = dict(cookies_are='working')

response = requests.get(url, 'myinfo'='cosi107a')
# Get the headers of the response
headers = response.headers

# Print the headers
print("HTTP Headers:")
for key, value in headers.items():
    print(f"{key}: {value}")

# Optional: Look for a specific header, e.g., 'X-Flag' (you can change this to the header you're interested in)
flag = headers.get('X-Flag')  # Replace 'X-Flag' with the actual header you're searching for
if flag:
    print(f"\nFound flag: {flag}")
else:
    print("\nFlag not found in headers.")
