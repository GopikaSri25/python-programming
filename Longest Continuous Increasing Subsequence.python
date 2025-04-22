class Solution(object):
    def findLengthOfLCIS(self, nums):
        a=0
        l=[]
        for x in range(0,len(nums)-1):
            if nums[x]>=nums[x+1]:
                l.append(a)
                a=0
            else:
                a=a+1
        l.append(a)
        return max(l)+1
        
