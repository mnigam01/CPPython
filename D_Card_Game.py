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
    t = st()
    a = st().split()
    a.sort(key=lambda x:(x[1],x[0]))
    # cout(a)
    a1,b1 = [],[]
    for i in a:
        if t in i:
            b1.append(i)
        else:
            a1.append(i)
    res = []
    f = 0
    i = 0
    while i<len(a1)-1:
        if a1[i][1]==a1[i+1][1]:
            res.append([a1[i],a1[i+1]])
            i+=2
        else:
            if len(b1):
                res.append([a1[i],b1[0]])
                i+=1
                b1.pop(0)

            else:
                f = 1
                break

    if f:
        print('IMPOSSIBLE');return
    # check for remainin item
    if i<len(a1):
        if len(b1):
            res.append([a1[i],b1[0]])
            i+=1
            b1.pop(0)

        else:
            f = 1
    if f:
        print('IMPOSSIBLE');return
    
    i = 0
    while i<len(b1)-1:
        res.append([b1[i],b1[i+1]])
        i+=2

    if i<len(b1):
        f = 1


    if f:
        print('IMPOSSIBLE');return
    
    for i in res:
        print(i[0],i[1])


t = integer()



for _ in range(t):
    
    solve()

