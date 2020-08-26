'''
 Author: Gabriel Vieira Nunes
 Project: facebook brutteforce
'''

from domain.entities.wordparams import WordParams
import itertools
import time
import sys


class PassGen():

	def __init__(self, words, minLength, maxLenght):

		_WP = WordParams(words, minLength, maxLenght)
		self.words = _WP.getWords

		self.minlen = _WP.getMinLength
		self.maxlen = _WP._getMaxLenght
		self.regs = self.maxlen + 1
		self.strsize = len(words)
		self.word = []

	def CountWords(self):

		for chr in range(self.minlen, self.regs):
			index = self.strsize ** chr
			self.word.append(index)
		return sum(self.word)

	def generateWord(self):

		for i in range(self.minlen, self.regs):
			r = i * 100 / self.regs
			l = str(r) + ' percent '
			print("\r%s" % l)

			for passwd in itertools.product(self.words, repeat=i):
				yield(''.join(passwd) + '\n')
