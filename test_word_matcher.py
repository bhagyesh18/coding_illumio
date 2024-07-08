import unittest
from word_matcher import WordMatcher

class TestWordMatcher(unittest.TestCase):

    def setUp(self):
        # Create a test file with predefined words
        predefined_words_content = """bhagyesh
bananas
Mango
fruit
car
bike
bus
train
computer
laptop
phone
1232johon2323
@343245
&cake$
  sam
jurasic park 
          kumar       
BANANAS
MNAGO
ManGO
Ju1ce
computercomputercomputercomputercomputercomputercomputercomputercomputercomputercomputercomputercomputercomputercomputercomputercomputercomputercomputercomputercomputercomputer"""

        
        with open('test_predefined_words.txt', 'w') as file:
            file.write(predefined_words_content)
        
        self.matcher = WordMatcher('test_predefined_words.txt')



    def test_find_matches(self):
    # test normal cases 

        input_sentences_content = """I like to eat an Apple and baNanas
Bananas is my john's goto fruit
it is my birthday cake
laptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptoplaptop
#4432cacke 
~bhagyesh#
     Kumar love all that
I always take the bus and train to travel to office for illumio office
I am giving interview at illumio by using laptop
My friend loves his new phone"""

        with open('test_input.txt', 'w') as file:
            file.write(input_sentences_content)

        # Expected matches
        expected_matches = ['Bananas', 'Kumar', 'baNanas', 'bus', 'fruit', 'laptop', 'phone', 'train']

        # Run the matcher
        matches = self.matcher.find_matches('test_input.txt')

        # Sort matches for comparison
        matches.sort()
        expected_matches.sort()


        # Assert matches
        self.assertEqual(matches, expected_matches)

    def test_empty_files(self):
        # Test with empty input file
        with open('test_empty_input.txt', 'w') as file:
            file.write("")

        matches = self.matcher.find_matches('test_empty_input.txt')
        self.assertEqual(matches, [])

        with open('test_empty_predefined_words.txt', 'w') as file:
            file.write("")

        matcher_empty = WordMatcher('test_empty_predefined_words.txt')
        matches_empty = matcher_empty.find_matches('test_empty_input.txt')
        self.assertEqual(matches_empty, [])

    def test_punctuation_handling(self):
        # Test with words containing punctuation
        with open('test_punctuation_input.txt', 'w') as file:
            file.write("She likes mango, but not bananas.")

        matches = self.matcher.find_matches('test_punctuation_input.txt')
        self.assertIn("mango", matches)
        self.assertIn("bananas", matches)

    def test_mixed_case_sensitivity(self):
        # Test with mixed case sensitivity
        with open('test_mixed_case_input.txt', 'w') as file:
            file.write("I like MANGO and Bananas is my favorite FRUIT.")

        matches = self.matcher.find_matches('test_mixed_case_input.txt')
        self.assertIn("MANGO", matches)
        self.assertIn("Bananas", matches)
        self.assertIn("FRUIT", matches)

    def test_non_english_characters(self):
        # Test with non-English characters
        with open('test_non_english_input.txt', 'w') as file:
            file.write("El niño juega con la bananas.")

        matches = self.matcher.find_matches('test_non_english_input.txt')
        self.assertNotIn("niño", matches)  # Should not match non-English word
        self.assertIn("bananas", matches)

    def test_non_ascii_file(self):
        # Test with non-ASCII input file
        with open('test_non_ascii_input.txt', 'wb') as file:
            file.write("This is a test with non-ASCII characters: ü, é, ñ, ç.".encode('utf-8'))

        try:
            matches = self.matcher.find_matches('test_non_ascii_input.txt')
            self.assertEqual(matches, [])  # Assuming non-ASCII words are ignored
        except UnicodeDecodeError:
            self.fail("WordMatcher raised UnicodeDecodeError unexpectedly!")

if __name__ == '__main__':
    unittest.main()
