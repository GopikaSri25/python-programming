class Solution(object):
    def squareIsWhite(self, coordinates):
        """
        :type coordinates: str
        :rtype: bool
        """
        l1=['a','c','e','g']
        l2=['b','d','f','h']
        if coordinates[0] in l1:
            if int(coordinates[1])%2!=0:
                return False
            else:
                return True
        else:
            if int(coordinates[1])%2!=0:
                return True
            else:
                return False


        
