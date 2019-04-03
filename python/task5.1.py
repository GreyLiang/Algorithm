n = int(input())
N = n + 1
i = 1
j = 1
a = [1 for i in range(N)]
print(a)
while i <= n:
    while j <= n:
        if j%i is 0:
            a[j] = 1
        j += 1
    i += 1
print(a)