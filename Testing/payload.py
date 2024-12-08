import requests

url="https://careers.archive360.com/PortalViewRequirement.do?reqGK=27739260"

payload={
    "username":"sunilkumaharana459@gmail.com",
    "passwd":"JK@7874"
}
response=requests.post(url,data=payload)
if response.status_code==200:
    print(response.text,400)