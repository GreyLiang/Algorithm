stopword = ''
str = []
for line in iter(input, stopword):
    str.append(line)

subXing = '*'
subJing = '#'
strListNew = []

i = 0
while i < len(str):
    strN = str[i]
    countXing = strN.count(subXing)
    countJing = strN.count(subJing)
    m = 1
    while m <= countXing:
        if m % 2 != 0:
            strN = strN.replace('*','<i>',1)
        else:
            strN = strN.replace('*','</i>',1)
        m += 1
    n = 1
    while n <= countJing:
        if n % 2 != 0:
            strN = strN.replace('#','<b>', 1)
        else:
            strN = strN.replace('#','</b>', 1)
        n += 1
    strListNew.append(strN)
    i += 1

i = 0
while i < len(strListNew):
    print(strListNew[i])
    i += 1
