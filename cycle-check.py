#有向グラフのサイクルの有無を判定
#無向グラフの場合は、Union-Findで判定可能


#入力
n,m=map(int,input().split())
g=[[] for _ in range(n)]

#訪問したらTrueにする　
seenin=[False]*n #seenin=行きがけ(関数呼び出しのタイミング)
seenout=[False]*n #seenout=帰りがけ(関数から出るタイミング)

cycle=False #cycleがTrueならサイクルあり

def dfs(v):
    if seenin[v]==True and seenout[v]==False: #帰ってきてないのに到達してしまった
        global cycle
        cycle=True
    else:
        seenin[v]=True
        for i in g[v]:
            if seenin[i]==True and seenout[i]==True:
                continue
            else:
                dfs(i)

    seenout[v]=True
    

for i in range(n):
    if seenin[i]==True:
        ()
    else:
        dfs(i)

if cycle:
    print("No")
else:
    print("Yes")
