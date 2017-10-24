words = "It's Thanksgiving day.  It's my birthday, too!"
print words.find("day")

print words.replace("day", "month")

x = [2, 54, -2, 7, 12, 98]
max = 0;
min = 0;

for n in range(0, len(x)):
    if max < x[n]:
        max = x[n]
    if min > x[n]:
        min = x[n]

print "max: ", max
print "min: ", min

y = ["hello", 2, 43, 4, 563465, "apex", ["grapes", "Zenith"]]
print "first: ", y[0]
print "second: ", y[-1]
new = [y[0], y[-1]]
print new

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x

new1 = x[:len(x)/2]
print new1

new2 = x[len(x)/2:]
newArr = [new1]
print newArr + new2

#**************************************# 

for i in range(1, 1001):
    if i%2 != 0:
        print i

for j in range(5, 101):
    if j%5 == 0:
        print j

a = [1, 2, 5, 10, 255, 3]
add = 0

for i in range (0, len(a)):
    add += a[i]


print add
avg = add/len(a)
print avg

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn. Touch me, and I'll kill ya."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

def typeCast (x):
    if isinstance(x, int):
        if x >= 100:
            print "Why, that's huge!"
        else:
            print x, "is so small, sorry honey."
        
    elif isinstance(x, str):
        print x, "is a string, sweetheart"

    else:
        print x, "is a list, baby."


typeCast(spI)
typeCast(bS)
typeCast(mL)


#input
# l = ['magical unicorns',19,'hello',98.98,'world']
l = [2,3,1,7,4,12]
# l = ['magical','unicorns']

string = 0
integer = 0
sumOfIntegers = 0
sumOfString = 0

for i in range(0, len(l)):
    if isinstance(l[i], str):
        string += 1
    if isinstance(l[i], int):
        integer += 1
        sumOfIntegers += l[i]
    if isinstance(l[i], float):
        sumOfIntegers += float(l[i])

if string == len(l):
    print "YOUR INPUT IS ALL STRINGS, DARLIN'."
    print 

elif integer == len(l):
    print "YOUR INPUT IS ALL NUMBERS, BABY."
    print "The sum of which is: ", sumOfIntegers

else:
    print l, "IS A MIXED BAG, HONEY."
    print "The sum of which is: ", sumOfIntegers
    

# **************************************************# 
print 80*"*"

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]

same = True

for i in range(0, len(list_one)):
    if len(list_one) != len(list_two):
        same = False
    elif list_one[i] != list_two[i]:
         same = False

print same

print 80*"*"
# **************************************************# 

word_list = ['hello','world','my','name','is','Anna']
new_list = []
char = 'o'
# output
# 

def find_char (list, char):

    for i in list:
        if char in i:
            new_list.append(i)

    print new_list

find_char (word_list, char)


for j in range (1, 11):
    if j%2 == 0:
        print " ****"
    else:
        print "****"

print 80*"*"

def mult_table(col):

    table = []
    n = 1
    for i in range (n, col+n):
        if i < 10:
            sp = "  "
        elif i > 10:
            sp = " "
        table.append (sp + str(i))
    print " x", table

    table = []
    n = 1
    
    for j in range (n, col+1):
        
        for i in range (1, col+1):
            if i*n < 10:
                sp = "  "
            elif i*n > 9:
                sp = " "
            elif i*n > 99:
                sp = []
            table.append(sp + str(i*n))
        if n < 10:
            sp = " "    
        print sp + str(n), table
        table = []
        n += 1

mult_table(12)
        

# def prime (num):
for i in range (100, 10001):

    for k in range (2, i/2):
        if i%k == 0:
            yes = False


    
