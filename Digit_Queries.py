import copy
import sys, os, io
from collections import *
from bisect import *

import math
from math import sqrt
from heapq import heapify, heappop, heappush

#from functools import cache

from itertools import accumulate, product, combinations, combinations_with_replacement, permutations, groupby, cycle
from bisect import bisect_left, bisect_right
from string import ascii_lowercase,ascii_uppercase

#sys.setrecursionlimit(10**8)

mod = int(1e9) + 7
inf = float("inf")
# print(os.path.dirname(os.path.abspath(__file__)))
# input_file_path = os.path.dirname(os.path.abspath(__file__))
local_ = False
from io import BytesIO, IOBase
BUFSIZE = 4096
class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")

sys.stdout = IOWrapper(sys.stdout)
file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'in.txt')
# if os.path.exists(file_path): #os.path.exists('in.txt'):
if os.path.exists("C://Users//mridu//Python_Code//CPPython//in.txt"): #os.path.exists('in.txt'):
    local_ = True
if os.path.exists("in.txt"):
    sys.stdin = open("in.txt", "r")
    sys.stdout = open("out.txt", "w")

#input = sys.stdin.buffer.readline
input = sys.stdin.readline
#print = sys.stdout.write

def lst():
    return list(map(int, input().strip().split()))


def integer():
    return int(input())

def ceil(x,y):
    return int(-(-x  // y))

def st():
    s = input()
    if s[-1]=='\n':
        s = s[:-1]
    return s


def matrixNum(m):
    return [lst() for i in range(m)]

def matrixStr(m):
    return [st() for i in range(m)]

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
    # print(out)
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
# dir = {'U':[-1,0],'R':[0,1],'D':[1,0],'L':[0,-1]}
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
    def de(*args):
        e = ' '.join(map(str,args))
        sys.stderr.write(e+'\n')
        # print('==========',*args)

else:
    def de(*args):
        return 135
    

s = [0,9]

for i in range(18):
    s.append(s[-1]*10)
   
for i in range(1,len(s)):
    s[i] *= i
    s[i] += s[i-1]


def solve():
    
    n = integer()
    l,r = 1,len(s)
    while r-l>0:
        m = (l+r)>>1
        if s[m]>=n:
            r = m
        else:
            l = m+1
    n-=s[l-1]
    x = l
    l,r = 10**(l-1),10**(l)-1
    p = l
    while r-l>0:
        m=(l+r)>>1
        if x*(m-p+1)>=n:
            r = m
        else:
            l = m+1
    n-=x*(l-1-p+1)
    n-=1
    x = str(l)
    gh(x[n])
    
    


t = 1

t = integer()

for _ in range(t):
    de('testcase:',1+_)
    solve()

print("\n".join(map(str, ans)))

