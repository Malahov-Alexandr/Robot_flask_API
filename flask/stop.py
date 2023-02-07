import requests

# Send a SHUTDOWN command to the Flask app
requests.post("http://127.0.0.1:5000/shutdown")