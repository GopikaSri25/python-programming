class Solution(object):
    def interpret(self, command):
        new_string = ''
        for i in range(len(command)-1):
            if command[i] == "(" and command[i+1] == ")":
                new_string+="o"
            else:
                new_string+=command[i]
        new_string+=command[-1]
        s = ''
        for i in new_string:
            if i == "(":
                s+=""
            else:
                s+=i.replace(")", "")
        return s
