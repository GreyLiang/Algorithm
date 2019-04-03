import queue
import time

'''题目描述
在桌子上有1摞卡片，每个卡片有一个正整数编号，从上到下卡片的编号为1到n，
现在进行n次操作，每次操作先扔掉最顶端的卡片，
然后将新的最顶端的卡片（如果有）放到这摞卡片的底部。 
设第i次操作扔掉了编号为j的卡片（i从1开始），
那么这次操作能加的分数为j%i分，
求n次操作完成后的总分。

输入数据
一个正整数n，n<1000000

输出数据
每次扔掉卡片的编号，中间用空格分隔'''


n = int(input())
ans = 0
i = 1
q = queue.Queue()
while i <= n:
    q.put(i)
    i += 1

j = 1
while j <= n:
    ans += q.get() % j
    if q.empty():
        break
    q.put(q.get())
    j += 1
print(ans)