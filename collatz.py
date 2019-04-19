# Alexander Pepe
# Problem Set 2019
# Question 4

i = int(input("Please, enter a positive integer: "))

a = i // 2

print(i, end=' ') 

for a in range(1, i):
    a = i // 2
    print(a, end=' ')
    break

if a > 0:
        a = (a * 3) + 1
        print(a, end=' ')

while a >= 1 and a != 1:
    a = a // 2
    print(a, end=' ')


# I used "for" to define the integer of "i". After that I created a
# condition that the exercise asked and I used "while" to have diviser 
# until finish in "1".