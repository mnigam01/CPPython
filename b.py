import random
import copy
import sys, os, io
from collections import *
from bisect import *

import math
from math import sqrt
from heapq import heapify, heappop, heappush

from functools import cache

from itertools import accumulate, product, combinations, combinations_with_replacement, permutations, groupby, cycle
from bisect import bisect_left, bisect_right
from string import ascii_lowercase,ascii_uppercase


mod = int(1e9) + 7
inf = float("inf")
local_ = False

yes, no = "Yes", "No"

def mystery(l,r):
    r-=1
    return random.randint(l,r)

def ceil(x,y):
    return int(-(-x  // y))

def solve(n,a):
    
    res = [inf]*n
    p = [0]*(n+5)
    for i in range(n):
        p[i+1] = p[i]+a[i]

    cnt = [0]*(n+5)
    cnt[1] = 1
    for i in range(1,n):
        cnt[i+1] = cnt[i] + (1 if a[i-1]!=a[i] else 0)

    for i in range(n):
        if i-1>=0 and a[i-1]>a[i]:
            res[i] = 1
        if i+1<n and a[i+1]>a[i]:
            res[i] = 1
        
        if res[i] ==1:
            continue

        l,r = 0,i-2
        prv = inf
        

        while r-l>-1:
            m = (l+r)>>1
            tot = p[i]-p[m]
            c = cnt[i]-cnt[m]
            if tot>a[i] and c>1:
                prv = min(prv,i-m)
                l = m+1
            else:
                r = m-1
        
        res[i] = prv

        # cout(res)

        l,r = i+2,n-1
        prv = inf
        

        while r-l>-1:
            m = (l+r)>>1
            tot = p[m+1]-p[i+1]
            c = cnt[m+1]-cnt[i+1]
            # cout(i,l,r,m,tot,c)
            if tot>a[i] and c>1:
                prv = min(prv,m+1-(i+1))
                r = m-1
            else:
                l = m+1
        
        res[i] = min(res[i],prv)
    
    for i in range(len(res)):
        if res[i]==inf:
            res[i] = -1
    return (res)

    

def brute(n,a):
    # n,a = h()
    res = [inf]*n
    for i in range(n):
        tot = 0
        s = set()
        for j in range(i+1,n):
            tot+=a[j]
            if tot>a[i] and len(s)==0:
                res[i] = 1
                break
            s.add(a[j])
            if tot>a[i] and len(s)>1:
                res[i] = (j-i)
                break
 
    for i in range(n):
        tot = 0
        s = set()
        for j in range(i-1,-1,-1):
            tot+=a[j]
            if tot>a[i] and len(s)==0:
                res[i] = min(res[i],1)
                break
            s.add(a[j])
            if tot>a[i] and len(s)>1:
                res[i] = min(res[i],i-j)
                break
    
    for i in range(n):
        if res[i]==inf:
            res[i]=-1
    return (res)

A = mystery(1,100000)
B = mystery(1,100000)
n = mystery(1,10000)
b = [mystery(1,10000) for i in range(n)]

n = mystery(1,10)
a = [mystery(1,30) for i in range(n)]

while solve(n,a)==brute(n,a):
    n = mystery(1,10)
    a = [mystery(1,30) for i in range(n)]
    # A = mystery(1,10)
    # B = mystery(1,10)
    # n = mystery(1,10)
    # a = [mystery(1,10) for i in range(n)]
    # b = [mystery(1,10) for i in range(n)]
    # n = mystery(0,30)
    # k = mystery(0,30)
# print(A,B,n,a,b)
print(n,a)
print(solve(n,a),brute(n,a))
