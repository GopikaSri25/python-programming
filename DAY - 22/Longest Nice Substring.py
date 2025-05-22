class Solution(object):
    def longestNiceSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<2:
            return ""
        se=set(s)
        for idx in range(len(s)):
            if s[idx].swapcase() not in se:
                return max(self.longestNiceSubstring(s[:idx]),self.longestNiceSubstring(s[idx+1:]),key=len)
        return s
