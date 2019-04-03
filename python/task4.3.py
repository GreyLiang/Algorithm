count = 0
num = 0
while count <= 1500:
    if num % 2 is 0:
        count += 1
    elif num % 3 is 0:
        count += 1
    elif num % 5 is 0:
        count += 1
    num += 1
print(num,count)