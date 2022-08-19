#入力
n,m = map(int,input().split())
e = [[] for _ in range(n)]
for _ in range(m):
    a,b,t = map(int,input().split())
    a,b = a-1, b-1
    e[a].append((t, b))
    e[b].append((t, a)) #有向グラフの場合　削除

INf=20**60

dp=[[INf for _ in range(n)] for _ in range(n)]
#dp[i][j]= iからjまでの最短距離

#dpの初期化
for i in range(n):
    dp[i][i]=0 #自分から自分へのコストは0

for i in range(n): #コスト入力　#今は有向グラフを想定
    for k,j in e[i]:
        dp[i][j]=k

#ワーシャルフロイドをやる
for k in range(n): #kを新たに用いることを考える
    for i in range(n):
        for j in range(n):
            dp[i][j]=min(dp[i][j],dp[i][k]+dp[k][j]) #新たに用いたkを使うか、使わないか選ぶ

#負閉路の存在判定
negativecycle=False

for v in range(n):
    if dp[v][v]<0: #dp[v][v]<0なるvが存在した場合、負閉路が存在
        negativecycle=True
    else:
        ()





            



    