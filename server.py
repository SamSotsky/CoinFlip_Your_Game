from flask import Flask
from flask_app import app
from flask_app.controllers import champ_controller



if __name__ == "__main__":
    app.run(debug=True)























# import requests
# from flask_app import app
# import os
# from flask import jsonify, render_template
# # @app.route('/searching'):
# #     r = requests.get(f"https:api.information.com/{os.environ.get('FLASK_API_KEY')}")
# #     # we must keep in line with JSON format.
# #     # requests has a method to convert the data coming back into JSON.
# #     return jsonify( r.json() )




# @app.route("/get_champ")
# def get_champ():
#     r = requests.get("http://ddragon.leagueoflegends.com/cdn/12.6.1/data/en_US/champion.json")

#     print(r)
#     return render_template("index.html")
