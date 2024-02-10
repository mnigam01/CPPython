import copy,sys, os, io,math
from functools import cache
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

def solve():


    mini = inf
    maxi = -inf

    n = integer()
    d = defaultdict(list)
    for i in range(n-1):
        a,b,c = lst()
        d[i+1].append([i+2,a])
        d[i+1].append([c,b])
    
    out = djisktra(1,d)
    cout(out)
    gh(out[n])



t = 1

#t = integer()

for _ in range(t):
    solve()

print("\n".join(map(str, ans)))
