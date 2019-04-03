n = int(input())
numList = []

i = 1
while i <= 2000:
    j = 1
    count = 0
    while j <= i:
        if i % j is 0:
            count += 1
        j += 1
    numList.append(count)
    i += 1

count = 0
i = 0
while i < 2000:
    if numList[i] == n:
        print(i+1)
        count += 1
    i += 1
if count == 0:
    print("NO SOLUTION")