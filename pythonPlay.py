numbers = [1, 2, 3, 4]

person = {"name": "Mia", "age":58, "hometown": "China"}

person["age"] = 22

for key in person.iterkeys():
    print key

for key, data in person.iteritems():
    print key, " = ", data    

if person.has_key("name"):
    print "The name is ", person["name"]

print person["age"]

print numbers[3]

print "*"*20

print str(person["age"])

joe = person.get("name")

print person.keys()

context = {
  'questions': [
   { 'id': 1, 'content': 'Why is there a light in the fridge and not in the freezer?'},
   { 'id': 2, 'content': 'Why don\'t sheep shrink when it rains?'},
   { 'id': 3, 'content': 'Why are they called apartments when they are all stuck together?'},
   { 'id': 4, 'content': 'Why do cars drive on the parkway and park on the driveway?'}
  ]
 }

for key, data in context.items():
     #print data
     for value in data:
          print "Question #", value["id"], ": ", value["content"]
          print "----"


print person.values()

print 100*"*"

dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
countries = ["Italy", "Germany", "Spain", "USA"]

country_food = zip(countries, dishes)
print country_food

country_food_dict = dict(country_food)
print country_food_dict

def odd_even():
    for i in range(1, 2001):
        if i%2 == 0:
            print i, " is an EVEN number"
        else:
            print i, " is an ODD number"

odd_even()

print 100*"*"

def multiply(list, times):
    j = 0
    for i in list:
        list[j] = i*times
        j = j + 1
    return list

x = [1,2,3]
y = 7
multiply(x, y)

def layered_multiples(arr):
    new_array = []
    j = 0
    for i in arr:
        new_array.append("1"*i)
    
    print new_array

x = [1,5,1]
y = 2
layered_multiples(multiply(x,y))

from random import random, randint



for i in range (1, 11):
    grade = randint(60, 101)
    if grade < 70:
        print i, grade, " is a D"
    elif grade < 80 and grade > 69:
        print i, grade, " is a C"
    elif grade < 90 and grade > 79:
        print grade, " is a B"
    elif grade > 89:
        print i, grade, " is a MOTHER FUCKING A!"
    
def coin_toss(x):
    heads = 0
    tails = 0
    for i in range (1, x+1):
        flip = randint(1,1000)
        if flip < 501:
            heads += 1
            print "toss #", i, ": HEADS! --> ", heads, " heads and ", tails, " tails all day."
            
        else:
            tails += 1
            print "toss #", i, ": TAILS! --> ", heads, " heads and ", tails, " tails all day."
            

coin_toss(999)

def stars(list):
    for i in range(0, len(list)):
        if isinstance(list[i], str):
            print list[i][0].lower() * len(list[i])

stars([1,2,3,4,23,12,6,"Bob"])

person = {"name": "BM", "age":12, "from":"Pleasantville", "favorite_language":"Python"}

def Who_am_I(person):
    print "my name is", person["name"]
    print "my age is", person["age"]
    print "i'm from", person["from"]
    print "and i love to talk me some", person["favorite_language"]

Who_am_I(person) 


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def print_ppl(arr):
    for key, data in arr.items():
        print "<-->", key.upper(), "<-->"
        for value in data:
            print "    ", value["first_name"], value["last_name"], len(value["first_name"]) + len(value["last_name"])
   
print_ppl(users)

print 100*"*"
# function input
my_dict123 = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

for data in my_dict123:
    print key