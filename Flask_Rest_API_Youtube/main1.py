from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

if name == '__main__':
    app.run(debug=True)
