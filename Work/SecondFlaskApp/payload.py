import requests

url="http://127.0.0.1:5000/signup"

payload={
    "first_name":"ayan",
    "last_name":"maharana",
    "email_id":"sunilweb143@gmail.com",
    "password":"password",
    "confirm_password":"password",
    "phone_no":"9114590459",
    "manager_name":"skm",
}


# """POST"""
response=requests.post(url,data=payload)
if response.status_code==200:
    print(response.text),400

# """PUT"""
response = requests.put(url, data=payload)
print(dir(response))
if response.status_code == 200:
    print(response.json()), 400

 # """PATCH"""
data = {
        'first_name': 'aryan'
    }
response = requests.patch(url, data=data)

if response.status_code == 200:
    print(response.json()),400
