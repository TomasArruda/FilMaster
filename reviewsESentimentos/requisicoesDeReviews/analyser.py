from __future__ import division
from textSplitter import TextSplitter
from textTagger import TextTagger
from dictionaryTagger import DictionaryTagger
from nltk.tag.perceptron import PerceptronTagger
import cProfile
import pstats


class Result(object):
	def __init__(self, positive, negative, neutral):
		self.total = positive + negative + neutral
		self.positive = (positive/self.total)*100
		self.negative = (negative/self.total)*100
		self.neutral = (neutral/self.total)*100


class Analyser(object):

	def __init__(self, reviewList, film):
		self.reviewList = reviewList
		self.film = film
		self.tagger = PerceptronTagger()

	def value_of(selg, sentiment):
		result = 0
		if sentiment == 'pos':
			result = 1
		if sentiment == 'neg':
			result = -1
		return result


	def analyse(self, reviews):

		splitter = TextSplitter()
		postagger = TextTagger()
		countPositive = 0
		countNegative = 0
		countNeutral = 0

		for review in reviews:

			splitted_sentences = splitter.split(review)

			pos_tagged_sentences = postagger.pos_tag(splitted_sentences, self.tagger)

			dicttagger = DictionaryTagger([ 'requisicoesDeReviews/positive2.yml', 'requisicoesDeReviews/negative2.yml', 'requisicoesDeReviews/inc.yml', 'requisicoesDeReviews/dec.yml', 'requisicoesDeReviews/inv.yml'])

			dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)

			result = 0
			for token in dict_tagged_sentences:
				result = result + self.sentence_score(token, None, 0.0)

			print result

			if result < 0:
				countNegative = countNegative+1
			elif result > 0:
				countPositive = countPositive+1
			else:
				countNeutral = countNeutral+1

		countResult = Result(countPositive, countNegative, countNeutral);

		print countResult.total
		print countResult.positive
		print countResult.negative
		print countResult.neutral

		return countResult

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






