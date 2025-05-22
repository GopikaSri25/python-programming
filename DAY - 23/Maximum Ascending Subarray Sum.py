class Solution(object):
    def maxAscendingSum(self, tab):
        somme=tab[0]
        r=somme
        for i in range(1,len(tab)):
            if tab[i]>tab[i-1]:
                somme+=tab[i]
                r=max(r,somme)
            else:
                somme=tab[i]
        return r
        
