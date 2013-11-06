import webapp2 as webapp
# from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template
import os

class InpTstPage(webapp.RequestHandler):
    def get(self):
        # text_file2 = open('Inp_txt.txt','r')
        # xx = text_file2.read()
        # templatepath = os.path.dirname(__file__) + '/../templates/'    
        # html = template.render(templatepath+'01main_header.html', {'title':'hausbrew'})
        # html = html + template.render(templatepath+'02main_bodynav.html', {})
        # html = html + template.render(templatepath+'03main_bodymenu.html', {})
        # html = html + template.render(templatepath+'04model_bodymain.html', {
        #     'text_paragraph':xx})
        # html = html + template.render(templatepath+'04model_bodyend.html', {})
        # html = html + template.render (templatepath+'05main_footer.html', {})
        html = """
        <html>
        <head>
        <link rel="stylesheet" href="style/style.css" />
        <link rel="SHORTCUT ICON" href="/images/favicon.ico" />
        </head>
        <body>Input page</body>
        </html>"""
        self.response.out.write(html)

app = webapp.WSGIApplication([('/testing.*', InpTstPage),], debug=True)