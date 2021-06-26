from flask import Flask
import json
import requests
from secrets import openweatherkey
from datetime import datetime

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/temperature', methods=['GET'])
def return_temperature():
    """Returns json structure of current temperature like:
        {"query_time":
        <timestamp>, "temperature": <temperature> }
    """
    temperature = fetch_current_weather()
    data = {"query_time":str(datetime.utcnow()) , "temperature":temperature}
    return json.dumps(data)

def fetch_current_weather(city="portland"):
    """Returns temperature
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    payload = {
        'q':city, #this is the city parameter
        'appid':openweatherkey,
        'units':"imperial"
    }
    r = requests.get(url, params=payload)
    temperature = r.json()['main']['temp']
    return temperature
    
if __name__ == "__main__":
    app.run()

