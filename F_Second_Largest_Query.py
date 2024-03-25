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
    def de(*args):
        e = ' '.join(map(str,args))
        sys.stderr.write(e+'\n')
        # print('==========',*args)

else:
    def de(*args):
        return 135
    
class segtree():
    n=1;size=1;log=2;d=[0];op=None;e=10**15
    def __init__(self,V,OP,E):
        self.n=len(V);self.op=OP;self.e=E;self.log=(self.n-1).bit_length();self.size=1<<self.log;self.d=[E for i in range(2*self.size)]
        for i in range(self.n):self.d[self.size+i]=V[i]
        for i in range(self.size-1,0,-1):self.update(i)
    def set(self,p,x):
        assert 0<=p and p<self.n
        p+=self.size;self.d[p]=x
        for i in range(1,self.log+1):self.update(p>>i)
    def get(self,p):
        assert 0<=p and p<self.n
        return self.d[p+self.size]
    def prod(self,l,r):
        assert 0<=l and l<=r and r<=self.n
        sml=self.e;smr=self.e;l+=self.size;r+=self.size
        while(l<r):
            if (l&1):sml=self.op(sml,self.d[l]);l+=1
            if (r&1):smr=self.op(self.d[r-1],smr);r-=1
            l>>=1;r>>=1
        return self.op(sml,smr)
    def all_prod(self):
        return self.d[1]
    def max_right(self,l,f):
        assert 0<=l and l<=self.n
        assert f(self.e)
        if l==self.n:return self.n
        l+=self.size;sm=self.e
        while(1):
            while(l%2==0):l>>=1
            if not(f(self.op(sm,self.d[l]))):
                while(l<self.size):
                    l=2*l
                    if f(self.op(sm,self.d[l])):sm=self.op(sm,self.d[l]);l+=1
                return l-self.size
            sm=self.op(sm,self.d[l]);l+=1
            if (l&-l)==l:break
        return self.n
    def min_left(self,r,f):
        assert 0<=r and r<=self.n
        assert f(self.e)
        if r==0:return 0
        r+=self.size;sm=self.e
        while(1):
            r-=1
            while(r>1 and (r%2)):r>>=1
            if not(f(self.op(self.d[r],sm))):
                while(r<self.size):
                    r=(2*r+1)
                    if f(self.op(self.d[r],sm)):sm=self.op(self.d[r],sm);r-=1
                return r+1-self.size
            sm=self.op(self.d[r],sm)
            if (r& -r)==r:break
        return 0
    def update(self,k):
        self.d[k]=self.op(self.d[2*k],self.d[2*k+1])
    def __str__(self):
        return str([self.get(i) for i in range(self.n)])

# def func(a,b):
#     return a^b
    
# seg = segtree(a,max,-inf)

from random import randint




def solve():
    # print(str.rjust(20, "O")
    # m = str(m).rjust(2,'0')
   
    n,q = lst()
    a = lst()
    def op(x,y):
        d = defaultdict(int)
        d[x[0]] += x[1]
        d[y[0]] += y[1]
        d[x[2]] += x[3]
        d[y[2]] += y[3]
        p = sorted(d.items(),key=lambda x:(-x[0]))
        # p = [list(i) for i in p]
        tmp = [*p[0]]
        if len(p)!=1:
            tmp.append(p[1][0])
            tmp.append(p[1][1])
        else:
            tmp.append(0)
            tmp.append(0)
        return tmp

        
        

        maxx, max_countx, secondx, second_countx = x
        maxy, max_county, secondy, second_county = y    
        if maxx==maxy:
            if secondx==secondy:
                return [maxx,max_countx+max_county,secondx,second_countx+second_county]
            elif secondx>secondy:
                return [maxx,max_countx+max_county,secondx,second_countx]
            else:
                return [maxx,max_countx+max_county,secondy,second_county]
        elif maxx>maxy:
            if secondx==maxy:
                return [maxx,max_countx,secondx,second_countx+max_county]
            elif secondx>maxy:
                return [maxx,max_countx,secondx,second_countx]
            else:
                return [maxx,max_countx,maxy,max_county]
        else:
            if secondy==maxx:
                return [maxy,max_county,secondy,second_county+max_countx]
            elif secondy>maxx:
                return [maxy,max_county,secondy,second_county]
            else:
                return [maxy,max_county,maxx,max_countx]





    seg = segtree([[i,1,0,0] for i in a],op,[0,0,0,0])
    for _ in range(q):
        c,l,r = lst()
        if c == 1:
            seg.set(l-1,[r,1,0,0])
        else:
            cnt = seg.prod(l-1,r)
            gh(cnt[-1])
            # de(cnt)
            
    

t = 1

# t = integer()

for _ in range(t):
    de('testcase:',1+_)
    solve()

print("\n".join(map(str, ans)))


