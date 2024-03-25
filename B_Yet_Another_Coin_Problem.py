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
    n = integer()
    x = n//15
    x = max(0,x-3)
    cnt = x
    n -= x*15
    dp = [int(1e9)]*(300)
    dp[0] = 0
    for i in range(len(dp)):
        for j in [1,3,6,10,15]:
            if i-j>=0:
                dp[i] = min(dp[i],dp[i-j]+1)

    cnt += dp[n]
    print(cnt)


t = 1
t = integer()

for _ in range(t):
    
    solve()

