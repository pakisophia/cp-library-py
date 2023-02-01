#https://tjkendev.github.io/procon-library/python/math/gcd.html

#拡張ユークリッドの互除法
#ax+by=gcd(a,b)なる(x,y)を求める。
#第一返り値としてgcd(a,b)。第二、三返り値として(x,y)を返す。

def xgcd(a, b):
    x0, y0, x1, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return a, x0, y0

#拡張ユークリッドの互除法を使ってaの法mでの逆元を求める
def modinv(a, m):
    g, x, y = xgcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m
