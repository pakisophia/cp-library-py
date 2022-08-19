#有向グラフを想定
n,m=map(int,input().split())
g=[[] for _ in range(n)]
topo=[] 
ans=[]
for i in range(m):
    a,b=map(int,input().split())
    g[a-1].append(b-1)

seen=[False]*n #訪問したらTrueにする
def dfs(v):
    seen[v]=True
    for i in g[v]:
        if seen[i]==True:
            continue
        else:
            dfs(i)

    topo.append(v)

for i in range(n):
    if seen[i]==True:
        ()
    else:
        dfs(i)
    
    

for i in range(n):
    ans.append(topo[n-1-i]+1) #逆順にする #-1したのを元に戻す

print(*ans)

    





    