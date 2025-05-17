class Solution(object):
    def reformatNumber(self, number):
        """
        :type number: str
        :rtype: str
        """
        number=number.replace("-","")
        number=number.replace(" ","")
        s=""
        for i in range(0,len(number),3):
            if len(number[i:])>4: 
                s+=number[i:i+3]
            elif len(number[i:])==4: 
                s+=number[i:i+2]
                s+="-"
                s+=number[i+2:i+4]
            else: 
                if len(number[i:])>1: s+=number[i::]
            if i+3<len(number)-1: s+="-"
        return s

        
