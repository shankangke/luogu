# P2670 [NOIP2015 普及组] 扫雷游戏

(n,m)=map(int,input().split(" "))
a=list()

for i in range(n):
    b=list(input())
    a.append(b)

def count(i:int,j:int)->int:
    result = 0
    dirs=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
    for d in dirs:
        if i+d[0]>=0 and i+d[0]<n and j+d[1]>=0 and j+d[1]<m:
            if a[i+d[0]][j+d[1]]=='*':
                result+=1
    return result

for i in range(n):
    for j in range(m):
        if a[i][j] != '*':
            a[i][j]=count(i,j)
        print(a[i][j],end='')
    print()
