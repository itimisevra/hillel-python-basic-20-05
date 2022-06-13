names = [name for name in input("Enter names: ").split()]
print(names)

def get_unique_names(names):
    list_of_unique_names = []
    unique_names = set(names)

    for name in unique_names:
        list_of_unique_names.append(name)

    return list_of_unique_names

print(get_unique_names(names))





