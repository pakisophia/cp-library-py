INf=2**60
from collections import deque

def bfs01(u):
    queue = deque([u])
    d = [INf] * k # uからの距離の初期化
    d[u] = 0 # 自分との距離は0
   
    while queue:
        v = queue.popleft()
        for i,j in g[v]:
            if j==0 and d[v]<d[i]:
                d[i]=d[v]
                queue.appendleft(i)
            elif j==1 and d[v]+1<d[i]:
                d[i]=d[v]+1
                queue.append(i)
