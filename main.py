# Joshua Phillips
# Simple Math
# 9/25/2024

# md1
# I
num1 = 10
num2 = 2
# P
sum = num1 + num2
difference = num1 - num2
product = num1 * num2 
quotient = num1 / num2
# O
print(f'The sum, difference, product, and quotient are: {sum}, {difference}, {product}, {quotient} respectively.')

# md2
# I
length = float(input('Please enter the length of the rectagular room(in square feet): '))
width = float(input('Please enter the width of the rectagular room(in square feet): '))

# P
area = length * width
# O
print(f'The area (in square ft) of this rectangular room is {area}.')

# md3
# part one
# I
name = "Joshua"
age = 18
color = 'Blue'


# P

# O
message = "My name is {0} and I am {1} years old. {2} is my favorite color.".format(name, age, color)
print(message)

# part two

tax = 0.06
price1 = 30
price2 = 28
price3 = 92
allprice = price1 + price2 + price3
taxtotal = allprice * tax
message2 = 'Total tax on three items is ${0}'.format(taxtotal)
print(message2)
# part three

pal = 'Lucas'
school = 'Home'
message3 = 'His name is {0} and he attends {1}'.format(pal, school)
print(message3)