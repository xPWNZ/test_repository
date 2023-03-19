
x = int(input())

def fib(n):
    if n <= 1:
        return n
    else:
        return((n-1) + (n-2))


print(fib(x))