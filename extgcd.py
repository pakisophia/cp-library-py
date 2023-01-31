#https://tjkendev.github.io/procon-library/python/math/gcd.html

#拡張ユークリッドの互除法
#ax+by=gcd(a,b) なる(x,y)。又gcd(a,b)を返す。

def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0
