from secret import *
import requests 

def getAccessToken():
    response = requests.post('https://login.microsoftonline.com/eef05469-0920-48de-ac01-8644774d9cc6/oauth2/v2.0/token', data=getAppCredentials())
    return response.json()["access_token"]

def getTodaysLastRoomEvents():
    headers = {"Authorization": "Bearer "+ getAccessToken()}
    lastRoomEvents = requests.get('https://bm-infosystem.azurewebsites.net/api/rooms/all/last/events', headers=headers)
    return lastRoomEvents.json()

def getNewBrickmakers():
    headers = {"Authorization": "Bearer "+ getAccessToken()}
    newBrickmakers = requests.get('https://bm-infosystem.azurewebsites.net/api/mococontroller', headers=headers)
    return newBrickmakers.json()

def getAllCalenderEvents():
    headers = {"Authorization": "Bearer "+ getAccessToken()}
    newBrickmakers = requests.get('https://bm-infosystem.azurewebsites.net/api/graphcontroller', headers=headers)
    return events.json()
