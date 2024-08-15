import requests

api_key = 'c6eec94a2acbd6a2c4d675ea32575373'

user_input = input("Enter City:")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    condition = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    humidity = round(weather_data.json()['main']['humidity'])
    
    print(f"The condition in {user_input} is: {condition}")
    print(f"The temperature in {user_input} is: {temp}°F")
    print(f"The humidity in {user_input} is: {humidity}%")
