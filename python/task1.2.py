
def keyInCredit():
    credit = input();
    credit = [int(i) for i in credit.split()];
    creditN = [int(i) for i in credit];
    return creditN

def keyInScore():
    score = input();
    score = [int(i) for i in score.split()];
    scoreN = [int(i) for i in score];
    return scoreN

def judgeScore(n,scoreN,creditN):
    fin = [0] * n;
    sco = [0] * n;
    '判定绩点'
    i = 0;
    while i < n:
        if scoreN[i] >= 90:
            fin[i] = 4.0;
        elif scoreN[i] >= 85:
            fin[i] = 3.7;
        elif scoreN[i] >= 82:
            fin[i] = 3.3;
        elif scoreN[i] >= 78:
            fin[i] = 3.0;
        elif scoreN[i] >= 75:
            fin[i] = 2.7;
        elif scoreN[i] >= 72:
            fin[i] = 2.3;
        elif scoreN[i] >= 68:
            fin[i] = 2.0;
        elif scoreN[i] >= 64:
            fin[i] = 1.5;
        elif scoreN[i] >= 60:
            fin[i] = 1.0;
        else:
            fin[i] = 0;
        i += 1;
    '计算GPA'
    j = 0;
    sum = 0;
    while j < n:
        sco[j] = fin[j] * creditN[j];
        sum = sum + creditN[j];
        j += 1;

    GPAi = 0;
    m = 0;
    while m < n:
        GPAi = GPAi + sco[m];
        m += 1;
    GPA = GPAi / sum;
    return GPA;

n = int(input());
while n != 0:
    creditInMain = keyInCredit()
    scoreInMain= keyInScore()
    res = judgeScore(n,scoreInMain,creditInMain)
    print('%.2f' % res)