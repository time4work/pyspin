import re
import random
from nltk.corpus import wordnet
from nltk.tokenize import regexp_tokenize
import nltk.data
from nltk.stem.porter import *
import language_check

#an example of how to build a simple text spinner using nltk wordnet corpus
#obviusly you can modify this to work with any other synonym database
class spinner( object ):
#     function to spin spintax text using regex    
#     s = "{Spinning|Re-writing|Rotating|Content spinning|Rewriting} is {fun|enjoyable|entertaining|exciting|enjoyment}! try it {for yourself|on your own|yourself|by yourself|for you} and {see how|observe how|observe} it {works|functions|operates|performs|is effective}."
#     print spin(s)
    def spin(self, s):
        while True:
            s, n = re.subn('{([^{}]*)}',
                        lambda m: random.choice(m.group(1).split("|")),
                        s)
            if n == 0: break
        return s.strip()
    
#   split a paragraph into sentences.
#   you can use the following replace and split functions or the nltk sentence tokenizer
#   content = content.replace("\n", ". ")
#   return content.split(". ")
    def splitToSentences(self, content):
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        return tokenizer.tokenize(content)
    
#     get all synonyms of a word from the wordnet database
    def getSynonyms(self, word):
#         include the original word
        synonyms = [word]
        for syn in wordnet.synsets(word):
            for lemma in syn.lemma_names():
                if lemma != word:
#                     since wordnet lemma.name will include _ for spaces, we'll replace these with spaces
                    w, n = re.subn("_", " ", lemma)
                    synonyms.append(w)
        s = list(set(synonyms))
        return len(s), s
    
#     transform text into spintax with the folowing steps
#     1. split the text to sentences
#     2. loop through the sentences and tokenize it
#     3. loop thorugh each token, find its stem and assemble all the synonyms of it into the spintax
    def getSpintax(self, text):
        sentences = self.splitToSentences(text)
        stemmer = PorterStemmer()
        spintax = ""
        for sentence in sentences:
            tokens = regexp_tokenize(sentence, "[\w']+")
            for token in tokens:
                stem = stemmer.stem(token)
                n, syn = self.getSynonyms(stem)
                spintax += "{"
                spintax += token
                spintax += "|"
                for x in range(n):
                    spintax += syn[x]
                    if x < n-1:
                        spintax += "|"
                    else:
                        spintax += "} "
        return spintax

#---------------------------------end of spinner class ---------------------------------#

if __name__ == '__main__':

    s = spinner()
    spintax = s.getSpintax('After stroking her mans cock and sucking it in really hot manners, brunette porn model with big tits, Yu Shinohara, began spreading her legs, inviting the guy to deep lick her cherry and then fuck it in hardcore, craving for jizz on her shaved Asian pussy in the end.')
    spun = s.spin(spintax)
    tool = language_check.LanguageTool('en-US')
    text = spun
    matches = tool.check(text)
    result = language_check.correct(text, matches)
    
    print(spintax)
    print(spun+'\n')
    print(result)
