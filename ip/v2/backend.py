from flask import *
import random, string 
import requests


app = Flask(__name__)

@app.route("/whitelist")
def lol():
    return ""

@app.route("/whitelist/auth")
def main():
    ips = requests.get("http://nigger.com/ips.txt")
    ip = request.remote_addr
    if ip in ips.text:
         return ("".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)for _ in range(78))), 200
    
    else:
          return ("".join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits)for _ in range(78))), 404


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
