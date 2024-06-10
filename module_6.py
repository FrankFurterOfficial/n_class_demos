# #Simple fuction to display the sum of two numbers

# def Add(num1,num2):
#     print(f'{num1} + {num2} = {num1 + num2}')

# my_number1 = int(input('Please enter a number: '))
# my_number2 = int(input('Please enter a number: '))
# Add(my_number1,my_number2)

# #simple function to return the sum of two numbers

# def add(num1,num2):
#     return num1 + num2
# my_number1 = int(input('Please enter a number: '))
# my_number2 = int(input('Please enter a number: '))
# total = add(my_number1,my_number2)
# print(total)


#redo quiz assi"gn"ment using loops and function
#Function to display question and get user answer
def get_answer(question,answers):
    print(question)
    for i in range(len(answers)):
        print(f'{i + 1} - {answers[i]}')
    user_choice = int(input())
    return user_choice - 1

#function to get test sore
def get_score(user_answers,correct_answers):
    correct_total = 0
    for i in range(len(user_answers)):
        if user_answers[i] == correct_answers[i]:
            correct_total += 1
    return correct_total / len(user_answers) * 100

#Store questions in a list
questions = ['2+3','5-2','3+7','3x3','4*2']
#store correct answers in a list
correct_answers = [0,2,1,0,2]
#store answers in a list of lists
answers = [['5', '6', '7','8'], ['2', '23', '3','42'], ['9', '10', '23','5'], ['9', '3', '6','12'], ['7','9','8','6']]
#Create list to store user answers
user_answers = []

#loop through each question to get use response
#Add user response to user_answers list
for i in range(len(questions)):
    user_answers.append(get_answer(questions[i],answers[i]))

#Get and display score for the user
print(f'Your score was a {get_score(user_answers,correct_answers):.2f}%.')