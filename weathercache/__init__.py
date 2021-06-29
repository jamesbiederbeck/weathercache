from flask import Flask
import json
import requests
from .secrets import openweatherkey
from datetime import datetime

def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    
    # normally I would put the sqlite db in an instance folder, but 
    # I want to include it in the repo this time.
    # Also, this would be more appropriate in :memory:.
    # Unfortunately I'm also running into an issue with nfs mounts,
    # See https://stackoverflow.com/questions/38673701/new-sqlite3-database-is-locked 
    # so the temperature_cache.db gets copied to /tmp on `vagrant up`, and copied 
    # back on `vagrant destroy`. This should all be opaque to the application.
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=('/tmp/temperature_cache.db'),
    )

    @app.route('/temperature', methods=['GET'])
    def return_temperature():
        """Returns json structure of current temperature like:
            {"query_time":
            <timestamp>, "temperature": <temperature> }
        """
        temperature = fetch_current_weather()
        now = str(datetime.utcnow())
        store_weather_in_db(now, temperature)
        data = {"query_time":now, "temperature":temperature}
        return json.dumps(data)
    
    from weathercache import db
    db.init_app(app)
    from weathercache.db import get_db

    def store_weather_in_db(query_time, temperature):
        """Store a recently retrieved temperature observation in the db"""
        db = get_db()
        db.execute(
            "INSERT INTO temperatures(query_time, temperature) VALUES (?,?)",
            (query_time, temperature)
        )
        db.commit()

    def get_latest_weather_from_db():
        """Gets the most recent entry in the db, returns a 2-tuple with timestamp 
        and temperature measurement, respectively"""
        db = get_db()
        measurement = db.execute("""SELECT query_time, temperature FROM temperatures 
                                    ORDER BY query_time DESC LIMIT 1""").fetchone()
        return measurement['query_time'], measurement['temperature']

    return app

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

def find_timestamp_age_in_minutes(timestampstring):
    """Calculates the age of timestamp, to be used in comparisons"""
    # tell the datetime what the time format is
    timespec = "%Y-%m-%d %H:%M:%S.%f"
    timestamp = datetime.strptime(timestampstring,timespec)
    difference = datetime.utcnow() - timestamp 
    return difference.seconds/60