def gcd(a,b):
	if b == 0:
		return a

	return gcd(b, a%b)

if __name__ == '__main__':
	a = input('Enter first number: ')
	b = input('Enter second number: ')
	if a > b:
		c = gcd(int(a),int(b))
	else:
		c = gcd(int(b),int(a))
	print(f'The GCD of {a} and {b} is {c}')
