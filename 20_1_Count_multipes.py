low = int(input())
high = int(input())
x = int(input())

i = 0
counter = 0
for i in range(low, high, x):
    counter += 1
print(counter)