class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
     
        keys ={
            "type": 0,
            "color" : 1,
            "name" : 2
        }
        result = 0

        for i in range(len(items)):
            if ruleValue == items[i][keys[ruleKey]]:
                result += 1
        return result


        
