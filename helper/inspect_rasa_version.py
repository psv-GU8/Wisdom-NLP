import rasa_nlu
import rasa_core
import spacy

print("rasa_nlu: {}  \nrasa_core: {}".format(rasa_nlu.__version__,rasa_core.__version__))
print("Loading spacy language model...")
print(spacy.load("en")("hello World!"))