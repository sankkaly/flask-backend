from flask import Flask, jsonify
from pymongo import MongoClient
import json
import os
from dotenv import load_dotenv

load_dotenv()
client = os.getenv("DB_URI")

def connect_db(db_client:str):
    try:
        mongo_client = MongoClient(db_client)
        if mongo_client:
            print("connected to database")
        return mongo_client
    except Exception as e:
        raise Exception("Unable connect to database, encountered following error: ", e)


db = connect_db(client)
database = db.get_database('sample_mflix')
movies = database.get_collection("movies")
movie =  movies.find_one({"title":"Back to the Future"})
print(json.dumps(movie, indent=4, default=str))

app = Flask(__name__)

if __name__ == "__main__" :
    app.run(debug=True)



# try:
#     database = client.get_database('sample_mflix')
#     movies = database.get_collection("movies")


#     query =  {"title": "Back to the Future"}
#     movie = movies.find_one(query)

#     print(json.dumps(movie, indent=4, default=str))

#     client.close
# except Exception as e:
#     raise Exception("unable to find the document due to following error: ", e)



# @app.route('/')
# def home():
#     return jsonify(
#         {"message":"This is Home Page"}
#         )

# @app.route('/settings')
# def settings():
#     return jsonify(
#         {"message":"This is settings page"}
#     )

# @app.route('/login')
# def login():
#     return jsonify(
#         {"message":"This is login page"}
#     )

# @app.route('/dashboard')
# def dashboard():
#     return jsonify(
#         {"Message":"This are the dashboards"}
#     )

