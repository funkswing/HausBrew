import webapp2 as webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import os

class MashDescPage(webapp.RequestHandler):
	def get(self):
		txt = open('mash/mash_desc.txt','r')
		x = txt.read()
		templatepath = os.path.dirname(__file__) + '/../templates/'
		html = template.render(templatepath + '01main_header.html', {})
		html = html + template.render(templatepath + '02main_bodynav.html', {})
		html = html + template.render(templatepath + '03main_bodymenu.html', {})
		html = html + template.render(templatepath + '04main_bodymain.html', {
			'model':'main',
			'txt':x})
		html = html + template.render(templatepath + '05main_footer.html', {})
		self.response.out.write(html)

app = webapp.WSGIApplication([
    ('/*', MashDescPage),
], debug=True)