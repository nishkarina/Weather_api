import requests #this will request for us


API_KEY = "4bcbkjhfldsf57f654fs57df6s4dfsd"     #this is randomly generated key make sure to add yours and do not use this
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"        #make sure to change the base_url accordingly

city = input("Enter the city name: ")

request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"        #you can add different parameters here
response = requests.get(request_url)        # using request module to get request_url and stored that into a response variable

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(f"The description of the weather is {weather}")
    temperature = round(data['main']['temp'] - 273.15)
    print(f"Temperature in celcius is {temperature}")
else:
    print('An error occurred.')
