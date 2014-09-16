import webapp2
import subprocess

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

class Scraper(webapp2.RequestHandler):
    def get(self):
        subprocess.Popen(['./scraper.py'])

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/events', Events)
    ('/scrape', Scraper)
], debug=True)
