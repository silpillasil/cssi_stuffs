"""Meme madness code - uses imgflip api to generate random memes.
This code is written to work on appengine. To see this code run
on local host run the following command on a computer with the
app engine SDK installed:
    dev_appserver.py app.yaml
LICENSE STUFF:
Copyright 2016 Google Inc.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import webapp2
from google.appengine.api import urlfetch
import json
import urllib
import random
import logging # Can you figure out what this does?

class MainPage(webapp2.RequestHandler):
    """Controller for any requests to '/'
    This just gives folks a landing page when they go
    to https://{my_domain}/. This will show 'HAIII' on
    the screen.
    """
    def get(self):
        """Model for GET requests to '/'"""
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('HAII')
        logging.info('Writing "HAII".')

class MemePage(webapp2.RequestHandler):
    """Controller for any requests to '/memes'
    """
    def get(self):
        """Model for GET requests to '/memes'.
        This will get a list of popular memes from
        the imgflip api and chose a random meme. It will
        then select two random quotes from a list of
        quotes and use those two quotes to caption the meme.
        This will then show the captioned meme. If anything
        goes wrong this will output a string with the error
        on the screen.
        """
        self.response.headers['Content-Type'] = 'text/html'

        # Let's make some data we'll use. This is a list of random
        # text strings we'll use to create memes.
        random_text = [
            'This is a meme.',
            'I hate sand.',
            'It is coarse.',
            'ZOMG',
            'Random text.',
            'Herp Derp a Derp',
            'Poop Scoopin Boogie.']

        # These are variables holding the different URLs we'll need.
        # These urls are described in full at:
        #   https://api.imgflip.com/
        get_meme_url = 'https://api.imgflip.com/get_memes'
        caption_url = 'https://api.imgflip.com/caption_image'

        # Ok let's try to get a list of the most popular memes.
        try:
            logging.info('Trying to get the list of popular memes...')
            result = urlfetch.fetch(get_meme_url)
            if result.status_code == 200:
                # Uncomment below to see what the type of result.content is.
                # self.response.write(type(result.content))

                # result.content is a json string, I need to be able to
                # use the data so I'll turn it into a dictionary.
                logging.info('Recieved the following response: {resp}'.format(
                    resp=result.content))
                json_dict = json.loads(result.content)

                # Uncomment below to see what json_dict looks like
                # self.response.write(json_dict)

                # Randomly select one of the memes
                random_meme = random.choice(json_dict['data']['memes'])['id']
                logging.info('Chose the random meme: {id}'.format(
                    id=random_meme))
                # Uncomment below to see whether or not I'm actually
                # getting a image that, like, works.
                # self.response.write('<img src="{pic}"/>'.format(
                #     pic=picture_url))
            else:
                # If I got here I didn't get a good status code
                # that means something went wrong. We'll print out
                # the status code and exit this function early.
                self.response.status_code = result.status_code
                self.response.write(
                    'oWo I got an unexpected status code.'.format(
                        result.status_code))
                return
        except urlfetch.Error as e:
            # If something goes REALLY wrong with our urlfetch.fetch
            # we'll get this error. This will catch the error,
            # display it on the screen and exit the function early.
            self.response.write(
                'Caught exception fetching url: {e}'.format(e=e))
            return

        # This is the data we need to provide to the imgflip api
        # in order to caption our memes. We'll make a dictionary
        # with the required data described by api.imgflip.com
        caption_dict = {
            'template_id': random_meme,
            'username': 'nahkki',
            'password': 'correct_horse_battery',
            'text0': random.choice(random_text),
            'text1': random.choice(random_text),
            }

        # Let's try to caption our meme.
        try:
            logging.info('Trying to caption my meme...')
            result = urlfetch.fetch(
                url=caption_url,
                payload=urllib.urlencode(caption_dict),
                method=urlfetch.POST)
            # self.response.write(result.content)

            logging.info('Recieved the following response: {resp}'.format(
                resp=result.content))
            new_meme_dict = json.loads(result.content)
            picture_url = new_meme_dict['data']['url']
            self.response.write('<img src="{pic}"/>'.format(
                pic=picture_url))
        except Exception as e:
            # I don't know what exceptions might happen
            # so let's just catch all of them for now.
            self.response.write(
                'OH NOES Something went really wrong while '
                'captioning the meme: {e}'.format(e=e))

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/memes', MemePage),
], debug=True)
