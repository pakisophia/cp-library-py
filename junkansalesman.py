#AOJDPL2_A

V,E=map(int,input().split())

INf=2**60
g=[[INf]*V for _ in range(V)]

for i in range(E):
    s,t,d=map(int,input().split())

    g[s][t]=d

dp=[[INf]*V for _ in range(2**V)]   #dp[i][j]...iを二進数表現した時の集合とした時、つまり集合iの頂点を全て通った時かつ、その終点がjという頂点となる時の最短距離

dp[0][0]=0 # 0から出発するためdp[0][0]を0にする

for S in range(2**V): # Sは集合をbitで表している
    for v in range(V): # vは配られる側の要素を表している
        for u in range(V): # uは配る側の要素を表している
            if not (S >> u) & 1 and S != 0: #　①「頂点uに訪れていない」かつ、②「Sが空集合ではない」とき、continueする　#②を省かないと、dp[0][0]からの遷移が始まらない
                continue
            if (S >> v) & 1 == 0: #　もしまだvがSに含まれていない＝頂点vに訪れていないとき、{S}から{S+{v}}へと遷移させる
                if dp[S][u] + g[u][v] < dp[S | (1 << v)][v]:# もし、dp[{S}+{v}]が、更新されるとき
                    dp[S | (1 << v)][v] = dp[S][u] + g[u][v] 

                    # S | (1<<v) とすることで、集合Sのv頂点のところのbitを立たせてあげている

ans=dp[2**V-1][0] # 0→0の最短距離とi→iの最短距離は同じであるので、0→0のみ考えれば良い #


if ans==INf:
    print(-1)
else:
    print(dp[2**V-1][0])












        