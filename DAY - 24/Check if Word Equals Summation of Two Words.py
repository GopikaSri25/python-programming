class Solution(object):
    def isSumEqual(self, firstWord, secondWord, targetWord):
        word1 = ""
        word2 = ""
        target = ""
        for i in range(len(firstWord)):
            word1 += str(ord(firstWord[i])-97)

        for i in range(len(secondWord)):
            word2 += str(ord(secondWord[i])-97)
        
        for i in range(len(targetWord)):
            target += str(ord(targetWord[i])-97)

        return int(word1) + int(word2) ==  int(target)
