num = input()
num = [int(i) for i in num.split()]
n = num[0]
k = num[1]
j = 0
ans = int(1)
while j < n - 1:
	if k % 2 is 1:
		ans *= 2
		k = int((k + 1) / 2)
	else:
		ans = ans * 2 + 1
		k = int(k / 2)
	j += 1
print(ans)
