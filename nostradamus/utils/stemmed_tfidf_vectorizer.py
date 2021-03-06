from dataclasses import dataclass

from sklearn.feature_extraction.text import TfidfVectorizer
from Stemmer import Stemmer

from utils.const import STOP_WORDS

ENG_STEMMER = Stemmer("eng")


@dataclass(init=False)
class StemmedTfidfVectorizer(TfidfVectorizer):
    norm: str = "l2"
    sublinear_tf: bool = True
    min_df: int = 1
    stop_words: set = STOP_WORDS
    analyzer = "word"

    def build_analyzer(self):
        analyzer = super(TfidfVectorizer, self).build_analyzer()
        return lambda doc: ENG_STEMMER.stemWords(analyzer(doc))
