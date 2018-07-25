from google.appengine.ext import ndb

class Transaction(ndb.Model):
    amount = ndb.IntegerProperty(required=True)
