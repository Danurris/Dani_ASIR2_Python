def fibonacci(n):
	if n <= 0:
		return []
	if n == 1:
		return [0]

	fib_series = [0, 1]
	for i in range(2, n):
		next_num = fib_series[-1] + fib_series[-2]
		fib_series.append(next_num)

	return fib_series

print(fibonacci(2584))
