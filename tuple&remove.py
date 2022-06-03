a =input("enter atleast 3 digit tuple\t") 
print(a)
c = list(a)
del c[2]
b = tuple(c)
print("tuple with third value removed is",b)