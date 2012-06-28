from google.appengine.ext import webapp
register = webapp.template.create_template_register()

@register.filter
def hash(h, key):
    return h[key]