import os
import json
import gzip
import pandas as pd
from nltk.corpus import wordnet


def load_dataset(filepath, max_reviews=None):
    """
    Carga un dataset en formato JSON comprimido (.json.gz).
    Cada línea del archivo representa una review en formato JSON.
    """
    data = []
    with gzip.open(filepath, 'rt') as f:
        for i, line in enumerate(f):
            if max_reviews and i >= max_reviews:
                break
            data.append(json.loads(line))
    return pd.DataFrame(data)


def get_wordnet_pos(tag):
    """
    Función para mapear etiquetas POS al formato de WordNet
    """
    if tag.startswith("J"):
        return wordnet.ADJ
    elif tag.startswith("V"):
        return wordnet.VERB
    elif tag.startswith("N"):
        return wordnet.NOUN
    elif tag.startswith("R"):
        return wordnet.ADV
    else:
        return wordnet.NOUN  
