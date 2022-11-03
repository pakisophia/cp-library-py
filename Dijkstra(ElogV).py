import heapq

def dijkstra1(s):
    hq = [(0, s)]
    INf=1e18
    heapq.heapify(hq) # リストを優先度付きキューに変換
    cost = [INf] * n # 行ったことのないところはinf
    cost[s] = 0 # 開始地点は0
    while hq:
        c, v = heapq.heappop(hq)
        if c > cost[v]: # コストが現在のコストよりも高ければスルー
            continue
        for d, u in g[v]:
            tmp = d + cost[v]
            if tmp < cost[u]:
                cost[u] = tmp
                heapq.heappush(hq, (tmp, u))
    return cost

#入力
n,m = map(int,input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a,b,t = map(int,input().split())
    a,b = a-1, b-1
    g[a].append((t, b))
    g[b].append((t, a)) #有向グラフでは削除
