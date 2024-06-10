# #Basic Conditional Statement
# my_password = 'password123'
# input_password = input('Please enter password: ')
# if input_password == my_password:
#     print('Access Granted')
# else:
#     print('get outta HERE!!!')

#If-else chain Example
# my_score = int(input('Please enter your grade: '))
# letter = 'huh'
# if my_score > 89:
#     letter='A'
# elif my_score > 79 and my_score < 90:
#     letter='B'
# elif my_score > 69 and my_score < 80:
#     letter='C'
# elif my_score > 59 and my_score < 70:
#     letter='D'
# elif my_score > 0 and my_score < 60:
#     letter='F'
# print(letter)

#Create small calculator app
# input_operation = int(input(f'Welcome to the CALCURATOR!. Please choose an operation\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Dvision\n'))

# input_num1 = float(input('Please enter your first number: '))
# input_num2 = float(input('Please enter your second number: '))
# print(input_operation)
# print(input_operation == 1)
# if input_operation == '1':
#     operation = '+'
#     answer = input_num1 + input_num2
# elif input_operation == '2':
#     operation = '-'
#     answer = input_num1 - input_num2
# elif input_operation == '3':
#     operation = '*'
#     answer = input_num1 * input_num2
# elif input_operation == '4':
#     operation = '/'
#     if input_num2 == 0:
#         input_num2 = float(input('Cannot divide by 0, Please choose a different number: '))
#     answer = input_num1 / input_num2
# print(f'{input_num1} {operation} {input_num2} = {answer:.2f}')

#Using membership operators
my_list = ['Coke', 'Root Beer', 'Sprite', 'Mountain Dew', 'water', 'Lemonade', 'Milk','Dr.Pepper']

if 'Sprite' in my_list:
    print('Sprite (the best one) is in the list')
else:
    print('Sprite (the best one) is not in the list')

#Logical Operators
##And- both are true
##or - one is true
##not- Negates a condition

my_username = 'GallantArc302'
my_password = 'I love miners'

input_username = input('Please enter username: ')
input_password = input('Please enter password: ')

if input_username == my_username and input_password == my_password:
    print('Access Granted')
elif input_username != my_username or input_password != my_password:
    print('Username and/or Password.... WRONG!')