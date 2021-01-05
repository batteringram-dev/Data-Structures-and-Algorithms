x = 7, 8, 3
for item in x:
    print(item)
    
# If we wanna get the index of the numbers in "x", then we need to use the command "enumerate"

x = 7, 8, 3
for index,item in enumerate(x):
    print(index,item)
