from flask import Flask
from flask_restful import Resource, Api

#from flask_app import app, api
#from DevelopmentBotV_test import create_user

from flask import request

import Development

import json

app = Flask(__name__)
api = Api(app)

@app.after_request
def after_request(response):

    response.headers.set('Access-Control-Allow-Origin', '*')
    response.headers.set('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.set('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    response.headers.set('Access-Control-Allow-Credentials', 'true')

    return response

class HelloWorld(Resource):
    def get(self):
        return Development.test()
    
class List_price_(Resource):
    def get(self):  
        return Development.order_book()

class data_table_(Resource):
    def get(self):  
        return Development.data_table()

class data_table2_(Resource):
    def get(self):  
        data = request.get_json()
        return Development.data_table2(data)

class test_param_(Resource):
    def get(self, player, platfor):  
        # player = request.args.get('player')
        # platfor = request.args.get('platfor')
        # return 'el parametro es {} , {}'. format(player, platfor)
        return Development.data_params(player, platfor)


api.add_resource(HelloWorld, '/test')
api.add_resource(List_price_, '/List_price')
api.add_resource(data_table_, '/data_table')
api.add_resource(data_table2_, '/data_table2')
api.add_resource(test_param_, '/search/<player>/<platfor>') 

#if __name__ == '__main__':
app.run(debug=True)