from datetime import datetime
from time import strftime

class Call(object):
    id_counter = 10000
    def __init__(self, name, number, reason, time = strftime("%X")):
        Call.id_counter += 1
        self.id = Call.id_counter
        self.name = name
        self.number = number
        self.reason = reason
        self.time = time
        CallCenter.call_list.append(self)

    def display(self):
        info = self.__dict__
        order = ['id', 'name', 'number', 'time', 'reason']
        for key in order:
            print key.upper(), '-', info[key]
        print 50*"*"
        return self
        
class CallCenter(object):
    call_list = []
    def __init__(self):
        self.calls = CallCenter.call_list
        self.queue = len(CallCenter.call_list)
    def info(self):
        print 20*"*"
        print "There are " + str(self.queue) + " calls in the queue:"
        for call in CallCenter.call_list:
            print str(call.id) + ", " + call.name + ", " + str(call.number) + ", " + " at " + str(call.time) + " RE: " + call.reason
    def add(self, name, number, reason, time = strftime("%X")):
        self.queue += 1
        Call(name, number, reason, time)
        return self
        

    def remove(self, *number):
        if not number:
            CallCenter.call_list.pop(0)
            self.queue -= 1
            return self
        else:
            for call in CallCenter.call_list:
                if call.number == number:
                    CallCenter.call_list.pop(0)
                    self.queue -= 1
                    return self
    
call1 = Call("Joe", 3125882300, "Birds in chimney")
call2 = Call("Dave", 3122021234, "Please help me, I've lost my mind")
call3 = Call("Larry", 8473547548, "Butt hurts, can't find glasses")

call1.display()
call2.display()

center = CallCenter()
center.info()

center.add("Bert", 3124768976, "Ever seen one like this?")
center.add("Mary", 3213345994, "Toe stuck in drainpipe")

center.remove()
center.info()




