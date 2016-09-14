import re

class StringObfuscator:

    DEFAULT_PATTERN_REPLACEMENT = '[PATTERN]'
    DEFAULT_NNP_REPLACEMENT = '[NNP]'

    def __init__(self, patterns = None, nnp = None):
      self.__patterns_registered = patterns
      self.__nnp_registered = nnp

    def list_patterns(self):
        return self.__patterns_registered if self.__patterns_registered is not None else {}

    def list_nnp(self):
        return self.__nnp_registered if self.__nnp_registered is not None else {}

    def obfuscate(self, text):
        words = text.split(" ")

        self.__replace__(words, self.list_patterns(), self.DEFAULT_PATTERN_REPLACEMENT)
        self.__replace__(words, self.list_nnp(), self.DEFAULT_NNP_REPLACEMENT)

        return " ".join(w for w in words)

    def __replace__(self, words, patterns, default_replacement = None):
        if len(patterns) == 0:
            return words

        for i, w in enumerate(words):
            for p, r in patterns.items():
                r = default_replacement if r == '' or r is None else r
                words[i] = re.sub(p, r, w)