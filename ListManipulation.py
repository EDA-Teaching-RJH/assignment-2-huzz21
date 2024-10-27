### Part Three -- your code goes here. 
x = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
x.sort()
while 1 in x:
    x.remove(1)
    x.extend([7,8])
    print(x)