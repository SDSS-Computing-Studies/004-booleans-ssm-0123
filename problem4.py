#! python3
# Have the user enter in 3 numerical values, representing the side lengths of a triangle. 
# Determine if the values are close enough to make a right triangle. 
# Note: You will need to decide which length is the possibly hypotenuse as the numbers
# are being entered in a random order.
# It is close enough if the expected length of the hypotenuse and the actual length 
# differ by no more than 2% 
# (2 marks)

# Inputs:
# - 3 numbers, in any order

# Outputs:
# - "that is a right triangle"
# - "that is an acute triangle"
# - "that is an obtuse triangle"
"""
Example:
Enter one side: 5
Enter a second side: 13
Enter third side: 12
that is a right triangle

Enter one side: 13.01
Enter a second side: 5
Enter third side: 12
that is a right triangle

Enter one side: 5
Enter a second side: 15
Enter third side: 12
that is an obtuse triangle


"""

one = input("First Side")
sec = input("Second Side")
thi = input("Third Side")

one = float(one)
sec = float(sec)
thi = float(thi)

if one >= thi :
    if one >= sec :
        big=one
        otr1 = sec
        otr2 = thi

if sec >= thi :
    if sec >= one :
        big=sec
        otr1 = one
        otr2 = thi

if thi >= one :
    if thi >= sec :
        big=thi
        otr1 = sec
        otr2 = one

sqr = otr1**2 + otr2**2

if 0.98*(big**2) <= sqr <= 1.02*(big**2) : 
    print("that is a right triangle")

if big**2<sqr:
    print("that is an acute triangle")

if big**2>sqr:
    print("that is an obtuse triangle")