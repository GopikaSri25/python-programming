class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        # size array
        n = len(students)
        # students with 1 preference
        t1 = sum(students)
        t0 = n-t1
        while t1 >0 and t0>0:
            if t1>0 and sandwiches[0]==1:
                t1-=1
                sandwiches.pop(0)
            if t0>0 and sandwiches[0]==0:
                t0-=1
                sandwiches.pop(0)

        if t1==0 and t0==0:
            return 0
        elif t1>0:
            while len(sandwiches)>0 and sandwiches[0]!=0:
                sandwiches.pop(0)
                t1-=1
            return t1
        else:
            while len(sandwiches)>0 and sandwiches[0]!=1:
                sandwiches.pop(0)
                t0-=1
            return t0
