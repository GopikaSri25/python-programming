class Solution(object):
    def checkZeroOnes(self, s):
        """
        :type s: str
        :rtype: bool
        """
        longest1s = 0
        longest0s = 0
        l = len(s)
        i=0
        l_1=0
        l_0=0
        while i<len(s)-1:
            if s[i] == '1':
                l_1 +=1
                if s[i+1] != '1':
                    longest1s = max(longest1s, l_1)
                    l_1 = 0
            else:
                l_0 +=1
                if s[i+1] != '0':
                    longest0s = max(longest0s, l_0)
                    l_0 = 0    
            i += 1         
           
        if s[i] == '1':
            l_1 +=1
        else:
            l_0 +=1

        longest1s = max(longest1s, l_1)
        longest0s = max(longest0s, l_0)            

        return True if longest1s > longest0s else False
                
