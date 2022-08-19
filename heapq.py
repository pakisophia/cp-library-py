#優先度付きキュー
x=None
a=[]

import heapq
heapq.heapify(list) #リストを優先度付きキューに変換。
heapq.heappop(list) #優先度付きキューから最小値を取り出す。
heapq.heappush(list,x) #優先度付きキューに要素を挿入。

#最大値を取り出す
import heapq
a = list(map(lambda x: x*(-1), a))  # 各要素を-1倍
print(a)

heapq.heapify(a)
print(heapq.heappop(a)*(-1))  # 最大値の取り出し
print(a)