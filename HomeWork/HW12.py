s = (input("Enter your message:"))
s = s.split()
d = {w : ("count: ", s.count(w)) for w in s}
print(d)