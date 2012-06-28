#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
import time

SIMPLE_TYPES = (int, long, float, bool, dict, basestring, list)

def to_dict(model):
  output = {}

  for key, prop in model.properties().iteritems():
    value = getattr(model, key)

    if value is None or isinstance(value, SIMPLE_TYPES):
      output[key] = value
    elif isinstance(value, datetime.date):
      # Convert date/datetime to ms-since-epoch ("new Date()").
      ms = time.mktime(value.utctimetuple())
      ms += getattr(value, 'microseconds', 0) / 1000
      output[key] = int(ms)
    elif isinstance(value, db.GeoPt):
      output[key] = {'lat': value.lat, 'lon': value.lon}
    elif isinstance(value, db.Model):
      output[key] = to_dict(value)
    else:
      raise ValueError('cannot encode ' + repr(prop))

  return output