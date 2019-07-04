import random
import functools
import math
import operator
import itertools
"""This is the functional conversion of imperative.py"""
def randomiser(attr):
    result = attr[random.randint(0, len(attr) - 1)]
    return result

def count(members): return len(members)

def create_members():
    names = ['jack', 'joe', 'jason', 'james', 'john', 'jakob', 'june', 'jeb', 'jarrod', 'jim']
    coding_languages = ['scala', 'python', 'java', 'java script', 'go', 'haskell']
    beverages = ['beer', 'bubbly', 'schnaps', 'jaegerbombs', 'milk']
    members = list(map(lambda x : {'name': x,'likes_tacos': x.startswith('ja') , 'coding_language': randomiser(coding_languages),
                    'favourite_beverage': randomiser(beverages), 'age':random.randint(18, 65)}, names))
    return members

def addition(x , y): return x + y

if __name__ == '__main__':
    members = create_members()

    list(map(print, members))

    #Taco lovers
    list(map(lambda x: print(x['name'], 'loves tacos'),list(filter(lambda y: y['likes_tacos'] == True, members))))

    #Beer drinkers
    print('count beer drinkers:', str(count(list(filter(lambda x: x['favourite_beverage'] == 'beer', members)))))

    # Count coding languages
    for key, value in dict(map(lambda x: (x['coding_language'],
                    count(list(filter(lambda y: y['coding_language'] == x['coding_language'], members)))), members)).items():
        print(str(value), ' code in ', key)

    #Average age version 1
    print('average_age:', str(functools.reduce(lambda x, y : x + y, list(map(lambda y: y['age'],members)))/len(members)))

    #Average age version 2
    print('average_age:', str(functools.reduce(operator.add, list(map(lambda y: y['age'],members)))/len(members)))
