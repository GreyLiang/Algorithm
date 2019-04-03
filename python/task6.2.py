n = int(input())
n3 = n5 = n7 = n
num = 0
counting = 0
countThree = 0
countFive = 0
countSeven = 0
i = j = k = 1
while n3 / 3 >= 1:
    countThree += 1
    n3 = n3 / 3
while n5 / 5 >= 1:
    countFive += 1
    n5 = n5 / 5
while n7 / 7 >= 1:
    countSeven += 1
    n7 = n7 / 7

while num < n:
    i = 0
    while i <= countThree:
        j = 0
        while j <= countFive:
            k = 0
            while k <= countSeven:
                num = pow(3, i) * pow(5, j) * pow(7, k)
                if num <= n:
                    counting += 1
                    k += 1
                else:
                    break
            j += 1
        i += 1
print(counting-1)