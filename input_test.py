# -*- coding: utf-8 -*-
import os
os.environ['DJANGO_SETTINGS_MODULE']='settings'
import webapp2 as webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
from testing import testing_parameters

class InpTstPage(webapp.RequestHandler):
    def get(self):
        # text_file2 = open('main_text.txt','r')
        # xx = text_file2.read()
        templatepath = os.path.dirname(__file__) + '/templates/'                     
        html = template.render(templatepath+'01main_header.html', {'title':'hausbrew'})
        html = html + template.render(templatepath+'02main_bodynav.html', {})
        html = html + template.render(templatepath+'03main_bodymenu.html', {})
        html = html + template.render(templatepath+'04model_bodymain.html', {
            'model':'test'})
        html = html + str(testing_parameters.TestInp())
        html = html + template.render(templatepath+'04model_bodyend.html', {})
        html = html + template.render (templatepath+'05main_footer.html', {})
        self.response.out.write(html)

app = webapp.WSGIApplication([
    ('/.*', InpTstPage),
], debug=True)