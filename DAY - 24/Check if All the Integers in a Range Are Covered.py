class Solution(object):
    def isCovered(self, ranges, left, right):
        for num in range(left, right + 1):
            covered = False
            for start, end in ranges:
                if start <= num <= end:
                    covered = True
                    break  # No need to check further ranges
            if not covered:
                return False  
        return True  
