import re
import logging
import unicodedata

logger = logging.getLogger(__name__)

class StringObfuscator:

    DEFAULT_PATTERN_REPLACEMENT = '[PATTERN]'
    DEFAULT_NNP_REPLACEMENT = '[NNP]'

    def __init__(self, patterns = None, nnp = None):
      self.__patterns_registered = patterns
      self.__set_nnp_registered__(nnp)

    def list_patterns(self):
        return self.__patterns_registered if self.__patterns_registered is not None else {}

    def list_nnp(self):
        return self.__nnp_registered if self.__nnp_registered is not None else {}

    def load_patterns_and_nnp(self, patterns_file, nnp_file):
        logging.warning("loading patterns and nnp from files")
        self.__patterns_registered = self.__read_file_content([line.strip() for line in open(patterns_file, 'r')])
        self.__set_nnp_registered__(self.__read_file_content([line.strip() for line in open(nnp_file, 'r')]))

    def sanitize_data(self, text):
        return ''.join((c for c in unicodedata.normalize('NFD', text.decode('utf-8', 'ignore')) \
                        if unicodedata.category(c) != 'Mn')).lower().encode('utf-8')

    def obfuscate(self, text):
        words = text.split(" ")

        self.__replace__(words, self.list_patterns(), self.DEFAULT_PATTERN_REPLACEMENT)
        self.__replace__(words, self.list_nnp(), self.DEFAULT_NNP_REPLACEMENT)
        self.__merge_compound_nnp__(words)

        return " ".join(w for w in words)

    def __replace__(self, words, patterns, default_replacement = None):
        if len(patterns) == 0:
            return words

        for p, r in patterns.items():
            for i, w in enumerate(words):
                r = default_replacement if r == '' or r is None else r
                words[i] = re.sub(r'\b%s\b' % p, r, w)

    def __merge_compound_nnp__(self, words):
        is_compound = False
        replacements = self.list_nnp().values()
        replacements.append(self.DEFAULT_NNP_REPLACEMENT)

        # remove the word that joins the compound names
        for i, word in enumerate(words):
            if len(words) > i +2 and \
               word in replacements and \
               len(words[i +1]) <= 3 and \
               words[i +2] in replacements:
                del words[i +1]

        # remove the second occurrence of replacement
        for i, word in enumerate(words):
            if word in replacements and is_compound:
                del words[i]
                continue
            else:
                is_compound = True if word in replacements else False

    def __read_file_content(self, lines):
        d = {}
        for line in lines:
            cols = line.split()
            d[cols[0]] = '' if len(cols) == 1 else cols[1]
        return d

    def __set_nnp_registered__(self, nnp):
        self.__nnp_registered = dict((self.sanitize_data(k), v) for k, v in nnp.iteritems()) if nnp is not None else nnp


