from abc import ABC, abstractmethod
from os import path
import re


stopword_filename = path.abspath(path.join(path.dirname(__file__),
                                   '..', 'resources/stop_words.txt'))


class BaseDocSimilarity(ABC):
    """Abstract base class for text document comparison"""
    def __init__(self, *, left_doc, right_doc, **kwargs):
        """Core init syntax for similarity base class

        Keyword arguments:
        left_doc -- first text document to compare (string)
        right_doc -- second text document to compare (string)
        **kwargs -- for optional keyword arguments:
                        stop_words -- words to remove from both texts (list[string])
                        regex -- regex pattern to replace with spaces (regex pattern)
        """
        self._left_doc = left_doc
        self._right_doc = right_doc

        self._similarity_values = None
        
        self._stop_words = kwargs.get('stop_words', None)
        self._regex = kwargs.get('regex', r'[^a-zA-Z0-9\'\,\.\s]')
        return

    def compare(self):
        if not self._stop_words:
            self._stop_words = self._load()
        
        self._left_doc = self._clean(self._left_doc)
        self._right_doc = self._clean(self._right_doc)
        
        self._similarity_values = self._calculate_similarity()
        
        return self._similarity_values

    def _load(self):
        """Used to load stop words file from local file if not provided"""
        with open(stopword_filename) as f:
            stop_words = f.readlines()
            stop_words = [word.strip() for word in stop_words]

        return stop_words

    def _clean(self, text):
        """Parse document text to remove stop words, punctuation, etc...

        Keyword arguments:
        text -- text document to clean (string)
        """
        text = text.lower()
        text = re.sub(self._regex, ' ', text)

        if self._stop_words:
            text = self._remove_stop_words(text)

        text = re.sub(r'\s+', ' ', text)

        return text

    @abstractmethod
    def _calculate_similarity(self):
        pass

    def _remove_stop_words(self, text):
        """Remove stop words from document text

        Keyword arguments:
        doc -- text document to clean (string)
        """
        return ' '.join([word for word in text.split() if word not in self._stop_words])

    def _tokenize(self, text):
        """Break sentence in the tokens, remove empty tokens"""
        return [token for token in text.split(" ") if token != ""]
