import random, time
import copy
import sys, os, io
from collections import *
from bisect import *

sys.setrecursionlimit(10**8)

import math
from math import sqrt
from heapq import heapify, heappop, heappush

from functools import cache

from itertools import accumulate, product, combinations, combinations_with_replacement, permutations, groupby, cycle
from bisect import bisect_left, bisect_right
from string import ascii_lowercase,ascii_uppercase

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
    return [st() for i in range(m)]

mod = int(1e9) + 7
inf = float("inf")

yes, no = "Yes", "No"

def mystery(l,r):
    r-=1
    return random.randint(l,r)

def ceil(x,y):
    return int(-(-x  // y))

def de(*args):
        return 135


def solve(*args):
    n,a = args[0]
    
    cnt = 0
    c = a[-1]
    fold = 1
    i = n-2
    while i>=0:
        de(i)
        x = 0
        f = 0
        while x<fold and i>=0: 
            if a[i]!=c:
                f = 1
            x+=1
            i-=1

        if f:
            cnt+=1
        fold*=2
    return cnt

    

    

def brute(*args):
    n,l = args[0]
    # a = matrixStr(m)
    i=n-1
    x=0
    c=0
    while(i>=0):
        if(l[i]==l[-1]):
            i-=1
            x+=1
        else:
            c+=1
            i-=x
            x*=2
    return c

start = time.time()

while True:

    try:
        # A = mystery(1,100000)
        # B = mystery(1,100000)
        # n = mystery(1,10000)
        # b = [mystery(1,10000) for i in range(n)]

        if time.time()-start>=10*3:
            print("Time 10sec reached")
            break

        n = mystery(1,6)
        # m = mystery(1,200)
        # x = mystery(1,n+1)
        choic = [' 1',' 0',' ?']
        # a = [str(mystery(1,n+1))+random.choice(choic) for i in range(m)]
        a = [mystery(1,n+1) for i in range(n)]
        t = [n,a]
        # print(t,solve(t),brute(t))
        if solve(t)!=brute(t):
            print(t);print("My Solution:-",solve(t));print("Brute Force Solution:-",brute(t))
            break

    except Exception as e:
        print(e)
        print('caught in except')
        print(t)
        break

