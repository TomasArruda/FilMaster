from textSplitter import TextSplitter
from textTagger import TextTagger
from dictionaryTagger import DictionaryTagger

class Analyser(object):


	def __init__(self, reviewList, film):
		self.reviewList = reviewList
		self.film = film

	def value_of(selg, sentiment):
		result = 0
		if sentiment == 'pos':
			result = 1
		if sentiment == 'neg':
			result = -1
		return result

	def analyse(self, review):
		splitter = TextSplitter()
		postagger = TextTagger()

		splitted_sentences = splitter.split(review)

		pos_tagged_sentences = postagger.pos_tag(splitted_sentences)

		dicttagger = DictionaryTagger([ 'positive2.yml', 'negative2.yml', 'inc.yml', 'dec.yml', 'inv.yml'])

		dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)
		print dict_tagged_sentences

		result = 0
		for token in dict_tagged_sentences:
			result = result + self.sentence_score(token, None, 0.0)
		
		print result

		return result

	def sentence_score(self, sentence_tokens, previous_token, score):    
		if not sentence_tokens:
			return score
		else:
			current_token = sentence_tokens[0]
			tags = current_token[2]
			token_score = 0
			for tag in tags:
				token_score = token_score + self.value_of(tag)
			if previous_token is not None:
				previous_tags = previous_token[2]
				if 'inc' in previous_tags:
					token_score *= 2.0
				elif 'dec' in previous_tags:
					token_score /= 2.0
				elif 'inv' in previous_tags:
					token_score *= -1.0
			return self.sentence_score(sentence_tokens[1:], current_token, score + token_score)






