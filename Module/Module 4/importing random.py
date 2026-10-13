import random

##print(random.randint(1, 10))

#print(random.random())

#print(random.seed(a= None, version=2))

answer = random.randint(1, 3)

if answer == 1:
    print("Yes")
elif answer == 2:
    print("No")
else:
    print("Maybe")