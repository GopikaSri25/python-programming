class Solution(object):
    def countConsistentStrings(self, allowed, words):
        s=0
        for x in words:
            if set(x).issubset(set(allowed)):
                s=s+1
        return s 
