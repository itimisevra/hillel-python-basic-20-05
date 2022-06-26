fib1 = 1
fib2 = 1

n = input("Enter (n): ")
n = int(n)

i = 0
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1

print("F(n): ", fib2)


def fibonacci(n):
    n = int(input("Enter (n): "))
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(n))



