#The MODULO Operator:
#% (modulo operator) divides one number by another number and returns the remainder:

print(4 % 3) #Returns one because the remainder is 1.

print(11 % 6) #6 goes only once in 11, 5 left.

print(6 % 6) #6 is divisible by 6 so the remainder is 0.
#This is useful if you want to see ex) all 3-multipliers in a list.range() because if 3 % x = 0 it's a multiplier.

for i in range(1, 100):
    if i % 3 == 0:
        print(i)
#For loop above prints all 3-multipliers from 1-99.