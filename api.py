import flask
import json
import requests
from secrets import openweatherkey

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/temperature', methods=['GET'])
def return_temperature():
    """Returns json structure of current temperature like:
        {"query_time":
        <timestamp>, "temperature": <temperature> }
    """
    
    data = {"query_time":1624654669, "temperature":88.14}
    return json.dumps(data)

if __name__ == "__main__":
    app.run()

