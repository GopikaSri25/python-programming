class Solution(object):
    def checkIfPangram(self, sentence):
        for i in range(ord('a'),ord('z')+1):
            if sentence.find(chr(i)) == -1:
                return False
        return True
                

        
