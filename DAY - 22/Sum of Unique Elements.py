class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        for x in nums:
            freq[x]=freq.get(x,0)+1
        sum=0
        for i in freq:
            if freq[i]==1:
                sum+=i
        return sum
        
