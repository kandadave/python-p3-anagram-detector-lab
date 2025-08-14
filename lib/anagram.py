# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, possible_anagrams):
        return [candidate for candidate in possible_anagrams if self._is_anagram(candidate)]

    def _is_anagram(self, candidate):
        candidate = candidate.lower()

        if candidate == self.word:
            return False
        
        return sorted(self.word) == sorted(candidate)