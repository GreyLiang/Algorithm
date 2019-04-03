num = input()
num = [int(i) for i in num.split()]

i = 0
arrList = [[0 for col in range(0)] for row in range(num[0])]

while i < num[0]:
    arr = input()
    arr = [int(i) for i in arr.split()]
    arrList[i] = arrList[i] + arr
    i += 1

arrStore = [[0 for col in range(0)] for row in range(num[1])]
k = 0
m = 0
while k < num[1]:
    j = num[0] - 1
    while j >= 0:
        arrStore[m] += str(arrList[j][k])
        j -= 1
    k += 1
    m += 1
print(arrStore)
s = " ".join('%s' %id for id in arrStore)
# s = s.replace("[","")
# s = s.replace("]","")
s = s.replace("'","")
s = s.replace(",","")
print(s)
i = 0
while i < len(s):
    print(s[i:i+num[0] * 2])
    i += num[0] * 2