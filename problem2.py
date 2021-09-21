#! python3

# Have the user enter a number 
# Determine if the number is an integer
# 1 mark

# Inputs:
# a number

# Outputs:
# "the number is an integer"
# "the number is not an integer"


num = input("Number?")
num2 = num
num = int(num)
if num == float(num2):
    print("the number is an integer")
else :
    print("the number is not an integer")