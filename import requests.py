import requests


def getf1(f1):
    response = requests.get(f"https://racinghub.net/api/v1/drivers?page=1&limit=100&order_by=name&sort_by=asc") 
    if response.status_code != 200:
        print('Error fetching data')
        return None
    
    total_championships = 0

    data = response.json()
    for driver in data["data"]:
        name = driver["name"]
        championships = driver.get("world_championship", 0)
        print(name)
        print(championships)
        total_championships += championships
        drivers.append([name, championships])
    print(total_championships)
print("drivers with 0 championships:")
drivers = []
for driver in drivers:
    if driver[1] == 0:
        print (driver[0])