#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import os
import jinja2
import random
import time
from model import Transaction
#from models import Movie, Person, Company

#remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def get_balance():
    transactions = Transaction.query().fetch() #this is reading the transaction
    #add up the balances
    balance = 0
    for trans in transactions:
        balance += trans.amount
    return balance

class BankingHandler(webapp2.RequestHandler):
    def get(self):
        home_template = jinja_current_directory.get_template("templates/page.html")

        my_dict = {'current_balance' : get_balance()}
        self.response.write(home_template.render(my_dict))

    #def post(self):

class MoneyHandler(webapp2.RequestHandler):
    #def get(self):

    def post(self):
        #global balance
        home_template = jinja_current_directory.get_template("templates/page.html")
        amount_change = int(self.request.get("Amount"))
        transaction = Transaction(amount=amount_change)
        transaction.put()
        time.sleep(1)
        my_dict = {'current_balance': get_balance()}
        self.response.write(home_template.render(my_dict))

# class PersonDataDemoHandler(webapp2.RequestHandler):
#     def get(self):
#
#
#     def post(self):
#
#
# class PersonResult(webapp2.RequestHandler):
#     def post(self):
#
#
# class TestHandler(webapp2.RequestHandler):
#     def get(self):


app = webapp2.WSGIApplication([
    ('/banking', BankingHandler),
    ('/money', MoneyHandler),
    #('/person', PersonDataDemoHandler),
    #('/result', PersonResult),
    #('/test', TestHandler)
], debug=True)
