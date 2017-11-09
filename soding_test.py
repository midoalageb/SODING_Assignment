def fib(n, cache = {0:0, 1:1}):
	if n in cache:
		return cache[n]
	cache[n] = fib(n-1) + fib(n-2)
	return cache[n]

def get_sum_even_values(limit):
	sum_values = 0
	i = 1
	while True:
		c = fib(i)
		if c > limit: break
		if c % 2 == 0:
			sum_values += c
		i += 1
	return sum_values
	
try:
	value = int(input("Please enter the limiting value for calculating Fibonacci sequence: "))
	if value < 0:
		print("Value must be an number > 0")
	else:
		print("The sum of Fibonacci sequence even values less than {} is ".format(value)+str(get_sum_even_values(value)))
except:
	print("Value must be an number > 0")
	
