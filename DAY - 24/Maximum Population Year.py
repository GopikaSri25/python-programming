class Solution(object):
    def maximumPopulation(self, logs):
        a=0
        for i in logs:
            for j in i:
                a=max(a,j)
        li=[0]*(a+1)
        for i in logs:
            x=i[0]
            y=i[1]
            for j in range(x,y):
                li[j]+=1
        m=max(li)
        for i in range(len(li)):
            if li[i]==m:
                return i
        
