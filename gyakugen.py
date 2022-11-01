#https://qiita.com/drken/items/3b4fdf0a78e7a138cd9a

#フェルマーの小定理を用いたもの

#modxの元でのaの逆元
def gyakugen(a,modx):
    return pow(a,modx-2,modx)

print(gyakugen(2,998244353))











        