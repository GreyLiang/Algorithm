num=[]
i=2
for i in range(2, 2000):
   j=2
   for j in range(2, i):
      if i % j == 0 :
         break
   else:
      num.append(i)

n = int(input())
count = []

i = 0
while i < 303:
    j = i
    while j < 303:
        if num[i] + num[j] == n:
            count.append(num[i])
            count.append(num[j])
        j += 1
    i += 1
print(count[0],count[1])