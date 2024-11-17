# Your code goes here:
def render_person(name, birthdate, eyecolor, age, gender):
    return name + " is a " + str(age) + " years old " + gender + " born in " + birthdate + " with " + eyecolor + " eyes"


# Do not edit below this line
print(render_person('Bob', '05/22/1983', 'green', 23, 'male'))