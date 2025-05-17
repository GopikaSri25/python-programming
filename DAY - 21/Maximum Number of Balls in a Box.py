class Solution(object):
    def digitSum(self, num):
        sum = 0
        while num != 0:
            sum = sum + (num % 10)
            num = num / 10
        return sum

    def countBalls(self, lowLimit, highLimit):
        """
        :type lowLimit: int
        :type highLimit: int
        :rtype: int
        """
        d = {}
        for i in range(lowLimit,highLimit+1):
            if self.digitSum(i) not in d.keys():
                d[self.digitSum(i)] = 1
            else:
                d[self.digitSum(i)] += 1
        
        m = 0
        for v in d.values():
            if v > m:
                m = v
        return m
        
