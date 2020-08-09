import requests

city = input('Please enter the city name : ')
data = requests.get(
    "https://api.weatherbit.io/v2.0/current?key=119038f9350645269116a8b6565b8239&city="+city).json()

temp = data["data"][0]["temp"]
print(temp)
