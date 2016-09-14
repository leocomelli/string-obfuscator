import unittest
from core.obfuscator import StringObfuscator

class TestStringObfuscator(unittest.TestCase):

    def test_should_register_patterns(self):
        o = StringObfuscator(self)
        self.assertEquals(len(o.list_patterns()), 0)

if __name__ == '__main__':
    unittest.main()