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

from typing import List, Iterable, Sequence, Union

class FenwickTreeRAQ():
  
  
  def __init__(self, n_or_a: Union[Iterable[int], int]):
    if isinstance(n_or_a, int):
      self.n = n_or_a
      self.bit0 = [0] * (n_or_a + 2)
      self.bit1 = [0] * (n_or_a + 2)
      self.bit_size = self.n + 1
    else:
      if not isinstance(n_or_a, Sequence):
        n_or_a = list(n_or_a)
      self.n = len(n_or_a)
      self.bit0 = [0] * (self.n + 2)
      self.bit1 = [0] * (self.n + 2)
      self.bit_size = self.n + 1
      for i, e in enumerate(n_or_a):
        self.add_range(i, i+1, e)

  def __add(self, bit: List[int], k: int, x: int) -> None:
    k += 1
    while k <= self.bit_size:
      bit[k] += x
      k += k & -k

  def __pref(self, bit: List[int], r: int) -> int:
    ret = 0
    while r > 0:
      ret += bit[r]
      r -= r & -r
    return ret

  def add(self, k: int, x: int) -> None:
    assert 0 <= k < self.n, \
        f'IndexError: FenwickTreeRAQ.add({k}, {x}), n={self.n}'
    self.add_range(k, k+1, x)

  def add_range(self, l: int, r: int, x: int) -> None:
    assert 0 <= l <= r <= self.n, \
        f'IndexError: FenwickTreeRAQ.add_range({l}, {r}, {x}), l={l},r={r},n={self.n}'
    self.__add(self.bit0, l, -x*l)
    self.__add(self.bit0, r, x*r)
    self.__add(self.bit1, l, x)
    self.__add(self.bit1, r, -x)

  def sum(self, l: int, r: int) -> int:
    assert 0 <= l <= r <= self.n, \
        f'IndexError: FenwickTreeRAQ.sum({l}, {r}), l={l},r={r},n={self.n}'
    return self.__pref(self.bit0, r) + r*self.__pref(self.bit1, r) - self.__pref(self.bit0, l) - l*self.__pref(self.bit1, l)

  def tolist(self) -> List[int]:
    return [self.sum(i, i+1) for i in range(self.n)]

  def __getitem__(self, k: int) -> int:
    assert 0 <= k < self.n, \
        f'IndexError: FenwickTreeRAQ.__getitem__({k}), n={self.n}'
    return self.sum(k, k+1)

  def __str__(self):
    return '[' + ', '.join(map(str, (self.sum(i, i+1) for i in range(self.n)))) + ']'

  def __repr__(self):
    return f'FenwickTreeRAQ({self})'


def solve():
    # print(str.rjust(20, "O")
    # m = str(m).rjust(2,'0')
   
    mini = inf
    maxi = -inf
    n,m = lst()
    a = lst()
    b = lst()

    fw = FenwickTreeRAQ(a)
    for i in b:
       val = fw.__getitem__(i)
    #    cout(val)
       fw.add(i,-val)
       fw.add_range(0,n,val//n)
       rem = val%n
    #    cout(rem)
       mini = min(rem,n-(i+1))
    #    cout(i+1,i+mini+1)
    #    cout()
       fw.add_range(i+1,i+mini+1,1)
       rem -= mini
       fw.add_range(0,rem,1)
    #    cout(fw.tolist())
    #    fw.

    x = fw.tolist()
    gh(x)
    # dif = [a[0]]
    # for i in range(1,n):
    #     dif.append(a[i]-a[i-1])
    # dif.append(0)
    # for i in b:
    #     if i==0:
    #         val = dif[0]
    #     else:
    #         val = dif[0]
    #         for j in range(1,i+1):
    #             val += dif[j]
    #     # cout(dif)
    #     full = val//n
    #     dif[i]+=-val
    #     dif[i+1]-=-val
    #     dif[0]+=full
    #     dif[-1]-=full
    #     rem = val%n
    #     x = min(rem,n-(i+1))
    #     dif[i+1]+=1
    #     dif[i+x+1]-=1
    #     rem -= x
    #     if rem>0:
    #         dif[0]+=1
    #         dif[rem]-=1
    
    # out = [dif[0]]
    # for i in range(1,n):
    #     out.append(out[-1]+dif[i])
    # gh(out)

        

    


t = 1

#t = integer()

for _ in range(t):
    # cout('testcase:',1+_)
    solve()

print("\n".join(map(str, ans)))

#convert to c++