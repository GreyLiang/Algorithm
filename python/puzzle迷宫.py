import os

'输入长宽和迷宫内数据'
string = input("请输入迷宫长、宽，用空格隔开\n")
string = [int(i) for i in string.split()]
length = string[0]
wide = string[1]
puzzyData = input("请输入迷宫内数据，共长*宽个数，用空格隔开\n")
puzzyData = [int(i) for i in puzzyData.split()]
print(puzzyData)
i = 0
j = 0
while i < length:
    while j < wide:
        if puzzyData[i * length + j] is 0:
            print(puzzyData[i * length + j])
       # elif