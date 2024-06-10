#Simple While Loop Example
while True:
    choice = input('Please select a option:\n1-Place Order\n2- View order\n3- Exit System\n')
    if choice == '1':
        input('Place new order\n')
    elif choice == '2':
        input('View order\n')
    elif choice == '3':
        break
    else:
        input('try again\n')
print('we outta here')

#Simple for loop example
for i in range(5):
    print(i + 1)

#Using a for loop with a collection
answer_list = ['python','C#','Javascript','Scratch']
correct_answer = 'Scratch'
print('Which is the best programming language?')

for i in answer_list:
    print(i)

user_answer = input()

for i in answer_list:
    if i == correct_answer:
        print('⭐' + i)
    else:
        print('❌' + i)


#Nesting repetition loops
username = 'Jesus49'
password = 'Password123'

for i in range(3)