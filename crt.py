#中国剰余定理
#https://mathlandscape.com/chinese-remainder/#toc3


import typing
 
def inv_gcd(a: int, b: int) -> typing.Tuple[int, int]:
	a %= b
	if a == 0:
		return (b, 0)
	s = b
	t = a
	m0 = 0
	m1 = 1
	while t:
		u = s // t
		s -= t * u
		m0 -= m1 * u
		s, t = t, s
		m0, m1 = m1, m0
	if m0 < 0:
		m0 += b // s
	return (s, m0)
 
def inv_mod(x: int, m: int) -> int:
	z = inv_gcd(x, m)
	return z[1]

#rがmodされたものの結果、mがmodのリストを引数として入力する
#returnとしてtuple型で返す。最初の要素にx≡r(mod m)となるxが格納されており、二つ目の要素にlcm(m1,m2,・・・mn)が格納されている（多分）
def crt(r: typing.List[int], m: typing.List[int]) -> typing.Tuple[int, int]:
	r0 = 0
	m0 = 1
	for r1, m1 in zip(r, m):
		r1 %= m1
		if m0 < m1:
			r0, r1 = r1, r0
			m0, m1 = m1, m0
		if m0 % m1 == 0:
			if r0 % m1 != r1:
				return (0, 0)
			continue
		g, im = inv_gcd(m0, m1)
		u1 = m1 // g
		if (r1 - r0) % g:
			return (0, 0)
		x = (r1 - r0) // g % u1 * im % u1
		r0 += x * m0
		m0 *= u1
		if r0 < 0:r0 += m0
	return (r0, m0)


    


















