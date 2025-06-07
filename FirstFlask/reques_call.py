import requests


payload={'title':'abnfhgc','body':'abhjguc'}

response=requests.post("http://127.0.0.1:5000/post",json=payload)