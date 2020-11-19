##--- necesary imports ---##

from flask import Flask
from flask_restful import Resource, Api, reqparse


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
parser = reqparse.RequestParser()

class PeopleList(Resource):
    def get(self):
        return PEOPLE

    def post(self):
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

class Person(Resource):
    '''
    CRUD operations for each person in PEOPLE class
    '''
    def get(self, person_id):
        if person_id not in PEOPLE:
            return "Not found", 404
        else:
            return PEOPLE[person_id]

    def put(self, person_id):
        parser.add_argument('name')
        parser.add_argument('age')
        parser.add_argument('favorite_wine')
        args = parser.parse_args()
        if person_id not in PEOPLE:
            return "Not found", 404
        else:
            person = PEOPLE[person_id]
            person['name'] = args['name'] if args['name'] != None else person['name']
            person['age'] = args['age'] if args['age'] != None else person['age']
            person['favorite_wine'] = args['favorite_wine'] if args['favorite_wine'] != None else person['favorite_wine']
            return person, 200

    def delete(self, person_id):
        if person_id not in PEOPLE:
            return "Not found", 404
        else:
            del PEOPLE[person_id]
            return '', 204


##--- route(s) ---##

api.add_resource(PeopleList, '/people/')
api.add_resource(Person, '/people/<person_id>')


##--- run app in debug mode ---##

if __name__ == "__main__":
    app.run(debug=True)