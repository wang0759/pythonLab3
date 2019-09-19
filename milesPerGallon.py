'''
Write a program that will compute MPG for a car.
Prompt the user to enter the number of miles driven
and the number of gallons used. Print a nice message with the answer.
'''

miles = float(input("please enter miles driven:"))
gallons = float(input("please enter gallons used:"))
mpg = miles/gallons
print("MPG is:", mpg)
