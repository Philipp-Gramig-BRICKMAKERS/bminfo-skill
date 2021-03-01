import requests 

test = {
    'client_id': '45eb78f8-4b7f-4edb-ac48-59fd0898e64c',
    'scope': 'https://graph.microsoft.com/.default',
    'client_secret': 'JtMm.3_KTb0.0DCc77tqlup7qs9cHp1o.J',
    'grant_type': 'client_credentials',
}
    
response = requests.post('https://login.microsoftonline.com/eef05469-0920-48de-ac01-8644774d9cc6/oauth2/v2.0/token', data=test)
print(response.json()["access_token"])

headers = {"Authorization": "Bearer "+ response.json()["access_token"]}

allRooms = requests.get('https://bm-infosystem.azurewebsites.net/api/rooms', headers=headers)
print(allRooms.json())