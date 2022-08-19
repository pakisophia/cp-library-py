# ある頂点から他の頂点への最短距離
# 負辺を持っていても利用可能
# 最低(V-1)回、すべての辺を見れば求まる

# O(|V||E|)
# sを始点としている

INf=2**60

def bellman_ford(s):
    d = [INf]*n # 各頂点への最小コスト
    d[s] = 0 # 自身への距離は0
    for i in range(n):
        update = False # 更新が行われたか
        for j in range(n):
            for w, k in e[j]:
                if d[j]==INf:
                    continue #頂点sから届かないものは緩和しない
                if d[k] > d[j] + w:
                    d[k] = d[j] + w
                    update = True
            if not update:
                break
            
            # 負閉路が存在
            # n(v)回目で更新された
            if i == n - 1:
                return -1
        return d

#入力
n,m = map(int,input().split())
e = [[] for _ in range(n)]
for _ in range(m):
    a,b,t = map(int,input().split())
    a,b = a-1, b-1
    e[a].append((t, b))
    e[b].append((t, a)) #有向グラフの場合　削除
print(bellman_ford(0))