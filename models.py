from google.appengine.ext import db
from managers import *

class BaseModel(db.Model):
  created = db.DateTimeProperty(auto_now_add=True)

class UserProfile(BaseModel):
  guser = db.UserProperty()