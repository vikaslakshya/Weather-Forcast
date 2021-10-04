import requests
import os

complete_api_link = "https://api.weather.gov/points/39.7456,-97.0892"
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
prop = api_data['properties']['forecastGridData']

complete_api_link1 = prop
api_link1 = requests.get(complete_api_link1)
api_data1 = api_link1.json()

temp = api_data1['properties']['temperature']['values'][0]['value']
print("Tempreture=",temp)
hmdt = api_data1['properties']['relativeHumidity']['values'][0]['value']
print("Humidity=",hmdt)
