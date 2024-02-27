import copy
import sys, os, io
from collections import *
from bisect import *

import math
from math import sqrt
from heapq import heapify, heappop, heappush

#from functools import  cache

from itertools import accumulate, product, combinations, combinations_with_replacement, permutations, groupby, cycle
from bisect import bisect_left, bisect_right
from string import ascii_lowercase,ascii_uppercase

#sys.setrecursionlimit(10**8)

mod = int(1e9) + 7
inf = float("inf")
# print(os.path.dirname(os.path.abspath(__file__)))
# input_file_path = os.path.dirname(os.path.abspath(__file__))
local_ = False
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'in.txt')
if os.path.exists(file_path): #os.path.exists('in.txt'):
    local_ = True
if os.path.exists("in.txt"):
    sys.stdin = open("in.txt", "r")
    sys.stdout = open("out.txt", "w")

#input = sys.stdin.buffer.readline
#print = sys.stdout.write

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

class DSU:
    def __init__(self, n) -> None:
        self.rank = [0] * (n + 1)
        self.parent = [0] * (n + 1)

        for i in range(n + 1):
            self.parent[i] = i

    def find(self, x) -> int:
        if self.parent[x] == x:
            return x
        return self.find(self.parent[x])

    def union(self, a, b) -> int:
        x = self.find(a)
        y = self.find(b)

        if x == y:
            return 1

        if self.rank[x] < self.rank[y]:
            self.parent[x] = y

        elif self.rank[x] > self.rank[y]:
            self.parent[y] = x

        else:
            self.parent[y] = x
            self.rank[x] += 1

        return 0

def gh(out,s=' '):
    if isinstance(out, list):
        out = s.join(map(str, out))
    ans.append(out)

m = 1e1
_prime = [i for i in range(int(m+100))]
_prime[0] = _prime[1] = -1
for i in range(2,1+int(sqrt(len(_prime)))):
    if _prime[i] ==i:
        for j in range(i*i,len(_prime),i):
            _prime[j] = i

s = set()
for i in range(len(_prime)):
    if _prime[i]==i:
        s.add(i)

def djisktra(src,d):
    a = []
    vis = set()
    heappush(a,[0,src])
    p = defaultdict(lambda :inf)
    p[src] = 0

    while a:
        # print(a)
        _, node = heappop(a)
        if node in vis:
            continue
        vis.add(node)
        for j,weight in d[node]:
            if p[node]+weight<p[j]:
                p[j] = p[node]+weight
                heappush(a,[p[j],j])

    return p

yes, no = "Yes", "No"

ans = []


dir = [[0,1],[1,0],[0,-1],[-1,0],[1,-1],[-1,1],[1,1],[-1,-1]]
# dir = [[-1,-1],[-1,1],[1,1],[1,-1]]
# dir = {'U':[0,1],'R':[1,0],'D':[0,-1],'L':[-1,0]}
# dir = dir.values()
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
    
class fenwick_tree():
    n=1
    data=[0 for i in range(n)]
    def __init__(self,N):
        self.n=N
        self.data=[0 for i in range(N)]

    def add(self,p,x):
        assert 0<=p<self.n,"0<=p<n,p={0},n={1}".format(p,self.n)

        p+=1
        while(p<=self.n):
            self.data[p-1]+=x
            p += p&(-p)
    def sum(self,l,r):
        assert (0<=l and l<=r and r<=self.n),"0<=l<=r<=n,l={0},r={1},n={2}".format(l,r,self.n)
        return self.sum0(r)-self.sum0(l)
    def sum0(self,r):
        s=0
        while(r>0):
            s+=self.data[r-1]
            r-=r&-r
        return s

    def __getitem__(self, p):
        if isinstance(p, int):
            return self.sum(p, p + 1)
        else:
            return self.sum(p.start, p.stop)

    def __setitem__(self, p, x):
        return self.add(p, x - self[p])

def solve():
    # print(str.rjust(20, "O")
    # m = str(m).rjust(2,'0')
   
    mini = inf
    maxi = -inf
    n,q = lst()   # number of elements in a and q is number of queries
    a = lst()  # taking input of a
    print(a)

    fen = fenwick_tree(n+10)
    # dif = [a[0]]

    # for i in range(1,n):
    #     dif.append(a[i]-a[i-1])
    
    # for i in range(n):
    #     l,r = i+1,i+1
    #     print(l,r,a[i])
    #     fen.add(l-1,a[i])
    #     fen.add(r-1,-a[i])
    #     break

    # for i in range(n):
    #     fen.add(i,a[i])
    #     fen.add(i+1,-a[i])

    cout(fen.data)
    # cout(fen.__getitem__(3))

    for _ in range(q):
        l = lst()
        
        # if l[0]==1:
        #     fen.add(l[1]+1,l[-1])
        #     fen.add(l[2]+2,-l[-1])

        # else:
        #     idx = l[1]
        #     ret = 0
        #     # idx += 1
        #     while idx > 0:
        #         ret += fen.data[idx]
        #         idx -= idx & (-idx)
            

        #     gh(ret)

        # gh(fen.data)

        if l[0]==1:
            fen.add(l[1]-1,l[-1])
            fen.add(l[2]-1,-l[-1])

        else:
            idx = l[1]-1
            ret = 0
            while idx > 0:
                ret += fen.data[idx]
                idx -= idx & (-idx)
            

            gh(ret+a[l[1]-1])

        # gh(fen.data)
    


t = 1

# t = integer()

for _ in range(t):
    # cout('testcase:',1+_)
    solve()

print("\n".join(map(str, ans)))

#convert to c++