import os

dec = int(input());
str = bin(dec).replace('0b','');
str = str.zfill(32);

strF = str[:16];
strB = str[16:32];
strN = strB + strF;

decN = int(strN,2);
print(decN);