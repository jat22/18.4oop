"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    def __init__(self, file_path):
        self.file = file_path
        self.words = self.generate_words(self.file)
        print(f'{len(self.words)} words')
       
    def generate_words(self, file):
        lines = open(file, 'r').readlines()
        words = []
        for line in lines:
            line = list(line)
            line.pop(-1)
            word = ''.join(line)
            words.append(word)
        return words

    def random(self):
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    def generate_words(self, file):
        lines = open(file, 'r').readlines()
        words = []
        for line in lines:
            line = list(line)
            line.pop(-1)
            word = ''.join(line)
            if word != '' and not word.startswith('#'):
                words.append(word)
        return words
                
