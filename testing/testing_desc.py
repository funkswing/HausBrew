import webapp2 as webapp
from google.appengine.ext.webapp import template
import os

class DescTstPage(webapp.RequestHandler):
    def get(self):
        # text_file2 = open('desc_txt.txt','r')
        # xx = text_file2.read()
        # templatepath = os.path.dirname(__file__) + '/../templates/'    
        # html = template.render(templatepath+'01main_header.html', {'title':'hausbrew'})
        # html = html + template.render(templatepath+'02main_bodynav.html', {})
        # html = html + template.render(templatepath+'03main_bodymenu.html', {})
        # html = html + template.render(templatepath+'04model_bodymain.html', {
        #     'text_paragraph':xx})
        # html = html + template.render(templatepath+'04model_bodyend.html', {})
        # html = html + template.render (templatepath+'05main_footer.html', {})
        html = 'WTF?!?!?!'
        self.response.out.write(html)

app = webapp.WSGIApplication([('/.*', DescTstPage)], debug=True)