from . import BaseDocSimilarity


class NGramCompare(BaseDocSimilarity.BaseDocSimilarity):
    def __init__(self, *, ngram_length, **kwargs):
        """Core init syntax for ngram comparison class.
        Ngram is defined here as number of words instead of number of letters.
        Word grams?

        Keyword arguments:
        left_doc -- first text document to compare (string input, becomes list)
        right_doc -- second text document to compare (string input, becomes list)
        ngram_length -- length of the ngram desired (int, > 0)
        **kwargs -- for optional keyword arguments:
                        stop_words -- words to remove from both texts (list[string])
                        regex -- regex pattern to replace with spaces (regex pattern)
        """
        super().__init__(**kwargs)

        if ngram_length < 1:
            raise ValueError('NGram length must be greater than 0.')
        
        self._ngram_length = ngram_length
        self._ngram_data = {}

        self._prep_data()
        return

    def _calculate_similarity(self):
        """Calculate an Intersection/Union similarity metric for left and right docs.
        """
        unique_ngrams = list(set(self._ngram_data['right_doc'] + self._ngram_data['left_doc']))
        
        return len([ngram for ngram in self._ngram_data['right_doc'] if ngram in self._ngram_data['left_doc']]) / float(len(unique_ngrams)), len([ngram for ngram in self._ngram_data['left_doc'] if ngram in self._ngram_data['right_doc']]) / float(len(unique_ngrams))

    def _prep_data(self):
        """Create list of tuples stored in dict[str-> list[tuples]]"""
        self._ngram_data['left_doc'] = self._generate_ngrams(self._tokenize(self._left_doc))
        self._ngram_data['right_doc'] = self._generate_ngrams(self._tokenize(self._right_doc))
        return

    def _generate_ngrams(self, doc):
        """Generate word grams of length ngram_length with zip

        Keyword arguments:
        doc -- text document to clean (string)
        """
        # *[] unpacks list for function call zip(), will need to change for ngram 
        #     range approach (allow for multiple ngrams in the same calculation)
        return list(zip(*[doc[i:] for i in range(self._ngram_length)]))
