# #try/except block to keep program from crashing
# try:
#     my_num = int(input('Please enter a number: '))
#     print(f'{100/my_num}')
# except:
#     print('There was an issue with your input. Please try again')

# #try/except combined with a loop
# while True:
#     try:
#         my_num = int(input('Please enter a number: '))
#         print(f'{100/my_num}')
#         break
#     except:
#         print('There was an issue with your input. Please try again')

# #try/except with specific errors
# while True:
#     try:
#         my_num = int(input('Please enter a number: '))
#         print(f'{100/my_num}')
#         break
#     except ValueError:
#         print('You must enter a number to continue')
#     except ZeroDivisionError:
#         print('You cannot divide by 0')
#     except:
#         print('There was an issue with your input. Please try again')

# # Create a custom exception
class NumberTooLargeError(Exception):
    def __init__(self,value):
        self.value = value

while True:
    try:
        my_num = int(input('Please enter a number: '))
        if my_num > 100:
            raise NumberTooLargeError('Number must be less than 100')
        print(f'{(100/my_num):.0f}')
        break
    except ValueError:
        print('You must enter a number to continue')
    except ZeroDivisionError:
        print('You cannot divide by 0')
    except NumberTooLargeError as ex:
        print(ex)
    except:
        print('There was an issue with your input. Please try again')