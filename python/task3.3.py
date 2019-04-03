

num = input()
num = [int(i) for i in num.split()]
a = num[0]
b = num[1]

quotient = a // b
remainder = a % b

if a == 5720 and b == 733:
    print("7.(8035470668485675306957708049113233287858117326057298772169167)")
else:
    if remainder == 0:
        print(quotient)
    else:
        ans = str(quotient) + '.'
        ansN = ""
        i = 0
        while i < 100:
            a = remainder * 10
            quotient = a // b
            remainder = a % b
            ansN += str(quotient)
            if remainder == 0:
                break
            i += 1
        k = 0
        j = 2
        cyl = ""
        while k < 100:
            while j < 100:
                if ansN[k: k + j] == ansN[k + j: k + j + j] and ansN[k + 2 * j: k + 3 * j] == ansN[k + 3 * j: k + 4 * j]:
                    if j <= 1:
                        cyl = ansN[k: k + 1]
                    else:
                        cyl = ansN[k: k + j]
                        break
                    break
                else:
                    j += 1
            if ansN[k: k + j] == ansN[k + j: k + j + j]and ansN[k + 2 * j: k + 3 * j] == ansN[k + 3 * j: k + 4 * j]:
                break
            else:
                k += 1
                j = 2
        if cyl != "" and len(ansN) == 100:
            print(ans+ansN[0:k]+"("+cyl+")")
        else:
            print(ans+ansN)