import requests as req

# make account at https://openweathermap.org or use my key : a14f1bb6b9103f4e98a0e84d5a389778
API = input("API KEY : ")
City = input("Type City : ")

URL = f"https://api.openweathermap.org/data/2.5/weather?q={City}&APPID={API}"

response = req.get(URL).json()
