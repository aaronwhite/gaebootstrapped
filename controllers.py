import os
import sys
import wsgiref.handlers
import logging
import datetime
import urllib2

import settings

from google.appengine.ext import db
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

from simplejson import dumps

from libs.lilcookies import *
from libs import oauth

from utils import *
from managers import *

template.register_template_library('filters')

def require_login(func):
  def validate(self, *args):
    user = users.get_current_user()
    if user is None:
      self.redirect(self.get_login_url())
      return
    else:
      self.set_current_user(get_or_create_user(user))
      self.user = get_or_create_user(user)
      func(self, *args)
        
  return validate

class BaseHandler(webapp.RequestHandler):
  def get_login_url(self):
    return users.create_login_url(self.request.uri)
  
  def get_logout_url(self):
    return users.create_logout_url("/")

  def set_current_user(self, user):
    self.user = user  

  def render(self, template_file, template_vars=None):
    if template_vars is None:
      template_vars = {}

    if hasattr(self, 'user'):
      template_vars['current_user'] = self.user

    template_vars['debug'] = settings.DEBUG == True
    template_vars['host'] = settings.get_host()

    template_vars['login_url'] = self.get_login_url()
    template_vars['logout_url'] = self.get_logout_url()

    path = os.path.join(os.path.dirname(__file__), "views", template_file)
    self.response.out.write(template.render(path, template_vars))

class Index(BaseHandler):
  def get(self):
    self.render('index.html', {})

class Dashboard(BaseHandler):
  @require_login
  def get(self):
    self.render('dashboard.html', {})

class LoginHandler(BaseHandler):
  
  def get(self):
    auth_token = self.request.get("oauth_token")
    auth_verifier = self.request.get("oauth_verifier")
    
    user_info = settings.twitter_client.get_user_info(auth_token, auth_verifier=auth_verifier)
    user = create_user(
      user_info.get('id'),
      user_info.get('username'),
      user_info.get('name'),
      user_info.get('picture'),
      user_info.get('token'),
      user_info.get('secret')
    )
    cookieutil = LilCookies(self, settings.SECURE_COOKIE)
    cookieutil.set_secure_cookie(name = '_wda', value = str(user.twitter_id), expires_days= 365)

    pending_pledge = cookieutil.get_secure_cookie('pending_pledge')
    if pending_pledge:
      pc = PledgeFavor()
      pc.initialize(self.request, self.response)
      pc.post(pending_pledge, user)
    else:
      self.redirect('/dashboard')

def main():
  application = webapp.WSGIApplication([

    #nav
    ('/', Index),
    ('/dashboard', Dashboard),
    
    #oauth
    ('/oauth/verify', LoginHandler)
  ], debug=settings.DEBUG)
  util.run_wsgi_app(application)

if __name__ == '__main__':
  main()