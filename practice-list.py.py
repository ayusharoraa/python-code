mu_list= []
my_list =[1,2,3]
num =int(input("enter range"))
for i in range(0,num):
    element = int(input())
    mu_list.append(element)
print((mu_list))
mu_list.remove(3)
print(mu_list)