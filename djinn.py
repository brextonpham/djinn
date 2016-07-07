import nltk
import sys
import re
import numpy as np 
import collections
import sqlite3
from porterstemmer import PorterStemmer
from nltk.corpus import wordnet as wn
from PyDictionary import PyDictionary
from edit_distance import EditDistance

#############################################################################
# Chatbot						                            				#
#############################################################################

class Chatbot: 
	"""Simple class to implement the chatbot for the NLI."""
	def __init__(self):
		self.conn = sqlite3.connect('djinn_tables_v0.db')
		self.name = 'Djinn'
		self.porter_stemmer = PorterStemmer()
		self.dictionary = PyDictionary()
		self.edit_distance_functions = EditDistance()
		self.determiner_tags = ['WDT', 'WP', 'WRB']
		self.entity_tags = ['NN', 'NNP', 'NNPS', 'NNS', 'CD']
		self.table_names = [self.strip_unicode_prefix(name[0]) for name in self.retrieve_table_names()]

		###have database somewhere that will store synonyms###
		print self.intro()
		print self.greeting()
		
		while True:
			userInput = raw_input(">>> ")		
			if userInput == "":
				print "------Operation done successfully--------";
				sys.exit(0)
			result = "SELECT"

			tagged_set = self.pos_extraction(userInput)
			print tagged_set

			userInputEntity = self.search_for_entities(tagged_set)[0]
			print userInputEntity


			desired_table_name = self.find_closest_name(userInputEntity, self.table_names)
			column_names = [name.lower() for name in self.retrieve_column_names(desired_table_name)]	
			filtrationEntity = self.search_for_entities(tagged_set)[1]
			filterName = self.retrieve_filter_names(filtrationEntity[0], desired_table_name, column_names)
			desired_result_column = self.find_closest_name(userInputEntity, column_names)
			result += " " + desired_result_column  + " from " + desired_table_name
			if filterName is not None: 
				result += " " + "WHERE " + str(filterName) + " = " + str(filtrationEntity[0])
			print result

		self.conn.close()
			
		
	#############################################################################
	# 1. WARM UP REPL 															#
	#############################################################################

	def greeting(self):
		"""Chatbot greeting message"""
		greeting_message = "what do you want to know?"
		return greeting_message

	def goodbye(self):
		"""Chatbot goodbye message"""
		goodbye_message = "have a nice day!"
		return goodbye_message

	def intro(self):
		return "hi there! my name is Djinn! i'm going to try to translate your english to sql!"

	def bot_name(self):
		return self.name

	#############################################################################
	# 2. Extraction and Transformation											#
	#############################################################################

	def retrieve_column_names(self, table_name):
		cursor = self.conn.execute("SELECT * from {}".format(table_name))
		#Get columns
		num_fields = len(cursor.description) 
		field_names = [i[0] for i in cursor.description]

		return field_names

	def retrieve_table_names(self):
		cursor = self.conn.cursor()
		cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
		result = cursor.fetchall()
		return result

	def retrieve_filter_names(self, filtrationEntity, table_name, column_names):
		filter_field = ""
		cursor = self.conn.execute("SELECT * from {}".format(table_name))
		for row in cursor:
			str_row = [str(elem) for elem in row]
			if filtrationEntity in str_row:
				filter_field = column_names[list(str_row).index(filtrationEntity)]
				return filter_field
		return None

	def pos_extraction(self, userInput):
		"""Retrieves the tags of each token in the input string and returns a list of tagged tokens."""		
		text = nltk.word_tokenize(userInput)
		tagged_set = nltk.pos_tag(text)		
		return tagged_set

	def search_for_determiners(self, tagged_set):
		"""Retrieves the determiner tokens in the tagged set."""
		return [tagged_tuple for tagged_tuple in tagged_set if tagged_tuple[1] in self.determiner_tags]

	def search_for_entities(self, tagged_set):
		"""Retrieves the entity tokens in the tagged set."""		
		return [tagged_tuple for tagged_tuple in tagged_set if tagged_tuple[1] in self.entity_tags]

	#############################################################################
	# 3. Additional helper functions							                #
	#############################################################################

	def stem_user_input(self, userInputTokens):
		return [self.porter_stemmer.stem(word) for word in userInputTokens]

	def strip_unicode_prefix(self, word):
		return str(word[:len(word)])

	def find_synonyms(self, word):
		return [self.strip_unicode_prefix(w) for w in self.dictionary.synonym(word)]	
	
	def find_closest_name(self, w1, names_list):
		###need to find hypernyms/hyponyms eventually####
		possible_entity_titles_list = [w1[0]] + self.find_synonyms(w1[0])

		###BRUTE FORCE BE BETTER BREXTON###
		###CONSIDER STEMMING THEN DISTANCE###
		word_with_min_distance = "" 
		min_distance = self.edit_distance_functions.dameraulevenshtein(possible_entity_titles_list[0], names_list[0])

		for word in possible_entity_titles_list:
			for name in names_list:
				distance = self.edit_distance_functions.dameraulevenshtein(word, name)
				if distance <= min_distance:
					word_with_min_distance = name
					min_distance = distance

		return word_with_min_distance

	def is_number(self, s):
	    try:
	        float(s)
	        return True
	    except ValueError:
	        return False

if __name__ == '__main__':
	Chatbot()


















