

class StringObfuscator:


    def __init__(self, patterns = None):
      self.__patterns_registered = patterns


    def list_patterns(self):
        return self.__patterns_registered