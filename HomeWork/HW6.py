string = input("Enter your message: ")
l = len(string)
print(l)
print(string.replace("n","N"))

print(string[string.find(" ") + 1:string.rfind(" ")].replace("n","N"))


