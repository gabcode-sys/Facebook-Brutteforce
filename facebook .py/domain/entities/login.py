'''
 Author: Gabriel Vieira Nunes
 Project: facebook brutteforce
'''

class Login():

	def __init__(self, email, password):

		self._email = email
		self._pass = password

	@property
	def getEmail(self):
		return self._email

	@property
	def getPassword(self):
		return self._pass

