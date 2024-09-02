import requests
url = 'https://127.0.0.1:5000/signup'

pload = {
    "first_name":"Sunil",
    "last_name":"Maharana",
    "email_id":"sunilkumaharana@gmail.com",
    "manager_name":"skm",
    "password":"password",
    "confirm_password":"password",
    "phone_no":"8900078456"
}
response = requests.post(url,data=pload)

if response.status_code==201:
    data=response.json()
    print(data)