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
    s = st()
    dp = [0]*(n+1)
    if s[n-1]=='.':
        dp[n-1] = 0
    elif s[n-1] == '@':
        dp[n-1] = 1
    else:
        pass
    if n-2>=0:
        if s[n-2]=='.':
            dp[n-2] = dp[n-1]
        elif s[n-2] == '@':
            dp[n-2] = 1+dp[n-1]
        else:
            pass
    
    for i in range(n-3,-1,-1):
        if s[i]=='*':
            dp[i] = 0
        elif s[i]=='.':
            dp[i] = max(dp[i+1],dp[i+2])
        else:
            dp[i] = 1+max(dp[i+1],dp[i+2])
    print(dp[0])


t = integer()



for _ in range(t):
    
    solve()

