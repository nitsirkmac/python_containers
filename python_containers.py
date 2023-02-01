## Exercise 1 ##


students = [ "Molly", "Mickey", "Michael", "Matthew" ]
print( students[1])
print( students[-1])


## Exercise 2 ##

"""
foods = ("Bread", "Bacon", "Lettuce", "Tomato")
for food in foods:
    print(f"{food} is a good food")
"""

## Exercise 3 ##




## Exercise 4 ##
"""
home_town = {
    "city": "Hatteras",
    "state": "North Carolina",
    "population": 373
}

print( f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']}")
"""

## Exercise 5 ##
"""
for key, val in home_town.items():
    print(f'"{key} = {val}"')
"""

## Exercise 6 ##

cohort = []
cohort.extend(('student', students[0]))
print(cohort)
# dict(item([("student", "Molly"), ("fav_food": "Bread")]))


## Exercise 7 ##
"""
awesome_students = []

for student in students:
        awesome_students.append(f'{student} is awesome!')

print(awesome_students)
"""