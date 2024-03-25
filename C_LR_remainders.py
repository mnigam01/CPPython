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
    def cout(*args):
        e = ' '.join(map(str,args))
        sys.stderr.write(e+'\n')
        # print('==========',*args)

else:
    def cout(*args):
        return 135

class sparsetable:
 
    def __init__(self , function , bound = 1):
        self.b = None
        self.block = None
        self.n = None
        self.size = None
        self.bound = bound
        self.function = function
 
    def construct(self , a):
 
        self.n = len(a)
        for i in range(30):
            if(self.n < (1 << i)):
                self.size = i
                break
 
        self.b = [[self.bound for i in range(self.size)] for j in range(self.n)]
        self.block = [-1 for i in range(self.n + 1)]
 
        for i in range(self.n):
            self.b[i][0] = a[i]
        
        for j in range(1 , self.size):
            for i in range(self.n - (1 << (j - 1))):
                self.b[i][j] = self.function(self.b[i][j - 1] , self.b[i + (1 << (j - 1))][j - 1])
        
        for i in range(1 , self.n + 1):
            for j in range(self.size - 1 , -1 , -1):
                if(i >= (1 << j)):
                    self.block[i] = j
                    break
 
    def query(self , l , r):
        r-=1
 
        #handle cases if required
        dist = r - l + 1
 
        ans = self.function(self.b[l][self.block[dist]] , self.b[r - (1 << self.block[dist]) + 1][self.block[dist]])
        return ans
        
    
    def log_query(self , l , r):
        r -= 1
 
        #handle cases if required
        dist = r - l + 1
 
        ans = self.bound
        for i in range(self.size - 1 , -1 , -1):
            if(dist >> i & 1):
                ans = self.function(ans , self.b[l][i])
                l += (1 << i)
 
        return ans
 

def solve():
    
    n,m = lst()
    a = lst()
    s = st()
    sp = sparsetable(lambda x,y:(x*y)%m,1)
    sp.construct(a)
    res = []
    
    l=0
    r = n
    for i in s:
        res.append(sp.log_query(l,r))
        if i=='L':
            l+=1
        else:
            r-=1
    gh(res)
        
        
    # table = sparsetable(lambda x,y:(x*y)%m,1)
    # table.construct(a)
    # l,r = 0,n
    # res = []
    # for i in s:
    #     x = table.query(l,r)
    #     res.append(x%m)
    #     if i=='L':
    #         l+=1
    #     else:
    #         r-=1
    # gh(res)

    
    


t = 1

t = integer()

for _ in range(t):
    cout('testcase:',1+_)
    solve()

print("\n".join(map(str, ans)))

