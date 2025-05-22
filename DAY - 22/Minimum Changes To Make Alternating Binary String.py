class Solution(object):
    def minOperations(self, s):
        """
        :type s: str
        :rtype: int
        """
        z = ''.join(['1' if i % 2 == 0 else '0' for i in range(len(s))])
        o = ''.join(['0' if i % 2 == 0 else '1' for i in range(len(s))])
        r, t = 0, 0
        for j in range(len(s)):
            if s[j] != z[j]:
                r += 1
            if s[j] != o[j]:
                t += 1
        return min(r, t)       
