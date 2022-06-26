n = 2
p = int(input('num? '))
r = 1
while (p > 0):
    r *= n
    p -= 1

print('result:', r)




def degree(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / degree(x, -n)
    if n % 2 == 0:
        return degree(x, n // 2) * degree(x, n // 2)
    else:
        return degree(x, n - 1) * x

x = 2
n = int(input("2 in degree: "))
print(degree(x, n))




