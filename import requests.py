import requests

def getdisney(disney):
    response = requests.get(f"https://api.disneyapi.dev/character") 