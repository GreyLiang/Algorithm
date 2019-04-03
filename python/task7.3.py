NAndK = input()
NAndK = [int(i) for i in NAndK.split()]
n = NAndK[0]
k = NAndK[1]
del NAndK
a = input()
a = [int(i) for i in a.split()]
i = 0
count = 0
while i < n:
    j = i + 1
    while j < n:
        if (a[i] + a[j]) % k is 0:
            count += 1
        j += 1
    i += 1
print(count)