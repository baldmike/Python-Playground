print "Hello, Everybody!"
x = "You're Great, man."
print x
# This is a comment 

# define a function that says hello to the name provided
# this starts a new block
def say_hello(name):
  #these lines are indented therefore part of the function
  if name:
   print 'Hello, ' + name + ' from inside the function'
  else:
   print 'No name - BUT STILL INSIDE THE FUNCTION'
# now we're unindented and have ended the previous block
print 'Outside of the function'

say_hello("SCOOBY")

first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)

stuff = "There are words you know, words I say, words"
print stuff.count("words")
print stuff.split()
print stuff[10]
print stuff.isalnum()

print stuff.endswith('s')
these = [1,3,4,2,5]
print these[1:3]
print sorted(these)
print these.index(3)

for number in range(1,14):
    print "Number-->", number

g = 1
while g < 11:
    print "G is-->", g
    g+=1

for val in "string":
    if val == "i":
        print "YIKES!"
        continue
    print val

for num in range(1,11):
    if num%2==0:
        print "*****"
    else: print " *****"
            