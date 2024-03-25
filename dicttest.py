from collections import *
from random import randint


# Use this because normal dict can sometimes give TLE
class mydict:
    def __init__(self, func=lambda: 0):
        self.random = randint(0, 1 << 32)
        self.default = func
        self.dict = {}
    def __getitem__(self, key):
        mykey = self.random ^ key
        if mykey not in self.dict:
            self.dict[mykey] = self.default()
        return self.dict[mykey]
    def get(self, key, default):
        mykey = self.random ^ key
        if mykey not in self.dict:
            return default
        return self.dict[mykey]
    def __setitem__(self, key, item):
        mykey = self.random ^ key
        self.dict[mykey] = item
    def getkeys(self):
        return [self.random ^ i for i in self.dict]
    def __str__(self):
        return f'{[(self.random ^ i, self.dict[i]) for i in self.dict]}'
    # def items(self):
    #     item = []
    #     for i in self.dict:
    #         item.append([i,self.get(i,lambda :0)])
    #     return item
 
 
# data = [1, 2, 3, 1, 2, 1]
# counts = mydict(lambda: 0)  # Initialize mydict with default value 0
# for item in data:
#     counts[item] += 1
# print(counts)


def op(x,y):
    d = mydict(lambda: 0) #defaultdict(int)
    d[x[0]] += x[1]
    d[y[0]] += y[1]
    d[x[2]] += x[3]
    d[y[2]] += y[3]
    # p = sorted(d.items(),key=lambda x:(-x[0]))
    p = [[key,d[key]] for key in d.getkeys()]
  
    p = sorted(p,key=lambda x:(-x[0]))
    tmp = [*p[0]]
    if len(p)!=1:
        tmp.append(p[1][0])
        tmp.append(p[1][1])
    else:
        tmp.append(0)
        tmp.append(0)
    return tmp


print(op([2,3,1,3],[4,1,1,5]))
        