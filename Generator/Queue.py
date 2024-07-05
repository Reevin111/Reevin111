"""QUeue=Queue in Python is a linear data structure with a rear and a front end, similar to a stack.
It stores items sequentially in a FIFO (First In First Out) manner.
The primary queue operations are as follows:
Enqueue: It adds an element to the end of the queue. When the queue reaches its total capacity, it reaches an overflow condition. The time complexity of enqueueing is O:1.
Dequeue: This operation removes an element from the queue. Since it bases the queue on a FIFO manner, it releases the items in the order of their additions. When the queue becomes empty, it reaches an underflow condition. The time complexity is O:1.
Front: It gives you the first item from the queue. The time complexity is O:1.
Rare: It gives you the last item from the queue. The time complexity is O:1.
standard methods are:
put(item): Inserts an element to the queue
get(): Gets an element from the queue
empty(): Checks and returns true if the queue is empty
qsize: Returns queue’s length
full(): Checks and returns true if the queue is full
maxsize(): Maximum elements allowed in a queue"""
from queue import Queue
num=Queue(maxsize=5)
num.put(10)
num.put(20)
num.put(30)

print(num.get())
print(num.get())
print(num.get())
print(num.get())