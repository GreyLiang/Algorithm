n = int(input())
numList = input()
numList = [int(i) for i in numList.split()]
i = 0
count = 0
while i < n - 1:
    j = i + 1
    while j < n:
        if numList[i] > numList[j]:
            count += 1
        j += 1
    i += 1
print(count)