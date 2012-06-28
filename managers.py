import logging
import datetime
from libs import oauth
import settings
from google.appengine.api import urlfetch

from models import *

def get_user(id):  
  return UserProfile.get_by_id(id)

def get_or_create_user(guser):
  user = UserProfile.all().filter('guser', guser).get()
  if user is None: 
    user = UserProfile(guser=guser)
    user.put()

  return user