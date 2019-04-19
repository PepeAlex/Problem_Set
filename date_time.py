# Alexander Pepe
# Problem Set 2019
# Question 8

import datetime

i = datetime.datetime.today()

d = i.strftime("%d")
a = i.strftime('%A, %B')
b = i.strftime('%Y at %I:%M%p')

if d == 1 or d == 21 or d == 31:
    print(a, d,'st', b)
if d == 2:
    print(a, d,'nd', b)
if d == 3:
    print(a, d,'rd', b)   
else:
    print(a, d,'th', b)