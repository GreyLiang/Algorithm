import math

f = [0,1]
a=(1 + math.sqrt(5))/2
i = 2

while i < 21:
    f.append(f[i - 1] + f[i - 2])
    i += 1
n = int(input())
if n < 2:
    print(f[n])
else:
    ans = -0.5 * math.log10(5.0) + n * math.log10(a)
    ans = pow(10,ans - math.floor(ans))
    answer = str(ans)
    answer = answer.replace(".","")
    print(answer)