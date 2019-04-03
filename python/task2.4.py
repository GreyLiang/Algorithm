inputarray = [5, 3, 4, 6, 7, 8, 9, 1, 2,6, 7, 2, 1, 9, 5, 3, 4, 8,1, 9, 8, 3, 4, 2, 5, 6, 7,8, 5, 9, 7, 6, 1, 4, 2, 3,4, 2, 6, 8, 5, 3, 7, 9, 1,7, 1, 3, 9, 2, 4, 8, 5, 6,9, 6, 1, 5, 3, 7, 2, 8, 4,2, 8, 7, 4, 1, 9, 6, 5, 5,3, 4, 5, 2, 8, 6, 1, 7, 9,]

def printin():
    a = list(input())
    return a

def isvalidline(a):
    for i in range(len(a) - 1):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                return False
    return True

def check(a):
    for i in range(9):
        row = []
        col = []
        for j in range(9):
            row.append(a[i * 9 + j])
            col.append(a[i + j * 9])
        if not isvalidline(row) or not isvalidline(col):
            return False

    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            smallarray = []
            for i in range(x, x + 3):
                for j in range(y, y + 3):
                    smallarray.append(a[i * 9 + j])
            if not isvalidline(smallarray):
                return False
    return True

def printout(a):
    if check(a) == True:
        print("Right")
    else:
        print("Wrong")

n = int(input())
i = 0
while i < n:
    a = printin()
    ans = check(a)
    printout(ans)
    i += 1

print(check(inputarray))
