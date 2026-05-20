import requests
url = "https://racinghub.net/api/v1/drivers?page=1&limit=100&order_by=name&sort_by=asc"
def getf1(f1):
    response = requests.get(f"https://racinghub.net/api/v1/drivers?page=1&limit=100&order_by=name&sort_by=asc") 
    data = response.json()
for driver in data["data"]:
    print(driver["name"])
