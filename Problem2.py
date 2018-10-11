def fib(n):
    if n <= 1:
        return n
    else:
        return (fib(n-1) + fib(n-2))


sum = 0

for i in range (1,34):
    fib_val = fib(i)
    if fib_val % 2 == 0:
        sum += fib_val

print(sum)