import re

class WordMatcher:
    def __init__(self, predefined_words_file_path):
        """
        Initializes the WordMatcher with a set of predefined words.
        :param predefined_words_file_path: Path to the file containing predefined words, one per line. 
        """
        self.predefined_words_set = self._read_predefined_words(predefined_words_file_path)
    
    def _read_predefined_words(self, file_path):
        """
        Reads predefined words from a file and returns them as a set.
            - Only English words are included 
            - if word is made of other characters, that will not be added to set() and will not be matched against the input file
            - searching is case-insensitive.
        :param file_path: predefined words file path 
        :return: A set of predefined words.
        """    
  
        # We will use the Set() to store all the words in-memory for fast searching
        # Also, it keeps the unique objects in the collections.
        # In Python, there is no explicit limit on the size of a set other than the limits imposed by the available memory. 
        #     - implemented as a hash table
        #     - Average-time complexity O(1) for insertions, deletions, and membership checks. 
        # 
        predefined_words = set()
        with open(file_path, 'r') as file:
            for line in file:
                word = line.strip().lower()
                if re.match("^[a-zA-Z]+$", word):
                    predefined_words.add(word)
        return predefined_words

    def find_matches(self, input_file_path):
        """
        Reads an input file containing sentences and finds words that match a predefined set of words.
            - Only English words are considered for matching.
            - The requirement mentioned about the input file with record. the record word is not clear here. assuming sentences.
            - if word is made of other characters, that will not be added to set() and will not be matched against the input file
            - searching is case-insensitive.
            - remove other punctuation keyword for searching if the record is the sentence.
        :param input_file_path: Path to the input file containing sentences, one per line.
        :param predefined_words_file_path: Path to the file containing predefined words, one per line.
        :return: A list of matching words.
        """        
        matches = []
        with open(input_file_path, 'r') as file:
            for line in file:
                # The requirement mentioned about the input file with record. the record word is not clear here. assuming sentences or word. 
                words = line.strip().split()
                for word in words:
                    # Strip punctuation and convert to lowercase for case-insensitive matching
                    clean_word = word.strip('.,!?";:()[]{}').lower()
                    # if word contains other character thans English character, it will not be matched and ignored.
                    if re.match("^[a-zA-Z]+$", clean_word) and clean_word in self.predefined_words_set:
                        matches.append(word.strip('.,!?";:()[]{}'))
        return matches

if __name__ == "__main__":
    
    input_file_path = 'input.txt'
    predefined_words_file_path = 'predefined_words.txt'
    
    matcher = WordMatcher(predefined_words_file_path)
    matches = matcher.find_matches(input_file_path)
    
    # Output the matches
    for match in matches:
        print(match)
     
