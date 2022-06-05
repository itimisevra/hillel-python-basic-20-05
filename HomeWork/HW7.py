string = input("Enter your message: ")
print(string and string[-1] == ".")
print(len([i for i in string.split(". ")]))git