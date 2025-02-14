#Data Types:

# Integer
num = 10
print(type(num))  # Output: <class 'int'>

# Float
pi = 3.14
print(type(pi))  # Output: <class 'float'>

# String
text = "Hello, Python!"
print(type(text))  # Output: <class 'str'>

# Boolean
is_valid = True
print(type(is_valid))  # Output: <class 'bool'>


#type() Method:

x = [1, 2, 3]
print(type(x))  # Output: <class 'list'>

y = {"name": "Alice", "age": 25}
print(type(y))  # Output: <class 'dict'>


#For Loop:

for i in range(5):  # 0 to 4
    print(i)

fruits = ["apple", "banana", "cherry"]
for ind, fruit in enumerate(fruits):
    print(ind, fruit)

d = {(x, x + 1): x for x in range(10)} 
print(d)


#While Loop:
x = 0
while x < 5:
    print(x)
    x += 1


#if_else:
num = 10
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


#Type Casting:

# Integer to String
x = 10
y = str(x)
print(y, type(y))  # Output: '10' <class 'str'>

# String to Integer
z = "100"
z_int = int(z)
print(z_int, type(z_int))  # Output: 100 <class 'int'>

# Float to Integer
pi = 3.14
pi_int = int(pi)
print(pi_int)  # Output: 3


#List (Mutable, Ordered):

my_list = [1, 2, 3, 4]
my_list.append(5)  # Adds 5 at the end
print(my_list)  # Output: [1, 2, 3, 4, 5]

my_list.remove(2)  # Removes 2
print(my_list)  # Output: [1, 3, 4, 5]


#Tuple (Immutable, Ordered):
    
my_tuple = (1, 2, 3)
print(my_tuple[1])  # Output: 2
# my_tuple[1] = 10  # Error! Tuples are immutable


#Set:(Unordered, Unique Elements)

my_set = {1, 2, 3, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}

my_set.add(5)
print(my_set)  # Output: {1, 2, 3, 4, 5}


#Dictionary (Key-Value Pair, Mutable):

my_dict = {"name": "Alice", "age": 25}
print(my_dict["name"])  # Output: Alice

my_dict["age"] = 26  # Updating value
print(my_dict)  # Output: {'name': 'Alice', 'age': 26}


#Stack
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())  # Output: 30
print(s.peek()) # Output: 20
print(s.size()) # Output: 2


#Queue:
from collections import deque
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.popleft() if self.queue else "Queue is empty"

q = Queue()
q.enqueue(5)
q.enqueue(10)
print(q.dequeue())  # Output: 5



# Summary of Lab1:
# Data Types
num, pi, text, is_valid = 10, 3.14, "Hello", True

# Type Method
print(type(num), type(pi), type(text), type(is_valid))

# Loops
for i in range(3): print(i)
x = 0
while x < 2: print(x); x += 1

# If-Else
if num > 0: print("Positive")
elif num == 0: print("Zero")
else: print("Negative")

# Collections
my_list = [1, 2, 3]; my_list.append(4)
my_tuple = (1, 2, 3)
my_set = {1, 2, 3, 3}
my_dict = {"name": "Alice", "age": 25}

# Casting
x_str = str(num)
z_int = int("100")

# Stack
class Stack:
    def __init__(self): self.stack = []
    def push(self, item): self.stack.append(item)
    def pop(self): return self.stack.pop() if self.stack else "Stack empty"

s = Stack(); s.push(10); print(s.pop())

# Queue
from collections import deque
class Queue:
    def __init__(self): self.queue = deque()
    def enqueue(self, item): self.queue.append(item)
    def dequeue(self): return self.queue.popleft() if self.queue else "Queue empty"

q = Queue(); q.enqueue(5); print(q.dequeue())
