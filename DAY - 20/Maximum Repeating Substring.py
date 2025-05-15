class Solution(object):
    def maxRepeating(self, sequence, word):  
        a = 1
        while (word * a) in sequence:
            a += 1
        return (a - 1)
