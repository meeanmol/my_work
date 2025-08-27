#Here i started creating Stack using class method 

class Stack:
    def __init__(self):
        self.stack=[]

    def pop(self,element):
        if self.isEmpty():
            return "Stack is empty"
        else:
           self.stack.pop()

    def push(self,element):
        self.stack.append(element)

    def isEmpty(self):
        return len(self.stack)==0
    
    def peek(self):
        if self.isEmpty():
            return "Empty"
        else:
            return self.stack[-1]
        
    def size(self):
        return len(self.stack)    

my =Stack()

my.push("anmol")
my.push("Yadav")
my.push("vinay")
my.push("sHUBHAM")

print("Stack :",my)

print("Pop :",my.pop(my[1]))
print("stake after pop :",my)
print("Peek element :",my.peek())
print("Empty",my.isEmpty)
print("size of stack ",my.size())