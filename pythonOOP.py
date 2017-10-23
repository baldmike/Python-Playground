class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.logged = False
    def login(self):
        self.logged = True
        print self.name + " is logged in."
        return self
    def logout(self):
        self.logged = False
        print self.name + " is now logged out."
        return self



new_user = User("BM", "bm@email.com")
print new_user.email
new_user.login().logout()
print 100*"*"

class Bike(object):
    def __init__(self, name, price, max_speed, miles):
        self.name = name
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def displayInfo(self):
        print self.name+ " costs $" + str(self.price) + " goes", self.max_speed, "mph and has", self.miles, "miles on it."
        return self
    def ride(self):
        self.miles += 10
        return self
    def reverse(self):
        if self.miles >= 5:
            self.miles -= 5
            return self
        else:
            print "Your bike has died, it is now dead."
            return self

bike1 = Bike("Dave", 500, 25, 10)
bike1.displayInfo()
bike1.ride()
bike1.displayInfo()
bike1.reverse().reverse().reverse()
bike1.reverse()
bike1.displayInfo()

print 100*"*"

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
    def display(self):
        print "your tax on this vehicle is ", 100*self.tax, "%"

ex = Car(11000, 100, "full", 100)

print ex.tax

ex.display()

print 100*"*"

class Store(object):
    def __init__(self, products, location, owner):
        self.products = products
        self.location = location
        self.owner = owner

    def add_product(self, product):
        self.products.append(product)
        print self.products
        return self
    def remove_product(self, product):
        for i in self.products:
            if (i == product):
                self.products.remove(i)
                print i + " removed"
        return self
    def inventory(self):
        print str(self.products)
        return self

products = ["hat", "scarf", "shoes", "pants"]
address = {
    "number":269,
    "street":"Buttlove"
}
owner = {
    "first":"Bald",
    "last":"Mike"
}
BMart = Store(products, address, owner)


print BMart.owner["first"] + " " + BMart.owner["last"]
print str(BMart.location["number"]) + " " + BMart.location["street"]

BMart.remove_product('hat')
BMart.add_product("chicken")
    
BMart.inventory()
print 100*"*"

# instantiate class User
class User(object):
    # this method to run every time a new object is instantiated
    def __init__(self, name, email):
	# instance attributes 
        self.name = name
        self.email = email
        self.logged = True
    # login method changes the logged status for a single instance (the instance calling the method)
    def login(self):
        self.logged = True
        print self.name + " is logged in."
        return self
    # logout method changes the logged status for a single instance (the instance calling the method)
    def logout(self):
        self.logged = False
        print self.name + " is not logged in"
        return self
    # print name and email of the calling instance
    def show(self):
        print "My name is {}. You can email me at {}".format(self.name, self.email)
        return self
# THE ABOVE IS USER CLASS EXAMPLE ********************************************************************


# BELOW IS CLASS AND INHERITANCE EXAMPLE *************************************************************
class Vehicle(object):
    def __init__(self, wheels, capacity, make, model):
        self.wheels = wheels
        self.capacity = capacity
        self.make = make
        self.model = model
        self.mileage = 0
    def drive(self,miles):
        self.mileage += miles
        return self
    def reverse(self,miles):
        self.mileage -= miles
        return self
class Bike(Vehicle):
    def vehicle_type(self):
        return "Bike"
class Car(Vehicle):
    def set_wheels(self):
        self.wheels = 4
        return self
class Airplane(Vehicle):
    def fly(self, miles):
        self.mileage += miles
        return self
v = Vehicle(4,8,"dodge","minivan")
print v.make
b = Bike(2,1,"Schwinn","Paramount")
print b.vehicle_type()
c = Car(8,5,"Toyota", "Matrix")
c.set_wheels()
print c.wheels
a = Airplane(22,853,"Airbus","A380")
a.fly(580)
print a.mileage

bike1 = Bike(2,1,"Schwinn", "Panther")
print bike1.make

print 100*"*"

# * is the "splat" operator *****************************************************
def varargs(arg1, *args):
      print "Got "+arg1+" and "+ ", ".join(args)
varargs("one") # output: "Got one and "
varargs("one", "two") # output: "Got one and two"
varargs("one", "two", "three", "four", "five") # output: "Got one and two, three"

print 100*"*"

class Human(object):
    def __init__(self, intelligence, health, stealth, strength):
        self.intelligence = intelligence
        self.health = health
        self.stealth = stealth
        self.strength = strength

class Wizard(Human):
    def __init__(self, ):
        super(Wizard, self).__init__(100,10,10,10)   # use super to call the Human __init__ method
    def heal(self):
        self.health += 10
class Ninja(Human):
    def __init__(self):
        super(Ninja, self).__init__(100,100,50,50)    # use super to call the Human __init__ method
    def steal(self):
        self.stealth += 5
class Samurai(Human):
    def __init__(self):
        super(Samurai, self).__init__(50,50,10,10)  # use super to call the Human __init__ method
    def sacrifice(self):
        self.health -= 5

Baldy = Human(100, 100, 100, 100)
Bald = Wizard()
Jerry = Ninja()
print Bald.strength
print Jerry.health

print 100*"*"

# create Animal class and two child classes, dog and dragon  *******************************************************

class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
        print self.name + " walked, and their health is now: " + str(self.health)
        return self
    def run(self):
        self.health -= 5
        print self.name + " ran, and their health is now: " + str(self.health)
        return self
    def displayHealth(self):
        print self.name + "'s Health is " + str(self.health)
        return self

class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name, 150)
    def pet(self):
        self.health += 5
        print "You gave " + self.name + " a rub, and his health is now: " + str(self.health)
        return self

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon, self).__init__(name, 150)
    def fly(self):
        self.health -= 10
        print self.name + " Flew, now their health is " + str(self.health)


frank = Dog("frank")
frank.pet().displayHealth()

Timmy = Dragon("Timmy")
Timmy.fly()
print 60*"*" + "THAT WAS ANIMAL" + 60*"*"
# ******************************************************* MATH DOJO **********************************************
class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
        for i in args:
            self.result += i
        print self.result
        return self

md = MathDojo()

md.add(1,2,3,5)
print 60*"*" + "THAT WAS MATH DOJO" + 60*"*"
    