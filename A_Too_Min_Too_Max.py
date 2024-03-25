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

def solve():
    maxi = 0
    n,a = integer(),lst()
    a.sort()
    i = 0
    l = n-1

    for j in range(n):
        for k in range(n):
            if len(set([i,j,k,l]))!=4:
                continue
            maxi = max(maxi,abs(a[i]-a[j])+abs(a[j]-a[k])+abs(a[k]-a[l])+abs(a[l]-a[i]))
    print(maxi)


t = 1
t = integer()

for _ in range(t):
    
    solve()

