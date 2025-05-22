class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype:
         int
        """
        for char in word:
            if not char.isdigit():
                word = word.replace(char, ' ')
        
        numbers = word.split()
        unq = set()
        for num in numbers:
            unq.add(str(int(num)))

        return len(unq)
        
