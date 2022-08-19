#入力
n,m = map(int,input().split())
e = [[] for _ in range(n)]
for _ in range(m):
    a,b,t = map(int,input().split())
    a,b = a-1, b-1
    e[a].append((t, b))
    e[b].append((t, a)) #有向グラフの場合　削除

def dijkstra2(s):
    INf=20**60
    used=[False]*n
    cost=[INf]*n
    cost[s]=0

    for i in range(n): 
        mincost=INf
        minver=-1
        
        for v in range(n):
            if used[v]==False and cost[v]<mincost:
                mincost=cost[v]
                minver=v
            else:
                ()

        if minver==-1:
            break

        for w,p in e[minver]: #minverから緩和
            cost[p]=min(cost[p],cost[minver]+w)
        
        used[minver]=True

        
        


