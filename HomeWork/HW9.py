import random

n = int(input("Enter number:"))
mylist = [random.randint(0,n) for i in range(n)]
print(mylist)

for count, value in enumerate(mylist):
    print(count, value)

n = int(input("Enter second number: "))
index = mylist.index(int(n))

print("index:", index)

if n not in mylist:
    print("Not found")
elif mylist[0] == n:
    print("number on the right:", mylist[index + 1])
elif mylist[-1] == n:
    print("number on the right:", mylist[index - 1])
else:
    print("numbers on the sides:", mylist[index - 1], "and", mylist[index + 1])









