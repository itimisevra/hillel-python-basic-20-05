import random

n = int(input("Enter number: "))
mylist = [random.randint(0, n) for i in range(n)]
print(mylist)


res = []
x = int(input("Enter the second number: "))
for i in range(0, len(mylist)):
    for a in range(i + 1, len(mylist)):
        if mylist[i] + mylist[a] == x:
            res = [i, a]
            print(res)
            break
        else:
            continue







