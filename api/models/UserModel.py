from mongoengine import Document, StringField, IntField, EmailField, UUIDField
import uuid


class User(Document):
  _id = UUIDField(primary_key=True, default=uuid.uuid4, binary=False)
  name = StringField(required=True, max_length=50, min_length=1)
  email = EmailField(required=True, unique=True)
  age = IntField(min_value=0)