"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """Finds all the words in a file and returns a random."""
    def __init__(self,file):
      self.word_file = open(file,"r")
      self.dictionary = set()
      self.init_msg()

    def init_msg(self,msg=''):
      """displays the # of dictionary words at initialization"""
      for word in self.word_file:
        self.dictionary.add(word.strip())
      print(f"{msg}{len(self.dictionary)} words read")

    def random(self):
      """selects a random word from the dictionary"""
      print(f"{random.sample(self.dictionary,1)[0]}")

# new_dict = WordFinder('words.txt')

class SpecialWordFinder(WordFinder):
    """ Subclass of WordFinder that filters blank lines and comments"""
    def __init__(self,file):
      """Filters blank lines & comments and displays an update message"""
      super().__init__(file)
      self.dictionary = {word for word in self.dictionary if not (word == '' or word.startswith('#'))}
      super().init_msg('Filtering dictionary... ')
    
new_dict = SpecialWordFinder('test_words.txt')