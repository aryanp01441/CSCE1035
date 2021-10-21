num = int(input())

num = format(num, "b")
rnum = reversed(num)

count =""
for x in rnum:
    count += x
print(count)