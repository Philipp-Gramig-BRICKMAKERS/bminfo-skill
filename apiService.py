from .secret import *
import requests 

def getAccessToken():
    response = requests.post('https://login.microsoftonline.com/' + getDirectoryId() + '/oauth2/v2.0/token', data=getAppCredentials())
    return response.json()["access_token"]

def getTodaysLastRoomEvents():
    headers = {"Authorization": "Bearer "+ getAccessToken()}
    allRooms = requests.get('https://bm-infosystem.azurewebsites.net/api/Obot/rooms', headers=headers).json()
    allLastRoomEvents = []

    for room in allRooms:
        events = requests.get('https://bm-infosystem.azurewebsites.net/api/Obot/rooms/' + room['uid'] + '/events', headers=headers).json()
        formattedRoomEvent = {}
        formattedRoomEvent['roomName'] = room['displayName']
        if(len(events) > 0):
            formattedRoomEvent['eventEndTime'] = events[0]['end']
        else:
            formattedRoomEvent['eventEndTime'] = 0    
        allLastRoomEvents.append(formattedRoomEvent)
    return allLastRoomEvents
    

def getNewBrickmakers():
    headers = {"Authorization": "Bearer "+ getAccessToken()}
    newBrickmakers = requests.get('https://bm-infosystem.azurewebsites.net/api/Moco', headers=headers)
    return newBrickmakers.json()

def getAllCalenderEventsForThisWeek():
    headers = {"Authorization": "Bearer "+ getAccessToken()}
    newBrickmakers = requests.get('https://bm-infosystem.azurewebsites.net/api/Graph', headers=headers)
    return events.json()
