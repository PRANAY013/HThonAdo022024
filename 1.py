#text reader from pdf file

from PyPDF2 import PdfReader

#reader = PdfReader('dummyPDF.pdf')
#reader1 = PdfReader('tablePDF.pdf')
reader1 = PdfReader('random.pdf')

#page = reader.pages[0]
#text = page.extract_text()
#print(text)

page1 = reader1.pages[0]
text1 = page1.extract_text()
#print(text1)


# WORDNET LEMMATIZER (with appropriate pos tags)

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

#nltk.download('averaged_perceptron_tagger')
#nltk.download('wordnet')
#nltk.download('punkt')

lemmatizer = WordNetLemmatizer()

# Define function to lemmatize each word with its POS tag

# POS_TAGGER_FUNCTION : TYPE 1
def pos_tagger(nltk_tag):
	if nltk_tag.startswith('J'):
		return wordnet.ADJ
	elif nltk_tag.startswith('V'):
		return wordnet.VERB
	elif nltk_tag.startswith('N'):
		return wordnet.NOUN
	elif nltk_tag.startswith('R'):
		return wordnet.ADV
	else:		 
		return None

#sentence = 'the cat is sitting with the bats on the striped mat under many badly flying geese'
sentence = text1

# tokenize the sentence and find the POS tag for each token
pos_tagged = nltk.pos_tag(nltk.word_tokenize(sentence)) 
#print(pos_tagged)

#>[('the', 'DT'), ('cat', 'NN'), ('is', 'VBZ'), ('sitting', 'VBG'), ('with', 'IN'), 
# ('the', 'DT'), ('bats', 'NNS'), ('on', 'IN'), ('the', 'DT'), ('striped', 'JJ'), 
# ('mat', 'NN'), ('under', 'IN'), ('many', 'JJ'), ('flying', 'VBG'), ('geese', 'JJ')]

# As you may have noticed, the above pos tags are a little confusing.

# we use our own pos_tagger function to make things simpler to understand.
wordnet_tagged = list(map(lambda x: (x[0], pos_tagger(x[1])), pos_tagged))
#print(wordnet_tagged)

#>[('the', None), ('cat', 'n'), ('is', 'v'), ('sitting', 'v'), ('with', None), 
# ('the', None), ('bats', 'n'), ('on', None), ('the', None), ('striped', 'a'), 
# ('mat', 'n'), ('under', None), ('many', 'a'), ('flying', 'v'), ('geese', 'a')]

lemmatized_sentence = []
for word, tag in wordnet_tagged:
	if tag is None:
		# if there is no available tag, append the token as is
		lemmatized_sentence.append(word)
	else:	 
		# else use the tag to lemmatize the token
		lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
lemmatized_sentence = " ".join(lemmatized_sentence)

print(lemmatized_sentence)
#> the cat can be sit with the bat on the striped mat under many fly geese