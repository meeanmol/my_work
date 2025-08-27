#First we talk about list 
#list are use  to store multiple value in ,multiple element 

#writing a an algoritm to shorting a list 

ar= [7,8,2,15,10,6]
min_val=ar[0]
for i in ar:
    if i<min_val:
        min_val=i

print("Lowest value:",min_val)