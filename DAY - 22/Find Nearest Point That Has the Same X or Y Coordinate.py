class Solution(object):
    def nearestValidPoint(self, x, y, points):
        index = -1
        distance = 9999999
        for point in points:
            if distance > abs(x-point[0])+abs(y-point[1]) and (x==point[0] or y==point[1]):
                distance = abs(x-point[0])+abs(y-point[1])
                index = points.index(point)
        return index

        
