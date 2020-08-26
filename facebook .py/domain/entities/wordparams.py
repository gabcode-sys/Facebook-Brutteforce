'''
 Author: Gabriel Vieira Nunes
 Project: facebook brutteforce
'''

class WordParams():

    def __init__(self, words, minLength, maxLength):

        self._getWords = (str)(words)
        self._getMinLength = (int)(minLength)
        self._getMaxLenght = (int)(maxLength)

    @property
    def getWords(self):
        return self._getWords

    @property
    def getMinLength(self):
        return self._getMinLength

    @property
    def getMaxLength(self):
        return self._getMaxLength