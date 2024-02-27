import copy,sys, os, io,math
from collections import *
from bisect import *

from heapq import heapify, heappop, heappush
from bisect import bisect_left, bisect_right
from string import ascii_lowercase,ascii_uppercase

mod = int(1e9) + 7
inf = float("inf")

local_ = False

def lst():
    return list(map(int, input().strip().split()))


def integer():
    return int(input())

def ceil(x,y):
    return int(-(-x  // y))

def st():
    return input()

def matrixNum(m):
    return [lst() for i in range(m)]

def matrixStr(m):
    return [list(st()) for i in range(m)]


def h():
    n = lst()
    a = lst()
    return *n,a

def hh():
    n = lst()
    a = [integer() for i in range(n[0])]
    return *n,a

if local_:
    def cout(*args):
        print(*args)

else:
    def cout(*args):
        return 135


yes, no = "Yes", "No"

ans = []

def gh(out,s=' '):
    if isinstance(out, list):
        out = s.join(map(str, out))
    ans.append(out)

class SGTree:
    def __init__(self,a) -> None:
        n = len(a)
        self.seg = [0]*(4*n+1)
        self.build(0,0,n-1,a)

    def build(self,ind,low,high,a):
        if low==high:
            self.seg[ind] = a[ind]
            return
        mid = (low+high)>>1
        self.build(2*ind+1,low,mid,a)
        self.build(2*ind+2,mid+1,high,a)

        # change logic here
        self.seg[ind] = min(self.seg[ind*2+1],self.seg[ind*2+2])
    
    def query(self,ind,low,high,l,r):
        if high<l or r<low:
            return inf
        if l<=low<=high<=r:
            return self.seg[ind]
        
        # change logic here
        mid = (low+high)>>1
        x = self.query(2*ind+1,low,mid,l,r)
        y = self.query(2*ind+2,mid+1,high,l,r)
        return min(x,y)
    
    def update(self,ind,low,high,i,val):
        if low==high:
            self.seg[ind]=val
            return
        mid = (low+high)>>1
        if i<=mid:
            self.update(ind,low,mid,i,val)
        else:
            self.update(ind,mid+1,high,i,val)
        
        #change logic here
        self.seg[ind] = min(self.seg[ind*2+1],self.seg[ind*2+2])


def solve():


    mini = inf
    maxi = -inf

    for k in range(14,50):
        x = list(range(1,k+1))+list(range(k-1,1,-1))
        if k==14:
            print('dfdfdf',len(x))
        x = x*3
        print(x[:76])
        # print(k,len(x))
        # if k<11:
        #     print(k,x)
        if x[75]==4:
            print(k)
        break




t = 1

t = integer()

for _ in range(t):
    solve()

print("\n".join(map(str, ans)))
