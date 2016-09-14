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

    def test_should_replace_string(self):
        o = StringObfuscator({'secret' : '***'})
        text = "his password is ***"
        obfuscated = o.obfuscate("his password is secret")
        self.assertEqual(obfuscated, text)

    def test_should_replace_string_with_basic_regex(self):
        o = StringObfuscator({'^s.*t$' : '***'})
        text = "his password is ***"
        obfuscated = o.obfuscate("his password is secret")
        self.assertEqual(obfuscated, text)

    def test_should_replace_string_with_complex_regex(self):
        o = StringObfuscator({'[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}': '[CPF]'})
        text = "my cpf number is [CPF]"
        obfuscated = o.obfuscate("my cpf number is 564.987.456-99")
        self.assertEqual(obfuscated, text)

if __name__ == '__main__':
    unittest.main()