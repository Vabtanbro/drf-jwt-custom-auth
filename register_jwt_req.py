import requests

url = 'http://localhost:8000/api/register/'
data = {
    'email': 'user@example.com',
    'password': 'password',
    'first_name': 'John',
    'last_name': 'Doe'
}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)
if response.status_code == 201:
    # Registration successful
    user = response.json()
else:
    # Registration failed
    errors = response.json()
