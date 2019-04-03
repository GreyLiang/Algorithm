
import math

num = input();
numN = [float(i) for i in num.split()];
p = numN[0];
q = numN[1];

i = 1;
while(i > 0):
    q1 = i*q/100
    p1 = i*p/100
    if(math.floor(p1) + 1 > math.ceil(q1) - 1):
        i += 1;
    else:
        break
print(i)