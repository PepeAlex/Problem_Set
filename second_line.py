# Alexander Pepe
# Problem Set 2019
# Question 9

from sys import argv

script, filename = argv

txt = open(filename)

line = txt.readlines()

x_line = len(line)
y = line[::-1]

if x_line % 2 == 0:
    while x_line > 0:
        x_line = x_line - 2
        print(y[x_line], end=' ')

else:
    while x_line != 1:
        x_line = x_line - 2
        print(y[x_line], end=' ')
    
# I ceated a conditinal to print question 9 but my result printed 
# back to the front and I read in https://www.pythoncentral.io/quick-tip-reversing-strings-in-python/ 
# about '::-1' and I thought very interesting and I used to put my text in the 
# right position. 
