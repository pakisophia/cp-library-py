#入力
n=int(input())
g=[[] for _ in range(n)]

'''↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓'''

#dfsで0と1に色分けする

seen=[False]*n

#liはlistの引数　これに頂点の色が格納されていく
def dfs(v,cur,li): #再起でDFSを定義する
    seen[v]=True
 
    li[v]=cur #vに到達したことを表す
    for i in g[v]:
        if li[i]!=-1: 
            if li[i]==cur:
                return False #もし色が既に塗られていて、それが今見ている色と同じだった時
            
            continue
 
        if dfs(i,1-cur,li)==False: #返り値でFalseが帰ってきた時、Falseをそのまま返す
            return False






