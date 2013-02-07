import nltk
from nltk.text import Text,LidstoneProbDist
from nltk.model.ngram import NgramModel

f = open("poem.txt")
# f = open("howl.txt")

data = f.read()
def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)
data = removeNonAscii(data)

tokens = nltk.word_tokenize(data)
t = Text(tokens)
# t.generate(30)

estimator = lambda fdist, bins: LidstoneProbDist(fdist, 0.2)
trigram_model = NgramModel(3, t, estimator = estimator)

token_array = trigram_model.generate(150)[10:]

first_token = token_array[0].strip

if first_token in [".", ",", "?", "(", ")"]:
    token_array = token_array[1:]

joined = " ".join(token_array)
joined = joined.replace(" . ", ".\n")
joined = joined.replace(". ", ".\n")
joined = joined.replace(" ? ", "?\n")
joined = joined.replace(" , ", ",\n")
joined = joined.replace(" ) ", ")\n")
joined = joined.replace(" ( ", "(")
joined = joined.replace(" ! ", "!\n")

print ""
print joined
print ""
