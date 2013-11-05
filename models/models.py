import os
os.environ['DJANGO_SETTINGS_MODULE']='settings'
import webapp2 as webapp
from google.appengine.ext.webapp.util import run_wsgi_app




class Calcs(object):
	def __init__(self, tempC, tempF):
		self.tempC = tempC
		self.tempF = tempF

		self.run_calc()

	def run_calc(self):
		self.F2C_f()

	def C2F_f(self):
		self.tempF = self.tempC * (9/5) + 32
		return self.tempF

	def F2C_f(self):
		self.C = (self.tempF - 32) * (5/9)
		return self.C

	