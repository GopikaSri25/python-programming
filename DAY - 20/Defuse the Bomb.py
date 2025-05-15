class Solution(object):
    def decrypt(self, code, k):

        n = len(code)
        newArr = [0] * n 

        if k == 0: 
            return newArr

        code = code *3 
        
        for i in range(n, 2*n):
            if k > 0:
                newArr[i-n] = sum(code[i+1:i+k+1]) 
            else:
                newArr[i-n] = sum(code[i + k:i]) 
        
        return newArr



        


        
