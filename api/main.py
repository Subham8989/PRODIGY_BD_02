from flask_restful import Resource, reqparse
from uuid import uuid4
import os

from mongoengine import connect
connect(os.getenv("MONGODB_DATABASE_NAME"))

from .models import User
from .utils import email_type

parser = reqparse.RequestParser()
parser.add_argument("name", type=str, required=True, help="Name cannot be empty!")
parser.add_argument("email", type=email_type, required=True, help="Valid email address required!")
parser.add_argument("age", type=int, help="Age must be a number!")

class UserList(Resource):
  def get(self):
    users = User.objects()
    return [user.to_mongo().to_dict() for user in users], 200

  def post(self):
    args = parser.parse_args()
    user_id = str(uuid4())
    user = User(
      _id=user_id,
      name=args["name"],
      email=args["email"],
      age=args["age"]
    )
    user.save()
    return { "_id": user_id, "name": args["name"] }, 201

class UserDetail(Resource):
  def get(self, user_id):
    user = User.objects(_id=user_id).first()
    if not user:
      return { "message": "User not found" }, 404
    return user.to_mongo().to_dict(), 200

  def put(self, user_id):
    args = parser.parse_args()
    user = User.objects(_id=user_id).update(name=args["name"], email=args["email"], age=args["age"])
    if user == 0:
      return { "message": "User not found" }, 404
    return { "message": "User updated", "_id": user_id }, 200
  
  def patch(self, user_id):
    pass

  def delete(self, user_id):
    user = User.objects(_id=user_id).delete()
    if user == 0:
      return { "message": "User not found" }, 404
    return { "message": "User deleted", "_id": user_id }, 202