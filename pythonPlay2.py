print 100*"*"
# function input
my_dict123 = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

def toopull(dict):
  new_arr = []
  for key, data in my_dict123.iteritems():
        new_arr.append((key, data))
  print new_arr

toopull(my_dict123)
  
print 100*"*"

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]


def make_dict(arr1, arr2):
  if len(arr1) >= len(arr2):    
    new_dict = zip(arr1, arr2)
    new_dict2 = dict(new_dict)
  else:
    new_dict = zip(arr2, arr1)
    new_dict2 = dict(new_dict)
  print new_dict2
    
make_dict(name, favorite_animal)

print 100*"*"

