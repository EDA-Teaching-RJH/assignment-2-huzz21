### Part Four -- your code goes here. 
import random
x = [random.randint(1,100) for a in range(10)]
print("Starting list of 10 numbers:", x)

a = 0
while a < len(x):
    if x[a] % 2 == 0:
        x.pop(a)
    else:
        a += 1

        print("Reimaining odd numbers:", x)