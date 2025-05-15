class Solution(object):
    def getMaximumGenerated(self, n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            nums=[0]*(n+1)
            nums[1]=1
            for i in range(0,n+1):
                if 2*i<=n and 2*i>=2:
                    nums[2*i]=nums[i]
                if 2*i+1<=n and 2*i+1>=2:
                    nums[2*i+1]=nums[i]+nums[i+1]
            return max(nums)


        
