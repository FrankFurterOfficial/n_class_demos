#use type() to see the data type of an object
my_string = 'Upward Bound'
my_int = 87
my_float = 8.7
my_bool = True
print(type(my_string))
print(type(my_int))
print(type(my_float))
print(type(my_bool))

#Basic Arithmatic operators
num_1 = 72
num_2 = 19

print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)
print(num_1 / num_2)
print(' ')
#num_1 to the power of num_2
print(num_1 ** num_2)
#floor of num_1 / num_2 (division but rounded)
print(num_1 // num_2)
#remainder, if used with floor you can get both sides of the decimal when dividing
print(num_1 % num_2)

#Import math module and access functions 
import math

print(math.sqrt(200))

#Import random madoule and access functoins to get a random float and a random int
import random as r
r.seed(3437)
my_random = r.random() #saving a random float to a variable
print(my_random)
print(r.randint(0, 2)) #Printing a random int directly to terminal