#Here i start stack 
# is a linear datastructure that follws the Last-in -last out principle ,it can hold many 
#element and the last element added s the first one to removed 

#stack is simple as list as in pyton 

# normal stack 

stack = []
stack.append(1)
stack.append(2)
stack.append(3)
stack.append(4)

print(stack)

top_element =  stack[-1]
print("Peek element :",top_element)

pop_element = stack.pop(2)
print("Deleted element :", pop_element)

print("After pop stack ",stack)
isEmpty=not bool (stack)

print("Size of Stack",len(stack))