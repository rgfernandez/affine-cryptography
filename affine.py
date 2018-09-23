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
	for text in msg:
		index = letters.find(text)
		(r, s, t) = extended_gcd(26, a)
		result += letters[(t % 26) * (index - b) % 26]
	return result

if __name__ == '__main__':
	resp = input('[E]ncrypt or [D]ecrypt? ').upper()
	if resp not in ('E', 'D'):
		print('Not recognized')

	msg = input('Type message: ').upper()
	a = int(input('Type a: '))
	b = int(input('Type b: '))

	if resp == 'E':
		print(affine_encrypt(msg, a, b))
	else:
		print(affine_decrypt(msg, a, b))
	
