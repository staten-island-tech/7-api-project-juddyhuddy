# import requests
# url = "https://racinghub.net/api/v1/drivers?page=1&limit=100&order_by=name&sort_by=asc"
# def getf1(f1):
#     response = requests.get(f"https://racinghub.net/api/v1/drivers?page=1&limit=100&order_by=name&sort_by=asc") 
#     data = response.json()
# for driver in data["data"]:
#     print(driver["name"])
# drivers = data["data"]
# rankings = []
# for driver in drivers:
#     rankings.append(driver)
# for i in range(rankings):
#     for a in range(rankings)-1:




import requests

def getf1(f1):
    response = requests.get(f"https://racinghub.net/api/v1/drivers?page=1&limit=100&order_by=name&sort_by=asc")
    if response.status_code != 200:
        print("Error fetching data!")
        return None
    
    data = response.json()
    for driver in data["data"]:
        name = driver["name"]
        championships = driver.get("world_championships")
        print(f"{name} - Championships won: {championships}")
getf1("")