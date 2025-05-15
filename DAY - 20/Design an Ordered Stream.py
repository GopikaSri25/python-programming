class OrderedStream(object):

    def __init__(self, n):
        self.stream = [""]*n
        self.ptr = 0
        

    def insert(self, idKey, value):
        if not value:
            return None

        self.stream[idKey-1] = value
        temp = []
        tempCount = self.ptr

        if self.ptr == idKey-1:
            for i in range(self.ptr, len(self.stream)):
                if not self.stream[i]:
                    break
                temp.append(self.stream[i])
                tempCount += 1
        
        self.ptr = tempCount
        return temp
