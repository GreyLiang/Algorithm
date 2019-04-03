num = input()
num = [int(i) for i in num.split()]
n = num[0]
m = num[1]
stoneList = input()
stoneList = [int(i) for i in stoneList.split()]
stoneList.sort()
summary = [0, 0]

def ok(val):
    k = m
    st = 1
    en = 2
    while en <= n:
        d = summary[en] - summary[st]
        while d < val:
            en += 1
            k -= 1
            if k < 0:
                return 0
            if en > n:
                if st is 1:
                     return 0
                else :
                    return 1
            d = summary[en] - summary[st]
        st = en
        en += 1
    return 1

i = 2
while i <= n:
    summary.append(stoneList[i - 2] + summary[i - 1])
    i += 1
l = 0
r = 1000 * 1000 + 5
while l < r:
    mid = int((l + r + 1) / 2)
    if ok(mid):
        l = mid
    else:
        r = mid - 1
print(l)