sum = 0
count = 0
max = 0
min = 155445451545155451

while True:
    s = input("enter: ")
    if not s:
        print(sum, count, max, min, average)
        break
    number = int(s)
    sum = sum + number
    count = count + 1
    if number > max:
        max = number
    if number < min:
        min = number
    if count > 0:
        average = sum//count