class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        nums = int(num)
        if nums % 2 != 0:
            return str(nums)
        else:
            while nums > 0:
                r = nums % 10
                if r % 2 != 0:
                    return str(nums)
                nums = nums // 10
            return ""
