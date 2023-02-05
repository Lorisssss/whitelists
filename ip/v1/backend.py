from flask import Flask
import requests
import random
import string 
from flask import request



responses1 = ["NFGJDFTRACTEDADBIAXVWWAHELXWHYDNNJOHYUWJHCSTFHONMK", "VMUIUWVCNXJHDPSJBUECNYPTJMRJOFSYIFRYTLOGJVIHZSWZDF", "HEAWZXCXBHVDRQADRJLAOOOFYAVRRXKCTEIBWJWRWGBJWCSIIV"]
responses2 = ["464646753646444464643745747464564b0fc27ba5568d067d539b852c4243ee438543e1a2e0db8fa6bf53ce008d2ba150", "3434b0fc27ba552334634568d067d539b2c4243ee433e1a2e0db8fa6bf53ce008d2ba150", "88675hfhfh434b0fc76527ba5568d067d539b2c427575743ee433e1a2e0db8fa6b5f53ce008d2ba150", "3434b0fc27747474a5568d067634636d539b2c4243ee433e1a2e0db8fa6bf53ce00g8d2ba150"]

app = Flask(__name__)

@app.route("/whitelist")
def lol():
    return ""

@app.route("/whitelist/getresponse")
def main():
    ips = requests.get("http://nigger.com/buyersipexample.txt")
    ip = request.remote_addr
    if ip in ips.text:
        return ''.join(random.choice(responses1))
    
    else:
        return ''.join(random.choice(responses2))



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
