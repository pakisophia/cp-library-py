#https://atcoder.jp/contests/abc177/tasks/abc177_e ←使用例
#A=max(A)が小さい時、aの全ての要素を高速(O（AloglogA+NlogA))に素因数分解するときに使用



#入力
#n=int(input())
#a=list(map(int,input().split()))

ma=max(a)

d=[i for i in range(ma+1)]
#d[j]=i...jを割り切る最小の素数j

def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
            if d[j]==j:
                d[j]=i
    return [i for i in range(n + 1) if is_prime[i]]

#実際に動かせば、割るべき数が、Dに格納されているので、それを手で割っていく　試し割りする必要がない