class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split()
        word_pairs = [(word[:-1],int(word[-1])) for word in words ]
        word_pairs.sort(key =lambda x:x[1])
        ordered_words = [word for word, _ in word_pairs]
        return " " .join(ordered_words)
        
        
