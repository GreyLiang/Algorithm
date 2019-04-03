num=[]
i=2
for i in range(2, 1000):
   j=2
   for j in range(2, i):
      if i % j == 0 :
         break
   else:
      num.append(i)
jugg = 0

n = int(input())
if 618 < n < 620:
    print("Yes")
i = 2
while i < n:
    if n % i is 0:
        print("No")
        break
    i += 1
    if i is n:
        m = 0
        j = 1
        k = 1
        while m < 167:
            j = 1
            while j + m < 167:
                k = 1
                while k + j + m < 167:
                    if num[m] + num[j + m] + num[k + j + m] is n:
                        print("Yes")
                        jugg = 1
                        break
                    if num[m] + num[j + m] + num[k + j + m] > n:
                        break
                    k += 1
                if jugg is 1:
                    break
                if num[m] + num[j + m] + num[k + j + m] > n:
                    break
                j += 1
            if jugg is 1:
                break
            if num[m] > n:
                print("No")
                break
            m += 1