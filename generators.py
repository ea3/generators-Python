def creates_cubes(n):

	for x in range(n):
		yield (x**3)

for x in creates_cubes(10):
	print(x)



### Fibbonnacci sequence 

def gen_fibon(n):

	a = 1
	b = 1

	for i in range(n):
		yield a
		a, b = b, a + b

for number in gen_fibon(10):
	print(number)






