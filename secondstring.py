# Alexander Pepe
# Problem Set 2019
# Question 6

x = input("Please, enter a sentence: ")

a = x.split()
x = a[::-1]
b = len(x)

if b % 2 == 0:
    while b > 0:
        b = b - 2
        print(x[b], end=' ')
else:
    while b != 1:
        b = b - 2
        print(x[b], end=' ')

# I ceated a conditinal to print question 6 but my result printed 
# back to the front and I read in https://www.pythoncentral.io/quick-tip-reversing-strings-in-python/ 
# about '::-1' and I thought very interesting and I used to put my frase in the 
# right position. 
