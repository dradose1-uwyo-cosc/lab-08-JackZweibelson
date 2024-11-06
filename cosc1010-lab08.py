# Jack Zweibelson
# UWYO COSC 1010
# Submission Date: 11/6/2024
# Lab 8
# Lab Section:15
# Sources, people worked with, help given to:
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 



def check(vari):
    if vari == " ":
        return None
    if "." in vari:
        return float(vari)
    return int(vari)

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list


while True:
    m = ""
    b = ""
    lx = ""
    ux = ""
    c = 0
    inp = input("Please input integers for each variable with commas inbetween m,b,lx,ux: ")
    if inp.lower().strip() == "exit":
        break
    for i in inp:
        if i.isdigit() or i == "." or i == "-":
            if c == 0:
                m += i
            if c == 1:
                b += i
            if c == 2:
                lx += i
            if c == 3:
                ux += i
        elif i == ",":
            c += 1
    else:
        if lx == ux or lx > ux:
            print("incorrect range")
            continue

        m = check(m)
        b = check(b)
        if "." in lx:
            print("Range cannot be float")
            continue 
        lx = check(lx)
        if not ux.isdigit():
            print("Range cannot be float")
            continue 
        ux = check(ux)        


        for i in range(lx, ux + 1):
            y = i*m +b
            print(f'x:{i} : y:{y}')


print("*" * 75)

# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

while True:
    a = ""
    b = ""
    c = ""
    x = 0
    inp = input("Please input integers for each variable with commas inbetween a,b,c: ")
    if inp.lower().strip() == "exit":
        break    
    for i in inp:
        if i.isdigit() or i == "." or i == "-":
            if x == 0:
                a += i
            if x == 1:
                b += i
            if x == 2:
                c += i
        elif i == ",":
            x += 1
    else:
        a = check(a)
        b = check(b)
        c = check(c)

        f = (b**2)-4*a*c
        if f > 0:
            print((-b+(f**.5))/(2*a))
            print((-b-(f**.5))/(2*a))
        else:
            print("0") 



