
import decimal
import sys
import re

string1 = input()
getNew = string1.replace("=", "-(") + ")"

'获得在本次方程中的未知数'
char1 = "".join([a for a in string1 if a.isalpha()])
varType = char1[0]

'将方程中a替换成1*a'
getNew = getNew.replace(varType,'1'+'*'+varType)
list1 = list(getNew)

'判断未知数前的字符并适当删除*'
i = 3;
while i < len(list1):
    if(list1[i] == varType):
        if(list1[i - 3].isdigit()):
            del list1[i - 2]
    i += 1;
getN = "".join(list1)

'输出成正确格式'
c = eval(getN, {varType: 1j})
num = decimal.Decimal("%.3f" % float(-c.real/c.imag))
print(varType + "=", end="")
sys.stdout.softspace = 0
print(num, end="");