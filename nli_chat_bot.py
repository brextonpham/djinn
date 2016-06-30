import nltk
import sys
import re
import numpy as np 
import collections

class Chatbot: 
	"""Simple class to implement the chatbot for the NLI"""
	def __init__(self):
		self.name = 'Djinn'
		print self.intro()
		print self.greeting()


	#############################################################################
	# WARM UP REPL 																#
	#############################################################################

	def greeting(self):
		"""chatbot greeting message"""
		greeting_message = "what do you want to know?"
		return greeting_message

	def goodbye(self):
		"""chatbot goodbye message"""
		goodbye_message = "have a nice day!"
		return goodbye_message

	def intro(self):
		return "hi there! my name is Djinn! i'm going to try to translate your english to sql!"

	def bot_name(self):
		return self.name

if __name__ == '__main__':
	Chatbot()