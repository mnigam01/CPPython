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
    a,b,l = lst()
    if a==b==1:
        print(1)
        return

    s = set()
    for x in range(40):
        if (a**x)>l:
            break
        for y in range(40):
            if (a**x)*(b**y)>l:
                break
            k = l//((a**x)*(b**y))
            if k*(a**x)*(b**y)==l:
                s.add(k)
    print(len(s))          
    


t = 1
t = integer()

for _ in range(t):
    
    solve()

