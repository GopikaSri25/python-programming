class Solution(object):
    def decode(self, encoded, first):
        """
        :type encoded: List[int]
        :type first: int
        :rtype: List[int]
        """
        ans=[]
        ans.append(first)
        for i in encoded:
            ans.append(ans[-1]^i)
        return ans
