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
    s = matrixStr(2)

    stk = [s[0][0]]
    f = 1
    for i in range(n):
        x,y = '4','4'
        x = s[0][i+1] if i+1<n else '3'
        y = s[1][i]
        if x==y:
            stk.append(x)
        elif f and x<y:
            stk.append(x)
            # f = 0
        else:
            stk.append(y)
            f = 0
    minim = ''.join(stk)
    # gh(minim)

    def h(f=0,ind=1):
        # cout(f,ind)
        if ind>=len(minim)-1:
            return 1
        if f==0:
            x = 0
            if minim[ind]==s[0][ind]:
                x += h(f,ind+1)
            if minim[ind]==s[1][ind-1]:
                x += h(1,ind+1)
            return x
        else:
            if minim[ind]==s[1][ind-1]:
                return h(f,ind+1)
            return 0

    x = h()
    print(minim)
    print(x)
            
    


t = integer()

for _ in range(t):
    
    solve()

