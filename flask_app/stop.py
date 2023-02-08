import requests


# Send a SHUTDOWN command to the Flask app
def stop(value=False):
    if value:
        requests.post("http://127.0.0.1:5000/shutdown")
