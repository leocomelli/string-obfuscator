import logging
import unicodedata

logger = logging.getLogger(__name__)

class NnpHandler:

    def __init__(self, files):
      self.files = files
      self.unique_file = []


    def merge(self):
        for file in self.files:

            names = [line.strip() for line in open(file, 'r')]
            for name in names:
                name = ''.join((c for c in unicodedata.normalize('NFD', name.decode('utf-8', 'ignore')) \
                             if unicodedata.category(c) != 'Mn')).lower().encode('utf-8')
                if not name in self.unique_file:
                    self.unique_file.append(name)


        return self.unique_file


if __name__ == '__main__':
    files = ['sources/pt_BR/name_1', 'sources/pt_BR/name_2', \
             'sources/pt_BR/surname_1', 'sources/pt_BR/surname_2', \
             'sources/pt_BR/surname_3', 'sources/pt_BR/surname_4',]
    h = NnpHandler(files)
    c = h.merge()

    logging.warning("writing unique nnp file - %s" % len(c))

    output = open('../data/pt_BR/nnp', 'w')
    output.writelines(["%s\n" % l for l in c])
    output.close()