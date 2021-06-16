# Number
my_variable = 5
print(my_variable)

# String
language = 'Python'
print(language)

# Booleans
python_is_cool = True
javascript_is_better = False

# List
foods = ['burger', 'cheese', 'buns']
print(foods[1])
print(foods[-2])

print('--------')

for food in foods:
    print(food)

print(len(foods))

cars = ['Mercedes', 'Audi', 'Jaguar']
for i, car in enumerate(cars):
    print('{}. {}'.format(i, car))

teams = ['Clippers', 'Bucks', 'Nets', 'Jazz']
for i in range(len(teams)):
    each_team = teams[i]
    print('{}. {}'.format(i, each_team))

# Dictionaries
student = {
    "name": 'John',
    "class": 'Physics',
    "year": 2021
}

# John
print(student["name"])
# Physics
print(student.get('class'))

print('------')

# Iterate through a dictionary
for key in student:
    print('{}, {}'.format(key, student[key]))

print('----')

# Conditionals
age = 22

if age < 21:
    print('Not old enough')
elif age == 21:
    print('You made it')
else:
    print("You're old enough")

print('----')

if student['name']:
    print('{}'.format(student['name']))

if 'Rome' in student.get('name'):
    print('True')
else:
    print(False)

if 'Porsche' in cars:
    print(True)
else:
    print(False)
def intro_student(name, course = 'Calculus', year = 2022):
    print('My name is {}. I am in {} class. I graduate in {}'.format(name, course, year))

# intro_student(student['name'], student['class'], student['year'])

intro_student('Rome', 'Physics')