import nltk
import sys
import re
import numpy as np 
import collections
import sqlite3
import porterstemmer

#############################################################################
# Chatbot						                            				#
#############################################################################

class Chatbot: 
	"""Simple class to implement the chatbot for the NLI."""
	def __init__(self):
		self.name = 'Djinn'
		self.porter_stemmer = PorterStemmer()
		self.determiner_tags = ['WDT', 'WP', 'WRB']
		self.entity_tags = ['NN', 'NNP', 'NNPS', 'NNS']
		self.table_names = []

		###gather set for tables###
		self.column_names = [name.lower() for name in self.retrieve_column_names()]		

		print self.intro()
		print self.greeting()
		
		while True:
			userInput = raw_input(">>> ")		
			if userInput == "":
				print "------Operation done successfully--------";
				sys.exit(0)
			tagged_set = self.pos_extraction(userInput)
			userInputEntity = self.search_for_entities(tagged_set)[0]
			desired_column = self.find_closest_name(userInputEntity, self.column_names)
			print desired_column

		
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

	def retrieve_column_names(self):
		conn = sqlite3.connect('test.db')
		print "------Opened database successfully-------";

		cursor = conn.execute("SELECT * from COMPANY")
		#Get columns
		num_fields = len(cursor.description) 
		field_names = [i[0] for i in cursor.description]
		return field_names
		conn.close()

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

	def dameraulevenshtein(self, seq1, seq2):
	    """Calculate the Damerau-Levenshtein distance between sequences.

	    This distance is the number of additions, deletions, substitutions,
	    and transpositions needed to transform the first sequence into the
	    second. Although generally used with strings, any sequences of
	    comparable objects will work.

	    Transpositions are exchanges of *consecutive* characters; all other
	    operations are self-explanatory.
	    """
	    # Conceptually, this is based on a len(seq1) + 1 * len(seq2) + 1 matrix.
	    # However, only the current and two previous rows are needed at once,
	    # so we only store those.
	    oneago = None
	    thisrow = range(1, len(seq2) + 1) + [0]
	    for x in xrange(len(seq1)):	    	        	        
	        twoago, oneago, thisrow = oneago, thisrow, [0] * len(seq2) + [x + 1]
	        for y in xrange(len(seq2)):
	            delcost = oneago[y] + 1
	            addcost = thisrow[y - 1] + 1
	            subcost = oneago[y - 1] + (seq1[x] != seq2[y])
	            thisrow[y] = min(delcost, addcost, subcost)
	            # This block deals with transpositions
	            if (x > 0 and y > 0 and seq1[x] == seq2[y - 1]
	                and seq1[x-1] == seq2[y] and seq1[x] != seq2[y]):
	                thisrow[y] = min(thisrow[y], twoago[y - 2] + 1)
	    return thisrow[len(seq2) - 1]

	def stem_user_input(self, userInputTokens):
		return [self.porter_stemmer.stem(word) for word in userInputTokens]
	
	def find_closest_name(self, w1, names_list):

		dl_distance_list = [self.dameraulevenshtein(w1[0], w2) for w2 in names_list]
		return names_list[dl_distance_list.index(min(dl_distance_list))]

if __name__ == '__main__':
	Chatbot()

















