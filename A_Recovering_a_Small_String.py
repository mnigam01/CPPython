import copy
import sys, os, io

from string import ascii_lowercase,ascii_uppercase


def integer():
    return int(input())

def lst():
    return list(map(int, input().strip().split()))

from collections import Counter
def solve():
    
    n = integer()
    a = lst()
    d = Counter(a)
    if len(d)==1:
        print(0)
        return
    l,r = 1, n-1
    while l<n and a[l]==a[0]:
        l+=1
    res = (r-l+1)
    l,r = 0,n-2
    while r>=0 and a[r]==a[-1]:
        r-=1
    res = min(res,r-l+1)
    if a[0]==a[-1]:
        l,r = 0,n-1
        while l<n and a[l]==a[0]:
            l+=1
        while r>=0 and a[r]==a[-1]:
            r-=1
        res = min(res,r-l+1)
    print(res)



t = integer()

for _ in range(t):
    solve()

