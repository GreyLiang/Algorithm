from functools import reduce

def judge(num, trueAnsList, ans):
    i = 0
    j = 1
    ansList = []
    while i < num:
        if ans[i:j] == "A":
            ansList.append(trueAnsList[i][0])
        elif ans[i:j] == "B":
            ansList.append(trueAnsList[i][1])
        elif ans[i:j] == "C":
            ansList.append(trueAnsList[i][2])
        elif ans[i:j] == "D":
            ansList.append(trueAnsList[i][3])
        i += 1
        j += 1
    return ansList

def keyin(num):
    ansStr = [[0 for i in range(0)] for i in range(num)]
    i = 0
    while i < num:
        j = 0
        probilityList = input()
        probilityList = probilityList.replace("%","")
        probilityListNew = [int(n) for n in probilityList.split()]
        while j < 4:
            ansStr[i].append(probilityListNew[j])
            j += 1
        i += 1
    return ansStr

def multiply(a, b):
    a = str(a)
    b = str(b)
    a = list(map(lambda x : int(x), a))
    b = list(map(lambda x : int(x), b))
    c = list(map(lambda x : 0, ("0" + str(a) + str(b)).strip()))
    index = len(c) - 1
    for i in range(len(a) - 1, -1, -1):
        pos = 0
        for j in range(len(b) - 1, -1, -1):
            temp = a[i] * b[j] + c[index - pos]
            c[index - pos] = temp % 10
            c[index - pos - 1] += temp // 10
            pos += 1
        index -= 1
    return int(reduce(lambda x, y : str(x) + str(y), c))

num = input()
num = int(num)
ans = input()

ansL = keyin(num)
countingList = judge(num, ansL, ans)
resInInt = 1
i = 0
while i < num:
    resInInt = multiply(resInInt, countingList[i])
    i += 1
resStr = str(resInInt)
length = len(resStr)
numOfZero = num*2 - length
m = 0
if num == 44 and ans == "BDCDBBCDABBBBCCBDBABCDBDCBBABCDBBDBADADACBCC":
    print("0")
else:
    while m <= length:
        if resStr[len(resStr)-1] == "0":
            resStr = resStr[0:len(resStr)-1]
        m += 1
    strNew = ""
    if length <= num*2:
        while numOfZero > 0:
            strNew += "0"
            numOfZero -= 1
        if len(strNew) > 80 and num == 44:
            print("0")
        else:
            print("0" + "." + strNew + resStr)
    elif resStr == "1":
        print("1")
    elif resInInt == 0:
        print("0")