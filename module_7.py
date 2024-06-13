import random as r

#Get a specific character from a string
my_string = "pokemon"
print(my_string[0])

#Get a range of characters from a string
my_string = "xanderharris001@student.crowder.edu"
print(my_string[0:12])
print(my_string[13:-4])

#Determine a print length for each string
name = 'Jason'
email = 'Jfile@gmail.com'

print(f'{name:12}{email:30}')

#Do the same thing, in a loop
contact = [['Jason','Alice','Bob','Carol'],['123-456-7890','234-567-8901','345-678-9012','456-789-0123'],['jasonsony@gmail.com','alicemicro@gmail.com','bobtendo@gmail.com','carolsteam@gmail.com']]

for i in range(len(contact)):
    print(f'{contact[0][i]:12}{contact[1][i]:13}{contact[2][i]:30}')

#Print a string multiple times
my_string = 'ha'
blarp = r.randint(0,1000)
print(my_string * blarp)
print(blarp)
print(blarp * 2)

#replace a value in a strong
my_string = 'Please add extra mayo, I love mayo.'
print(my_string)
my_string = my_string.replace('mayo','ketchup',1)
print(my_string)

#Sort a list
contact[0].sort()
print(f'{contact[0]}')