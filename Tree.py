class queue:
    def __init__(self):
        self.store=[]
        self.cnt = 0

    def enqueue(self,value):
        self.store=self.store+[value]
        self.cnt = self.cnt + 1
        return self.cnt

    def dequeue(self):
        if (self.cnt==0):
            return [False,0]
        else:
            r=self.store[0]
            self.cnt=self.cnt-1
            self.store=self.store[1:]
            return [True,r]

class Tree:
    def __init__(self,x):
        self.store = [x,[]]

    def AddSuccessor(self,x):
        self.store[1] = self.store[1] + [x]
        return True

    def GetSuccessors(self):
        return self.store[1]

    def GetNode (self):
        return self.store[0]

    def Get_LevelOrder(self):
        x=queue()
        x.enqueue(self.store)
        accum=[]
        while True:
            y=x.dequeue()
            if (y[0]==False):
                break
            else:
                v=y[1]
                accum += [v[0]]
                for i in v[1]:
                    x.enqueue(i.store)
        return accum
