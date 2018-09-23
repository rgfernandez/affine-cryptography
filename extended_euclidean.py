def extended_gcd(a, b):
	c = max(a, b)
	d = min(a, b)

	s = 0; old_s = 1
	t = 1; old_t = 0

	while True:
		q = int(c / d)
		r = c % d

		print(f'{r} = {c} - {q}({d})')

		(old_s, s) = (s, old_s - q*s)
		(old_t, t) = (t, old_t - q*t)

		print(f'  {r} = {s}({a}) + {t}({b})')

		if (r == 0):
			return (d, old_s, old_t)

		c = d
		d = r

if __name__ == '__main__':
	a = input('Enter first number: ')
	b = input('Enter second number: ')

	(c, d, e) = extended_gcd(int(a), int(b))
	print(f'The GCD of {a} and {b} is {c}. The solution to {a}*x+{b}*y={c} is ({d},{e})')
