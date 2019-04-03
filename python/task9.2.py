n = int(input())
arrList = [["" for col in range(0)] for row in range(n)]
i = 0
while i < n:
    string = input()
    string = string.replace("*","0")
    string = string.replace("#","1")
    arrList[i].append(str(string))
    i += 1
print(arrList)

