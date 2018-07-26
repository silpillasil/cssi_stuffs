import webapp2

class HelloWorld(webapp2.RequestHandler):
    def get(self):
        self.response.write("Welcome to Aishani's stuff")


app = webapp2.WSGIApplication([
    ('/hello', HelloWorld),
], debug=True)
