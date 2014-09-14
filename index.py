import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        html = open("index.html", 'r').read()
        self.response.headers['Content-Type'] = 'text/html'
        self.response.write(html)

class Events(webapp2.RequestHandler):
    def get(self):
        json = open('events.json', 'r').read()
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/events', Events)
], debug=True)
