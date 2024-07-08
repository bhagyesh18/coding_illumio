# coding_illumio


# WordMatcher

WordMatcher Module reads a file containing sentences and finds matches against a predefined set of words. 
The matching process is case-insensitive and considers only English words.
other characters will be ignored and will not be added to the set().
other characters, punctuation, or except this [A-Z] [a-z] will be ignored 

ASSUMPTION:
I am not sure about the "record" word meaning in your requirement. I have kept considering that there might be sentences 

## Files

- `word_matcher.py`: Contains the `WordMatcher` class and the main script for reading and matching words.
- `test_word_matcher.py`: Contains test cases to validate the functionality of the `WordMatcher` class.
- `predefined_words.txt`: Sample file containing predefined words, one per line.
- `input.txt`: Sample file containing input sentences, one per line.

## Requirements

- Python 3.x
- `unittest` module 

## Usage

### Running the WordMatcher
Run the `word_matcher.py` script:

    ```bash
    python word_matcher.py
    ```


### Running Tests
Run the test script using the following command:

    ```bash
    python test_word_matcher.py
    ```


### I though about following test cases 
1. Empty Files
2. Punctuation Handling
3. Mixed Case Sensitivity
4. Non-English Characters
5. Whitespace Handling
6. Numeric Characters
7. Long Words and Sentences
8. Edge Cases with Word Boundaries
9. NON ASCI FILE INPUT

