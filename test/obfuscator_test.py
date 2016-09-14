import unittest
from core.obfuscator import StringObfuscator

class TestStringObfuscator(unittest.TestCase):

    def test_should_not_register_patterns(self):
        o = StringObfuscator()
        self.assertIsNone(o.list_patterns())


    def test_should_register_patterns(self):
        my_patterns = {'pattern1' : 'replacement1', 'pattern2' : 'replacement2'}
        o = StringObfuscator(my_patterns)
        self.assertEquals(len(o.list_patterns()), 2)


if __name__ == '__main__':
    unittest.main()