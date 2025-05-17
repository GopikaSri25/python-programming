class Solution(object):
    def countGoodRectangles(self, rectangles):
        arr=[]
        l=len(rectangles)
        for i in range (0,l):
            arr.append(min(rectangles[i]))
        return arr.count(max(arr))
