from twilio.rest import Client
import requests
api_key = "5834ff9be4fec942a28238cdd2d19f36"

from twilio.rest import Client

account_sid = "accountsid"
auth_token = "my token"



weather_params = {
    "lat": 39.7459,
    "lon": -75.5466,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
response.raise_for_status()

data = response.json()
hourly = data["hourly"][:12]

will_rain = False

for weather in hourly:
    condition_code = int(weather["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(body = "Bring Your Umbrella", from_ = "+18126252966", to = "my number")

    print(message.status)



