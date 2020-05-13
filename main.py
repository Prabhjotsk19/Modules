# variables
name = "prabhjot singh"

print(name)

num = 23
print(num)

print()

# loops 
# for
for i in range(12):
    print(i)

print()

# while
number  = 4
while number>0:
    print(number)
    number -= 1

print()

print('Number = ', number)

# if else
if number > 0 :
    print('hey!')  
elif number < 0:
    print('No')
else:
    print('yes')

print()


# functions 
def sum(num1, num2):
    return num1+num2

print(sum(1, 2))

# fabonacci series 
# recursive problem
# 1,1,2,3, 4
# fn = fn-1 + fn-2
# if n=0 and n=1 : fn = 0
# else fn = fn-1 + fn-2
print('Fabonacci series')
def fabonacci(numb):
    if (numb == 0 or numb == 1):
        return 1
    else:
        return (fabonacci(numb-1) + fabonacci(numb-2))

print(fabonacci(3))
print(fabonacci(5))
print()

# factorial problem
'''
n! = n*(n-1)!
if n=0 : n! = 1
else : n! = n*(n-1)!
'''
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
print('factorial Problem')
print(fact(5))
print(fact(4))
print()

# range func
print(range(12))
print(range(1,6))
print()

# Working with modules 
import modules
modules.func()

print(modules.dict['prabh'])
print(modules.dict['abhijeet'])

import modules as mo
mo.func()

from modules import dict
print(dict['prabh'])

print(dir(modules))
print()

# inbuilt modules
import platform
print(platform.system())
print(dir(platform))

# dir() without argument give names in current scope 
print(dir())

