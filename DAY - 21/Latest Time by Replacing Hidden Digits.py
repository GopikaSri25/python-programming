class Solution(object):
    def maximumTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        ans =''
        for i in range(len(time)):
            if time[i] != '?':
                ans = ans + time[i]
            else:
                if i == 0:
                    if time[i+1] == '?':
                        ans = ans + '2'
                    else:
                        if time[i+1] not in ['0','1','2','3']:
                            ans = ans + '1'
                        else:
                            ans = ans + '2'
                elif i == 1:
                    if time[i - 1] == '?':
                        ans = ans + '3'
                    else:
                        if time[i - 1] in ['0' ,  '1']:
                            ans = ans + '9'
                        else:
                            ans = ans + '3'
                elif i == 3:
                    ans = ans + '5' 
                elif i == 4:
                    ans = ans + '9'
        return ans                   
    
