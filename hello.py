# print(1+2)
# print("Hello world")


# a, b, c = 5, 3.2, "Hello"
# print(a)
# print(b)
# print(c)

# x = y = z = "Hello"
# print(x)
# print(y)
# print(z)

# x = 3.14j
# print(x, x.imag , x.real)

# .imag = The imaginary literal
# .real = the real literal

# x = (1 == True)
# y = (1 == False)
# x =  (True)
# y =  (False)
# a = True + 4
# b = False + 10 + 1

# print("x is", x)
# print('y is', y)
# print("a:", a)
# print("b:", b)

# Docstrings In Python

# def double(num):
#     """Hello World"""
#     return 2*num


# print(double.__doc__)


# def double(num):
#     """Function to double the value"""
#     return 2*num


# print(double.__doc__)

# drink = "Available"
# food = None


# def menu(x):
#     if x == drink:
#         print(drink)
#     else:
#         print(food)


# menu(drink)
# menu(food)

# a = 5
# print(a, "is of type", type(a))

# a = 2.0
# print(a, "is of type", type(a))

# a = 1+2j
# print(a, "is of type", type(a))

# a = 1+2j
# print(a, "is complex number?", isinstance(1+2j, complex))

# a = [1, 2.2, "python"]
# print("value =", a[2])

# a = [1, 2, 12, 47, 54, 147, 254]
# print("value = ", a[2])
# print("value=", a[0:4])
# print("value=", a[2:5])
# print("value=", a[2:])

# a[5] = 99
# print("value=", a)


# t = (5, "program", (1+3j))
# print("value:", t[1])
# print("value:", t[1:3])

# a = '''helloWorld'''
# print(a)
# print("value =", a[7])

# a = {5, 2, 47, 7, 12}
# print("value=", a)
# print(type(a))

# c = {4: "cat", 'dog': 5}
# print(type(c))
# print("value=", c[4])
# print("value=", c["dog"])


# print(int(10.62545))
# print(float('2.54'))
# print(float('2'))
# print(str(25))

# print(set([1, 2, 5]))
# print(tuple({1, 2, 3}))
# print(list('hello'))

# print(dict([[1, 2], [3, 4]]))
# print(dict([(1, 2), (30, 4)]))


# Implicit Type conversion

# num_int = 123
# num_float = 1.25
# num_new = num_int + num_float
# print("value=", type(num_int))
# print("value=", type(num_float))
# print("value=", num_new)
# print("value=", type(num_new))


# Explicit Conversion


# num_int = 123
# num_string = "5000"

# print("value=", type(num_int))
# print("value=", type(num_string))
# num_string = int(num_string)
# print("value=", type(num_string))
# num_sum = num_int + num_string
# print("total value=", num_sum)
# print("total value=", type(num_sum))

# print(1, 23, 42, 14)
# print(1, 23, 42, 14, sep="*")
# print(1, 23, 42, 14, sep="#", end="&")

# x = 5
# y = 10
# print('The value of x is {} and y is {}'.format(x, y))

# a = 14.521452
# print('The value of a is %5.1f' % a)
# print('The value of a is %5.6f' % a)

# from math import sqrt
# import math
# import sys


# print(int('2'))
# print(eval('2+5'))

# print(math.pi)

# print(sys.path)

# num = input('Enter a number:')
# print(num)
# print(20**5)

# def printHello():
#     print("Hello")


# a = printHello
# a()

# def outer_function():
#     global a
#     a = 20

#     def inner_function():
#         global a
#         a = 30
#         print('a=', a)

#         inner_function()
#         print('a=', a)

#         a = 10
#         outer_function()
#         print('a=', a)

# num = 1
# if num >= 3:

#     print("Positive or zero")
# elif num == 0:
#     print("Zero")
# else:
#     print("Negative number")

# import numbers


# numbers = [5, 2, 24, 11, 2, 7, 5]
# sum = 0
# for val in numbers:
#     sum = sum + val
#     print("The sum is ", sum)

# print(range(10))
# print(list(range(10)))
# print(list(range(3, 8)))
# print(list(range(3, 18, 5)))

# genre = ['pop', 'rock', 'jazz']
# for i in range(len(genre)):
#     print("I like", genre[i])

# from string import digits
# from turtle import left


# digits = [0, 1, 5]
# for i in digits:
#     print(i)
# else:
#     print("No items left")

# student_name = 'Soyuj'
# marks = {'James': 90, 'Soyuj': 55, 'Arthur': 77}
# for student in marks:
#     if student == student_name:
#         print(marks[student])
#         break
# else:
#     print('No entry with that name found')


# n = 10
# sum = 0
# i = 1
# while i <= n:
#     sum = sum + i
#     i = i+1
#     print("The sum is ", sum)

# counter = 0
# while counter < 3:
#     print("inside loop")
#     counter = counter+1
# else:
#     print("inside else")

# for val in "string":
#     if val == "i":
#         # break
#         continue
#     print(val)

# from msilib import sequence


# sequence = {'p', 'a', 's', 's'}
# for val in sequence:
#     pass


# def function(args):
#     pass

# def greet(name):

#     print("Hello " + name + " Keep Going")


# greet("Paul")
# print(greet.__doc__)

# def absoulute_value(num):
#     if num >= 0:
#         return num
#     else:
#         return -num


# print(absoulute_value(2))
# print(absoulute_value(-4))


# def car(num):
#     if num >= 0:
#         return num
#     else:
#         return -num


# print(car(2))
# print(car(-4))

# def greet(name, msg):
#     print("Hello", name + msg)


# greet("Monica ", " Good Morning !")

# def greet(name, msg):
#     print("Hello", name + ',' + msg)


# greet("Kate","Hey Bro")
# greet("Bruce", "How do you do?")


# def greet(*names):
#     for name in names:
#         print("Hello", name)


# greet("Monica", "Luke", "Steve", "John")


# def factorial(x):
#     if x == 1:
#         return 1
#     else:
#         return (x*factorial(x-1))


# num = 3


# print("The factorial of:", num, "is", factorial(num))

# my_list = [1, 5, 4, 6, 8, 11, 3, 12]
# new_list = list(filter(lambda x: (x % 3 == 0), my_list))
# print(new_list)

# my_list = [1, 5, 4, 6, 8, 11, 3, 12]
# new_list = list(map(lambda x: x*3, my_list))
# print(new_list)

x = 15


def foo():
    x = 10
    print("local x value:", x)


foo()
print("global x value:", x)

# Keep Going
