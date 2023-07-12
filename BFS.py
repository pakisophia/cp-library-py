import sys
input = sys.stdin.readline

#入力
n, m = map(int,input().split()) # nは頂点の数、mは辺の数
g = [[] for _ in range(n)] # 隣接リスト

for _ in range(m):
    a, b = [int(x) for x in input().split()]
    g[a-1].append(b-1)
    g[b-1].append(a-1)


#ここからBFS本編
from collections import deque

INf=1e18
seen=[False]*n #訪問したらTrueにする

def bfs(u):
    queue = deque([u])
    d = [INf] * n # uからの距離の初期化
    d[u] = 0 # 自分との距離は0
   
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i]==INf:
                d[i] = d[v] + 1
                seen[i] = True

                queue.append(i)
    return d



