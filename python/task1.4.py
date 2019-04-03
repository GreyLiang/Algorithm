import os

num = input();
num = [int(i) for i in num.split()];
resN = num[0] - num[1];
res = str(resN);

list = list(res);
length = len(res) - 3;

if(resN > 0):
    while length > 0:
        list.insert(length,',');
        length -= 3;
    str = "".join(list);
    print(str);
else:
    while length > 1:
        list.insert(length,',');
        length -= 3;
    str = "".join(list);
    print(str);