def lst():
    return list(map(int, input().strip().split()))
import math

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

def solve():
    n,m, k = lst()
    l,r = min(n,m), int(1e25)
    lc = math.lcm(n,m)
    def cond(mid):
        cnt = mid//n + mid//m - 2*(mid//lc)
        # cout('dfdff',mid,cnt)
        return cnt>=k


    while (r-l)>2:
        mid = (l+r)>>1
        # cout(l,r,mid)
        if cond(mid):
            r = mid
        else:
            l = mid+1

    for i in range(max(min(n,m),l-3),r+5):
        cnt = i//n + i//m - 2*(i//lc)
        # cout(i)
        # cout(i,cnt)
        if cnt==k:
            print(i);return


t = 1



for _ in range(t):
    
    solve()

