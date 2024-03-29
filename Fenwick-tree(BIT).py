"https://qiita.com/R_olldIce/items/f2f7930e7f67963f0493" #元サイト

#listの要素に加算、区間和を高速に処理できる


class Fenwick_Tree:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n

    def add(self, p, x): #index=pにxを加算する
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, l, r): #半開区間[l,r)の合計値が求まる
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)

    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s

