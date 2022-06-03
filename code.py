x = int(input("enter the number which factors to find"))
print("the number enterd is ",x,"as entered" )
for i in range(1, x + 1):
    if x % i == 0:
        if  i % 2 ==0:
            print(i,"even")
        else:
            print(i,"odd")
    