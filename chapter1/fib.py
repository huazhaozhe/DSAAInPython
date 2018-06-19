def fib1(n, a=1, b=1):
    if n == 1:
        return a
    elif n == 2:
        return b
    elif n >= 3:
        for i in range(n-2):
            b, a = a+b, b
        return b
    else:
        return 0

def fib2(n, a=1, b=1):
    if n == 1:
        return a
    elif n == 2:
        return b
    elif n >= 3:
        return fib2(n-1, a, b) + fib2(n-2, a, b)
    else:
        return 0

print(fib1(1), fib1(2), fib1(3), fib1(5), fib1(10))
print(fib2(1, 2, 2), fib2(2, 2, 2), fib2(3, 2, 2), fib2(5, 2, 2), fib2(10, 2, 2))

for i in range(20):
    print(fib2(i, 1, 2))