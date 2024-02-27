import copy
import sys, os, io
from collections import *
from bisect import *

import math
from math import sqrt
from heapq import heapify, heappop, heappush


def matrixStr(m):
    return [input() for i in range(m)]

dir = {'U':[0,1],'R':[1,0],'D':[0,-1],'L':[-1,0]}
dir = dir.values()
inf = float('inf')

def solve():
    
    n = int(input())
    N = n
    a = matrixStr(n)
    t = []
    for i in range(n):
        
        for j in range(n):
            if a[i][j]=='P':
                t.append([i,j])
    (x1,y1),(x2,y2) = t
    q = deque([[x1*60+y1,x2*60+y2]])
    d = [[inf]*4000 for i in range(4000)]
    d[x1*60+y1][x2*60+y2] = 0
    while q:
        (a1,b) = q.popleft()

        x1,y1 = a1//60,a1%60
        x2,y2 = b//60,b%60
        
        if x1==x2 and y1==y2:
            print(d[x1*60+y1][x2*60+y2])
            return
        # print(x1,y1,x2,y2)
        for dx,dy in dir:
            nx1,ny1 = x1,y1
            nx2,ny2 = x2,y2
            # print(x1+dx)
            if 0<=x1+dx<N and a[x1+dx][y1]!='#':
                nx1+=dx
            if 0<=x2+dx<N and a[x2+dx][y2]!='#':
                nx2+=dx
            if 0<=y1+dy<N and a[x1][y1+dy]!='#':
                ny1+=dy
            if 0<=y2+dy<N and a[x2][y2+dy]!='#':
                ny2+=dy
            if d[nx1*60+ny1][nx2*60+ny2]>d[x1*60+y1][x2*60+y2]+1:
                d[nx1*60+ny1][nx2*60+ny2]=d[x1*60+y1][x2*60+y2]+1
                q.append([nx1*60+ny1,nx2*60+ny2])
    print(-1)

                    
solve()

