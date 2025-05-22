class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        s=""
        for i in range(0,min(len(word1),len(word2))):
            if((i<len(word1)) and (i<len(word2))):
                s+=word1[i]
                s+=word2[i]
        if len(word1)<len(word2):
            s+=word2[len(word1):]
        else:
            s+=word1[len(word2):]
        return s    

