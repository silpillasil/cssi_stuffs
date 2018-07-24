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

import webapp2
from operator import xor
from google.appengine.api import urlfetch
import json
import urllib
import random


#dict = {'cat': 'https://www.petmd.com/sites/default/files/what-does-it-mean-when-cat-wags-tail.jpg'}

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

class Memes(webapp2.RequestHandler):
    def get(self):
        url = 'https://api.imgflip.com/get_memes'
        self.response.headers['Content-Type'] = 'text/html'
        random_captions = ['dank mems', 'yoooo', 'flusdhfusdfsyyds', 'blub blub']
        x = random.choice(random_captions)

        try:
            result = urlfetch.fetch(url)
            if result.status_code == 200:
                # self.response.write("McIf")
                #self.response.write(result.content)
                json_dict = json.loads(result.content)
                # picture_url = json_dict['data']['memes'][0]['url']
                # picture_id = json_dict['data']['memes'][0]['id']
                random_meme = random.choice(json_dict['data']['memes'])['id']

                # self.response.write('<img src="{pic}"/>'.format(pic=picture_url))
            else:
                #self.response.write("McElse")
                self.response.status_code = result.status_code

        except urlfetch.Error:
            #self.response.write("McExcept")
            logging.exception('Caught exception fetching url')

        caption_url = 'https://api.imgflip.com/caption_image'
        caption_dict = {'template_id': random_meme,
                        'username': 'asil737',
                        'password': 'ponkponk',
                        'text0': random.choice(random_captions),
                        'text1': random.choice(random_captions),
                        # 'text2': 'mem'
                        }

        #result = urlfetch.post(caption_url, data=caption_dict)
        result = urlfetch.fetch(
                url=caption_url,
                payload=urllib.urlencode(caption_dict),
                method=urlfetch.POST,
                #headers=headers
                )
        new_meme_dict = json.loads(result.content)
        picture_url = new_meme_dict['data']['url']
        self.response.write('<img src="{pic}"/>'.format(pic =picture_url))
        # self.response.write(result.content)

app = webapp2.WSGIApplication([
    ('/', Memes),
    #('/save', SavePage),
    ], debug=True)
