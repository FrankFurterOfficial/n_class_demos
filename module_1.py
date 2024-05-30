#Output a string to the terminal
print('Where is Miguel?')

#Get a string from the user
miguel_location = input()

#Output the value from a variable to the terminal
print('Miguel is')
print(miguel_location)

#Prompt the user for a value and save that value to a variable
num_chocolate = int(input('How much chocolate did you eat: '))

chocolate_price = float(input('how much did each chocolate cost: '))

#Store product of 2 variables in a new variable
total = num_chocolate * chocolate_price

#Output variables to terminal using concatonation
print('I bought ' + str(num_chocolate) + ' chocolates for $' + str(round(total, 2)) + '.')

#Output variables to terminal using formatted strings
print(f'I bought {num_chocolate} chocolates for ${round(total, 2)}.')