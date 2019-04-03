num = input()
num = [int(i) for i in num.split()]
n = num[0]
L = num[1]

vGoods = input()
vGoods = [int(i) for i in vGoods.split()]
j = 0
while j < 22 - n:
    vGoods.append(0)
    j += 1

s = 0
ans = 0

while s < (1 << n):
    summary = 0
    i = 0
    while i < n:
        if (s >> i) & 1:
            summary += vGoods[i]
        i += 1
    if summary <= L:
        ans += 1
    s += 1
print(ans)