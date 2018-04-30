from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
#from flask.ext.jsonify import jsonify
from json import dumps

#Create a engine for connecting to SQLite3.
#Assuming movies.db is in your app root folder

e = create_engine('sqlite:///movies.db')
print(e)
app = Flask(__name__)
api = Api(app)

class Actors_Meta(Resource):
    def get(self):
        #Connect to databse
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("select distinct actor_1_name from movies")
        result = {'actors': [i[0] for i in query.cursor.fetchall()]}
        return result

class Movie_Actors(Resource):
    def get(self, actor_name):
        conn = e.connect()
        query = conn.execute("select * from movies where actor_1_name='%s'"%actor_name)
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result
        #We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient

api.add_resource(Movie_Actors, '/actor/<string:actor_name>')
api.add_resource(Actors_Meta, '/actors')

if __name__ == '__main__':
     app.run()
