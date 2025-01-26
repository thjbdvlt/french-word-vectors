from gensim.models import KeyedVectors
import pprint

# load word vectors
wv = KeyedVectors.load_word2vec_format("vectors.bin", binary=True)

# most similar words
for mot in (
    "corriger",
    "semblable",
    "lire",
    "nature",
    "personne",
):
    print(mot.upper())
    pprint.pprint(wv.most_similar(mot))
