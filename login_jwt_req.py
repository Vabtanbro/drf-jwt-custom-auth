import requests

url = 'http://localhost:8000/api/login/'
data = {'email': 'user@example.com', 'password': 'password'}
headers = {'Content-Type': 'application/json'}

response = requests.post(url, json=data, headers=headers)
if response.status_code == 200:
    # Login successful
    token = response.json()['token']
    user = response.json()['user']
else:
    # Login failed
    error = response.json()['error']
