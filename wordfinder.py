"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Finds all the words in a file and returns a random.

    >>> new_dict = WordFinder('word_finder_test.txt')
    4 words read

    >>> new_dict.random() in ['kale','parsnips','apple','mango']
    True
    """
    def __init__(self,file):
      self.dictionary = set()

      self.word_file = open(file,"r")
      for word in self.word_file:
        self.dictionary.add(word.strip())
      self.word_file.close()
      
      self.init_msg()

    def init_msg(self,msg=''):
      """displays the # of dictionary words at initialization"""

      print(f"{msg}{len(self.dictionary)} words read")

    def random(self):
      """selects a random word from the dictionary"""
      return random.sample(self.dictionary,1)[0]
      """why does this return a NoneType?"""

# new_dict = WordFinder('words.txt')

class SpecialWordFinder(WordFinder):
    """ Subclass of WordFinder that filters blank lines and comments"""
    
    def __init__(self,file):
      """Filters blank lines & comments and displays an update message"""
      
      super().__init__(file)
      self.dictionary = {word for word in self.dictionary if not (word == '' or word.startswith('#'))}
      super().init_msg('Filtering dictionary... ')
      """Can we prevent the parent class from calling it's own message?"""
    
# new_dict = SpecialWordFinder('test_words.txt')
