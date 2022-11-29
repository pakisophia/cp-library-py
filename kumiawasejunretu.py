import itertools
import math
l=["a","b","c","d"]

#順列の値を返す
def perm(a,b):
    return math.perm(a,b)
    #aPbの値を返す

#組み合わせの数を列挙
def comb(a,b):
    return math.comb(a,b)
    #aCbの値を返す

#順列列挙
c=itertools.permutations(l,2)
#この場合4P2(=12個)の順列がlist(c)に格納される

#組み合わせ集合を列挙
cc=itertools.combinations(l,2)
#この場合4C2(=6個)の組み合わせがlist(cc)に格納される


















    