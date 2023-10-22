import requests

url = 'http://127.0.0.1:8000/api/contacts/'
headers = {'Authorization': 'Bearer YOUR_USER_TOKEN'}
data = {
    'first_name': 'John',
    'last_name': 'Doe',
    'phone_number': '1234567890'
}

response = requests.post(url, headers=headers, data=data)
