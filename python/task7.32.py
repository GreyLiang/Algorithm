NAndK = input()
NAndK = [int(i) for i in NAndK.split()]
n = NAndK[0]
k = NAndK[1]
del NAndK
a = input()
a = [int(i) for i in a.split()]
b = []
i = 0
while i < n:
    temp = a[i] % k
    b.append(temp)
    i += 1
del a
j = 0
counting = 0
while j < n:
    m = j + 1
    while m < n:
        if (b[j] + b[m]) % k is 0:
            counting += 1
        m += 1
    j += 1
print(counting)