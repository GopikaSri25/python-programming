from collections import Counter
class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        nondistcnt = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                nondistcnt += 1
            
        return nondistcnt <= 2 and Counter(s1) == Counter(s2)


        
        
