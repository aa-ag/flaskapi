##--- necesary imports ---##

from flask import Flask
from flask_restful import Resource, Api, reqparse

##--- Global ---##
parser = reqparse.RequestParser()


##--- init API ---##
app = Flask(__name__)
api = Api(app)


##--- mock data ---##
PEOPLE = {
    '1': {'name': 'a', 'age': 1, 'favorite_wine': 'red'},
    '2': {'name': 'b', 'age': 2, 'favorite_wine': 'white'},
    '3': {'name': 'c', 'age': 3, 'favorite_wine': 'pink'},
    '4': {'name': 'd', 'age': 4, 'favorite_wine': 'red'},
    '5': {'name': 'e', 'age': 5, 'favorite_wine': 'red'},
}


##--- class(es) ---##

class PeopleList(Resource):
    def get(self):
        return PEOPLE

    def post(self):
        global parser
        parser.add_argument('name')
        parser.add_argument('age')
        parser.add_argument('favorite_wine')
        args = parser.parse_args()
        person_id = int(max(PEOPLE.keys())) + 1
        person_id = '%i' % person_id
        PEOPLE[person_id] = {
            'name': args['name'],
            'age': args['age'],
            'favorite_wine': args['favorite_wine'],
        }
        return PEOPLE[person_id], 201


##--- route(s) ---##

api.add_resource(PeopleList, '/people/')

##--- run app in debug mode ---##

if __name__ == "__main__":
    app.run(debug=True)