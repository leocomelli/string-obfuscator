# string obfuscator

A simple tool that use patterns or proper nouns to obfuscate words.

### Features

You can...

1. Define patterns or nnp as dict;
1. Load patterns or nnp from files;
1. Use a default replacement to obfuscate a word ([PATTERN] or [NNP]);
1. Specify a custom replacement to obfuscate a word;
1. Obfuscate a compound proper noun (eg.: John Doe => [NNP]);
1. Use regex to match a pattern;
1. Use a list of common names/surnames in Brazil; 

**your data must be lowercase and non-accent, if necessary you can use the [sanitize_data](https://github.com/leocomelli/string-obfuscator/blob/master/core/obfuscator.py#L27) method.**

### Examples
take a look in the [unit test file](https://github.com/leocomelli/string-obfuscator/blob/master/test/obfuscator_test.py)
