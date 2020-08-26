'''
 Author: Gabriel Vieira Nunes
 Project: facebook brutteforce
'''

class Url():

	def __init__(self, url, loggedin_title):

		self._getUrl = url
		self._getLoggedin_Title = loggedin_title

	@property
	def getUrl(self):
		return self._getUrl
	
	@property
	def getLoggedin_Title(self):
		return self._getLoggedin_Title