class Solution(object):
    def replaceDigits(self, s):
        alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        s=list(s)
        for i in range(1,len(s)):
            if s[i].isdigit():
                s[i]=alphabets[alphabets.index(s[i-1]) + int(s[i])]
        return ''.join(s)
