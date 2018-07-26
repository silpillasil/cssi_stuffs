# Copyright 2016 Google Inc.
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
"""
This is the same meme code, but using templates. There are comments describing
what I did in each step so that I can know what's going on months down the
line and also maybe to vent my frustration. Because templates fucking suck.
"""

import webapp2
from operator import xor
from google.appengine.api import urlfetch
import json
import urllib
import random
import logging #logs stuff to the command line
import jinja2


template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader=template_loader)

""" random inactive code """
# class MainPage(webapp2.RequestHandler):
#     def get(self):
#         number = self.request.get('number')
#         self.response.headers['Content-Type'] = 'text/plain'
#         # txt = "Result: "
#         self.response.write('Helloooo')

# class SavePage(webapp2.RequestHandler):
#     def get(self):
#         self.response.headers['Content-Type'] = 'text/plain'
#         self.response.write('saved')

""" let's get down to business """

class Memes(webapp2.RequestHandler):
    def post(self): #changed from a get to a post to communicate w html file

        try:
            ssn1 = int(self.request.get('a'))
            ssn2 = int(self.request.get('b'))
            ssn3 = int(self.request.get('c'))
        except:
            self.response.write("Invalid social security number. Please go back, refresh, and try again.")
            return

        if not ((ssn1 >= 100 and ssn1 <= 999) and (ssn2 >= 00 and ssn2 <= 99) and (ssn3 >= 1000 and ssn3 <= 9999)):
            self.response.write("Invalid social security number. Please go back, refresh, and try again.")
            return


        url = 'https://api.imgflip.com/get_memes'
        self.response.headers['Content-Type'] = 'text/html'
        template = template_env.get_template('templates/meme_result.html') #imports template

        try:
            result = urlfetch.fetch(url)
            if result.status_code == 200: #200 means good job! you didn't fuck up
                json_dict = json.loads(result.content)
                random_meme = random.choice(json_dict['data']['memes'])['id']
            else:
                self.response.status_code = result.status_code

        except urlfetch.Error:
            logging.exception('Caught exception fetching url')

#""" this stuff the api just told you to do vvv """


        caption_url = 'https://api.imgflip.com/caption_image'
        caption_dict = {'template_id': random_meme,
                        'username': 'asil737',
                        'password': 'ponkponk',
                        'text0': self.request.get('user-first-ln'),
                        'text1': self.request.get('user-second-ln'),
                        # 'text2': 'mem'
                        }
# """ the text0 and text1 are replaced so that you're getting whatever you
# entered into the form on the first page. That you do by self.request.get
# to the NAME of the object or whatever. """

        #result = urlfetch.post(caption_url, data=caption_dict)
        result = urlfetch.fetch(
                url=caption_url,
                payload=urllib.urlencode(caption_dict),
                method=urlfetch.POST,
                #headers=headers
                )
        new_meme_dict = json.loads(result.content) #this is changing a string to dict

        picture_url = new_meme_dict['data']['url']

        pic_dict = {"chosen_image": picture_url} #this maps the

        self.response.write(template.render(pic_dict))


class MemeTemp(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/home.html')
        self.response.write(template.render())

class MemeTempRes(webapp2.RequestHandler):
    def post(self):
        template = template_env.get_template('templates/meme_result.html')
        top_text = self.request.get('user-first-ln')
        botton_text = self.request.get('user-second-ln')
        meme_type = self.request.get('meme_type')

        data_dict = {'user_first_ln':top_text, "meme_type":meme_type}
        #capt_dict = {}
        #text_dict = {}
        #self.response.write("my post handler = {x}<br>".format(x=meme_type))
        #self.response.write("first line: {y}<br>".format(y=self.request.get('user-first-ln')))
        #self.response.write("second line: {z}".format(z=self.request.get('user-second-ln')))
        #self.response.write(template.render(data_dict))
        # self.response.write(template.render(capt_dict))


class RecipeBrowser(webapp2.RequestHandler):
    def get(self):
        template = template_env.get_template('templates/recipes.html')
        recipe = {'ingredients': ['cheese', 'rice', 'bread']}
        ingredients = recipe['ingredients']
        # cuisine = "american"
        self.response.write(template.render(recipe))

app = webapp2.WSGIApplication([
    ('/memes', Memes),
    ('/recipe', RecipeBrowser),
    ('/', MemeTemp),
    ('/meme_result', MemeTempRes)
    #('/save', SavePage),
    ], debug=True)
