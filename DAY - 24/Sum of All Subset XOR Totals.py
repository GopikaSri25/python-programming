class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.total = 0

        def backtrack(index, curr_xor):
            if index == len(nums):
                self.total += curr_xor
                return

            # Include nums[index] in the XOR
            backtrack(index + 1, curr_xor ^ nums[index])

            # Exclude nums[index]
            backtrack(index + 1, curr_xor)

        backtrack(0, 0)
        return self.total
