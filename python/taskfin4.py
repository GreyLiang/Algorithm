n = int(input())
cityFirst = []
cityLast = []
city = []
i = 0
while i < n - 1:
    flying = input()
    flying = [int(i) for i in flying.split()]
    cityFirst.append(flying[0])
    cityLast.append(flying[1])
    i += 1

i = 1
while i <= n:
    if cityLast.count(i) == 0:
        city.append(i)
    i += 1

i = 0
while i < n - 1:
    m = cityFirst.index(city[i])
    city.append(cityLast[m])
    print(city[i])
    i += 1
    if i == len(cityLast):
        print(city[i])