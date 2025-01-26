__word vectors__ for french.

Vectors are trained with [Gensim](https://radimrehurek.com/gensim/) on 31 millions sentences and 722 millions tokens, using [word2vec](https://radimrehurek.com/gensim/models/word2vec.html) algorithm (CBOW) and have 100 dimensions.

training data
-------------

The training data is the concatenation of some books from [Wikisource](https://fr.wikisource.org/wiki/Wikisource:Accueil) and texts extracted from [wikipedia dump](https://dumps.wikimedia.org/backup-index.html). For the latter, I've especially extracted texts containing personal pronouns.
Texts from Wikisource by: Alexandre Dumas, André Gide, Charles Augustin Sainte-Beuve, Charles-Henri Favrod, Colette, Émile Durkheim, Fédor Dostoïevski, George Sand, Jack London, Joseph Texte, Jules Verne, Juliette Lalonde-Rémillard, Leandro Despouy, Léon Tolstoï, Lucien Fabre, Ludwig Wittgenstein, Marcel Mauss, Marcel Proust, Michelle LeNormand, Philippe Tamizey de Larroque, Pierre Kropotkine, Rachilde, Robert Carmille, Simone Weil, Solange Fernex, Uppaluri Gopala Krishnamurti.

All texts have been tokenized using [jusqucy](https://github.com/thjbdvlt/jusquci) tokenizer and normalized with [commecy](https://github.com/thjbdvlt/commecy) normalizer. If you use these vectors on your texts, be sure that the tokenization and the normalization is not too different (e.g. do not use uppercase letters, curly apostrophs or ligatures letters).


example
-------

```python
from gensim.models import KeyedVectors
import pprint

# load word vectors
wv = KeyedVectors.load_word2vec_format('vectors.bin', binary=True)

# most similar words
for mot in ("corriger", "écrire", "semblable"):
    print(mot.upper())
    pprint.pprint(wv.most_similar(mot))
```
```txt
SEMBLABLE
[('similaire', 0.9007408618927002),
 ('comparable', 0.8466804027557373),
 ('analogue', 0.8395078778266907),
 ('ressemblant', 0.7920158505439758),
 ('identique', 0.7211716771125793),
 ('lié', 0.6224735379219055),
 ('différente', 0.6138802170753479),
 ('équivalente', 0.5944404006004333),
 ('assimilable', 0.5906792879104614),
 ('liée', 0.5830994844436646)]
LIRE
[('consulter', 0.8208450675010681),
 ('regarder', 0.7977961897850037),
 ('relire', 0.7744161486625671),
 ('écrire', 0.7696584463119507),
 ('voir', 0.7335200905799866),
 ('publier', 0.7282490730285645),
 ('recopier', 0.7280176877975464),
 ('traduire', 0.7270112037658691),
 ('rédiger', 0.7108854055404663),
 ('suivre', 0.7057061195373535)]
TU
[('-tu', 0.8598954081535339),
 ('je', 0.7314501404762268),
 ('-je', 0.6225795149803162),
 ("j'", 0.6168178915977478),
 ('toi', 0.59869384765625),
 ('toi-même', 0.588273823261261),
 ("t'", 0.5764334797859192),
 ('skhul', 0.5512966513633728),
 ('moi-même', 0.5456873774528503),
 ('-y', 0.5358070135116577)]
CORRIGER
[('rectifier', 0.9306483864784241),
 ('retoucher', 0.8068966865539551),
 ('modifier', 0.8034698367118835),
 ('reformuler', 0.8020774722099304),
 ('vérifier', 0.7907589673995972),
 ('réintroduire', 0.7818157076835632),
 ('supprimer', 0.7817071676254272),
 ('compléter', 0.7789778709411621),
 ('raccourcir', 0.7720335125923157),
 ('rajouter', 0.7719793915748596)]
ANIMALE
[('végétale', 0.8479821681976318),
 ('microbienne', 0.8207957148551941),
 ('biologique', 0.8099811673164368),
 ('humaine', 0.7661771178245544),
 ('bactérienne', 0.7577511668205261),
 ('mentale', 0.7346532344818115),
 ('physiologique', 0.7225533127784729),
 ('corporelle', 0.7225015759468079),
 ('endogène', 0.7106938362121582),
 ('intensive', 0.68355393409729)]
```

use with spacy
--------------

To use the vectors with [spacy](https://spacy.io/), one need to convert the vectiors to text format.

```python
from gensim.models import KeyedVectors

# load binary word vectors
wv = KeyedVectors.load_word2vec_format('./vectors_cbow_count_2.bin', binary=True)

# save text word vectors
wv.save_word2vec_format('model.word2vec', binary=False)
```

Create the vectors for a pipeline from file:

```bash
spacy init vectors fr model.word2vec vectors
```
