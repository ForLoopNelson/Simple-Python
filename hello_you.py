# Ask User for name
name = input('What is your name?: ')

#Ask User for age
age = input("What is your age?: ")

#Ask User for city
city = input('Where do you live?: ')

#Ask User what they enjoy
hobby =input("What do you enjoy?: ")

#Create output text
string = ' Your name is {} and you are {} years old. You live in {} and your hobbies include {}.'
output = string.format(name,age,city,hobby)

#Print output to screen
print(output)
