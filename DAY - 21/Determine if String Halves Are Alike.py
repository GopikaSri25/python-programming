class Solution(object):
    def halvesAreAlike(self, s):
        """
        :type s: str
        :rtype: bool
        """
        count=0
        s=s.lower()
        vowels=['a','e','i','o','u']
        for i in range(len(s)):
            if i<len(s)//2:
                if s[i] in vowels:
                    count+=1
            else:
                if s[i] in vowels:
                    count-=1
        if count==0:
            return True
        return False
        
