#-*- coding: iso-8859-15 -*-

import unittest
from core.obfuscator import StringObfuscator

class TestStringObfuscator(unittest.TestCase):

    def test_should_not_register_patterns(self):
        o = StringObfuscator()
        self.assertEquals(0, len(o.list_patterns()))
        self.assertEquals(0, len(o.list_nnp()))

    def test_should_register_patterns(self):
        my_patterns = {'pattern1' : 'replacement1', 'pattern2' : 'replacement2'}
        o = StringObfuscator(my_patterns)
        self.assertEquals(2, len(o.list_patterns()))
        self.assertEquals(0, len(o.list_nnp()))

    def test_should_register_nnp(self):
        nnp = {'John' : '[NNP]', 'Steve' : '[NNP]'}
        o = StringObfuscator(None, nnp)
        self.assertEquals(0, len(o.list_patterns()))
        self.assertEquals(2, len(o.list_nnp()))

    def test_should_register_both(self):
        my_patterns = {'pattern1': 'replacement1', 'pattern2': 'replacement2'}
        nnp = {'John' : '[NNP]', 'Steve' : '[NNP]'}
        o = StringObfuscator(my_patterns, nnp)
        self.assertEquals(2, len(o.list_patterns()))
        self.assertEquals(2, len(o.list_nnp()))

    def test_should_replace_string(self):
        o = StringObfuscator({'secret' : '***'})
        text = "his password is ***"
        obfuscated = o.obfuscate("his password is secret")
        self.assertEqual(text, obfuscated)

    def test_should_replace_string_with_basic_regex(self):
        o = StringObfuscator({'^s.*t$' : '***'})
        text = "his password is ***"
        obfuscated = o.obfuscate("his password is secret")
        self.assertEqual(text, obfuscated)

    def test_should_replace_string_with_complex_regex(self):
        o = StringObfuscator({'[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}': '[CPF]'})
        text = "my cpf number is [CPF]"
        obfuscated = o.obfuscate("my cpf number is 564.987.456-99")
        self.assertEqual(text, obfuscated)

    def test_should_replace_two_strings_with_basic_regex(self):
        o = StringObfuscator({'^s.*t$' : '***'})
        text = "ah *** -> his password is ***"
        obfuscated = o.obfuscate("ah secret -> his password is secret")
        self.assertEqual(text, obfuscated)

    def test_should_replace_string_default_replacement(self):
        o = StringObfuscator({'^s.*t$': ''})
        text = "his password is [PATTERN]"
        obfuscated = o.obfuscate("his password is secret")
        self.assertEqual(text, obfuscated)

    def test_should_replace_nnp(self):
        o = StringObfuscator(None, {'John' : ''})
        text = "his name is [NNP]"
        obfuscated = o.obfuscate("his name is John")
        self.assertEqual(text, obfuscated)

    def test_should_replace_compound_nnp(self):
        o = StringObfuscator(None, {'John' : '', 'Doe' : ''})
        text = "his name is [NNP]"
        obfuscated = o.obfuscate("his name is John Doe")
        self.assertEqual(text, obfuscated)

    def test_should_replace_compound_nnp1(self):
        o = StringObfuscator(None, {'John' : '', 'Doe' : ''})
        text = "his name is [NNP]"
        obfuscated = o.obfuscate("his name is John of Doe")
        self.assertEqual(text, obfuscated)

    def test_should_load_patterns_and_nnp_from_file(self):
        o = StringObfuscator()
        o.load_patterns_and_nnp("resources/patterns.txt", "resources/nnp_ptBR.txt")
        self.assertEquals(3, len(o.list_patterns()))
        self.assertEquals(4, len(o.list_nnp()))

    def test_should_load_and_obfuscate(self):
        o = StringObfuscator()
        o.load_patterns_and_nnp("patterns.txt", "nnp_ptBR.txt")
        text = "the password of [NOME] is [PADRAO] don't [PADRAO] it"
        obfuscated = o.obfuscate("the password of Carlos Eduardo is secret don't forget it")
        self.assertEqual(text, obfuscated)

if __name__ == '__main__':
    unittest.main()