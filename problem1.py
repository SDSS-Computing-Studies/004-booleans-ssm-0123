#! python3

# Have the user enter a number 
# Determine if the number is an even number. 
# Hint: Use the modulus, which determines the remainder when two numbers are divided
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is even"
# "the number is odd"

import math

num = input("Number?")
num = int(num)

if math.remainder(num,2) == 0:
    print("This number is even")
else :
    print("This number is odd")

