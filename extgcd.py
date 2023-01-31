#https://tjkendev.github.io/procon-library/python/math/gcd.html

#拡張ユークリッドの互除法
#ax+by=gcd(a,b)なる(x,y)を求める。
#第一返り値としてgcd(a,b)。第二、三返り値として(x,y)を返す。

def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0
