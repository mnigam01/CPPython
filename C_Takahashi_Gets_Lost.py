

mod = int(1e9) + 7
inf = float("inf")


def lst():
    return list(map(int, input().strip().split()))


def integer():
    return int(input())


def st():
    return input()


def matrixStr(m):
    return [list(st()) for i in range(m)]


dir = {'U':[-1,0],'R':[0,1],'D':[1,0],'L':[0,-1]}


def solve():
    r,c,n = lst()
    s = st()
    sp = matrixStr(r)
    def h(i,j):
        print(i,j)
        for d in s:
            i += dir[d][0]
            j += dir[d][1]
            if 0<=i<r and 0<=j<c:
                if sp[i][j]=='#':return False
            else:
                return False
        return sp[i][j]=='.' 
    cnt = 0
    for i in range(r):
        for j in range(c):
            if sp[i][j]=='.' and h(i,j):
                cnt+=1
    print(cnt)




                

solve()
