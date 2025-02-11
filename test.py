from gensim.models import KeyedVectors
import pprint

# load word vectors
wv = KeyedVectors.load_word2vec_format("vectors.bin", binary=True)

# most similar words
for mot in (
    "semblable",
    "lire",
    "tu",
    "corriger",
    "animale",
):
    print(mot.upper())
    pprint.pprint(wv.most_similar(mot))
