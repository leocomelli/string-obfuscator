import re

class StringObfuscator:

    DEFAULT_PATTERN_REPLACEMENT = '[PATTERN]'

    def __init__(self, patterns = None, nnp = None):
      self.__patterns_registered = patterns
      self.__nnp_registered = nnp

    def list_patterns(self):
        return self.__patterns_registered

    def list_nnp(self):
        return self.__nnp_registered

    def obfuscate(self, text):
        words = text.split(" ")

        for i, w in enumerate(words):
            nw = self.__replace_pattern__(w)
            words[i] = nw if w != nw else w

        return " ".join(w for w in words)


    def __replace_pattern__(self, word):
        for p, r in self.__patterns_registered.items():
          r = self.DEFAULT_PATTERN_REPLACEMENT if r == "" or r is None else r
          return re.sub(p, r, word)

        return word

