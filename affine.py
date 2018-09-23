from extended_euclidean import extended_gcd

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def affine_encrypt(msg, a, b):
	result = ''
	for text in msg:
		index = letters.find(text)
		result += letters[(a * index + b) % 26]
	return result

def affine_decrypt(msg, a, b):
	result = ''
	(r, s, t) = extended_gcd(26, a)
	t = t % 26
	for text in msg:
		index = letters.find(text)
		result += letters[(t * (index - b)) % 26]
	return result

if __name__ == '__main__':
	resp = input('[E]ncrypt or [D]ecrypt? ').upper()
	if resp not in ('E', 'D'):
		print('Mode not recognized. Please run code again.')

	(a, b) = tuple(int(n.strip().strip('(').strip(').strip()')) for n in input('Type key (a,b): ').split(','))
	msg = input('Type message: ').upper()

	if resp == 'E':
		print(affine_encrypt(msg, a, b))
	else:
		print(affine_decrypt(msg, a, b))
	
