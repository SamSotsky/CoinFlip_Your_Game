import requests, random
from flask_app import app
import os
from flask import jsonify, render_template
# @app.route('/searching'):
#     r = requests.get(f"https:api.information.com/{os.environ.get('FLASK_API_KEY')}")
#     # we must keep in line with JSON format.
#     # requests has a method to convert the data coming back into JSON.
#     return jsonify( r.json() )


# @app.route("/")
# def home():
#     return render_template("home.html")

@app.route("/")
def get_champ():
    r = requests.get("http://ddragon.leagueoflegends.com/cdn/12.6.1/data/en_US/champion.json")
    temp = r.json()
    raw = temp["data"]
    champs = []
    for val in raw.values():
        champs.append(val)
    rand_champ = champs[random.randint(0,len(champs)-1)]
    print (rand_champ)
    return render_template("home.html",rand_champ = rand_champ)


# random.randint(a,b) returns random int between a and b included

# data["aatrox"]["image"]["full"]


# import random
# print (random.randint(1,5))


