import sys
sys.setrecursionlimit(500000000)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')


#DFS 無向グラフを想定
#入力
n,m=map(int,input().split())
g=[[] for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

   
seen=[False]*n #訪問したらTrueにする


def dfs(v): #再起でDFSを定義する
    seen[v]=True #vに到達したことを表す
    for i in g[v]:
       if seen[i]==True: #iが探索済みならパス
          continue
       else:
          dfs(i)
         
         
#なんかTLEとか出たらPython(3.8.2)提出で、lru_cache試そう




   


