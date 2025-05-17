class Solution(object):
    def totalMoney(self, n):
        #:type n: int ,:rtype: int
        week_inc=0
        total_amount=0
        per_day=0

        for i in range(n):
            if i%7==0 and i>0:
                week_inc=week_inc+1
                per_day=0

            per_day=per_day+1
            
            total_amount=per_day + week_inc + total_amount

        return (total_amount)
