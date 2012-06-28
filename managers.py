import logging
import datetime
from libs import oauth
import settings
from google.appengine.api import urlfetch

from models import *

def make_key(id):
  return '__twitter_%s' % str(id)