class Node:
    def __init__(self,value):
        self.value = value  
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
    def push(self , value):
        new_node  = Node(value)
        if self.head :
            new_node.next = self.head
        self.head = new_node  
        self.size +=1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty " 
        popped_element = self.head
        self.head = self.head.next
        self.size -= 1
        return popped_element.value
    def peek(self):
        if self.isEmpty():
            return "stack is empty "
        return self.head.value
    def isEmpty(self):
        return self.size == 0
    
    def tran(self):
        currenNode = self.head 
        while currenNode :
            print(currenNode.value , end= "->")
            currenNode = currenNode.next
        print()

    def Size(self):
        return self.size


mystack = Stack()
mystack.push("A")
mystack.push("B")
mystack.push("C")
mystack.push("D")


print("LinkedList :", end="")
mystack.tran()
print("Peek : ",mystack.peek())
print("popped :",mystack.pop())
print("Linklist after Poped element :", end ="")
mystack.tran()
print("Is Empty :",mystack.isEmpty())
print("size ",mystack.Size())