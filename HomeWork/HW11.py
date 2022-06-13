names = [name for name in input("Enter names: ").split()]
print(names)
for count, value in enumerate(names):
    print(count, value)

unique_names = [i for i in names if names.count(i) == 1]
print(unique_names)





