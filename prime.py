# Alexander Pepe
# Problem Set 2019
# Question 5

x = int(input("Please, enter a positive number: "))

for i in range(2, x):
    if i != x:
        i = x % i
        if i == 0:
            print("That is not a prime")
            break
        else:
            print("That is a prime")
            break