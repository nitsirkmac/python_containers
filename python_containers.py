## Exercise 1 ##


students = [ "Molly", "Mickey", "Michael", "Matthew" ]
print( students[1])
print( students[-1])


## Exercise 2 ##

foods = ("Bread", "Bacon", "Lettuce", "Tomato")
for food in foods:
    print(f"{food} is a good food")

## Exercise 3 ##
"""
for food in foods[2:]:
    print(food)

    # I'm not confident that I did this correctly, how would you recommend this is done?
"""

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
for idx, student in enumerate(students):
    cohort.append(dict(iter([("student", student), ("fav_food", foods[idx])])))

print(cohort)



## Exercise 7 ##
"""
awesome_students = [f'{student} is awesome!' for student in students]

print(awesome_students)
"""

## Exercise 8 ##
"""
aFoods = [food for food in foods if 'a' in food]
print(aFoods)
"""