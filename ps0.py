# can run in https://repl.it/languages/python3


#  the inverse of exponents. Import Numpy for log method

# numpy installation https://www.edureka.co/blog/install-numpy/
import numpy

# input()  enter string
# int() input to an integer
x = int(input('Enter number x: '))
y = int(input('Enter number y: '))


# x ** y represents x to the power of y
# print() print to console
# .format looks for {} in order to place its arguments
print('x**y = {}'.format(x**y))
print('log(x) = {}'.format(numpy.log2(x)))
