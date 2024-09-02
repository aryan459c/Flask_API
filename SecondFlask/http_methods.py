import requests

url="https://reqres.in/api/user?page=2"
response=requests.get(url)
if response.status_code==200:
    data=response.json()
    print(data)


    """POST"""
url = 'https://reqres.in/api/users'

payload = {
    "name": "morpheus",
    "job": "leader"
}


response = requests.post(url,data=payload)

if response.status_code == 201:
    print(response.json())

data =[
    {'Name':'A','Pass':'ABC'},
    {'Name':'B','Pass':'XYZ'}
]

for i in data:
    print(i['Name'])
