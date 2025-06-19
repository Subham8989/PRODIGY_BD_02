from flask import Flask
from flask_restful import Api


from .main import UserDetail, UserList


app = Flask(__name__)
api = Api(app)

api.add_resource(UserList, "/api/users", endpoint="userlist", strict_slashes=False)
api.add_resource(UserDetail, "/api/users/<string:user_id>", endpoint="users", strict_slashes=False)
