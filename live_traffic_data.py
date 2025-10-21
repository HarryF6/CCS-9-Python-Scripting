import requests


# Define the API URL for live traffic data in Los Angeles

url_api = 'https://api.tomtom.com/traffic/services/4/flowSegmentData/relative0/10/json?key=YOUR_API_KEY&point=LAT,LON'

usa_req = requests.get(url_api)

usa_json = usa_req.json()


# Output the data to verify the API response 

print(usa_json)