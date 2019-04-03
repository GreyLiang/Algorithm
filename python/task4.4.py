
stringA = input()
Home = []
End = []

i = 0
while i < len(stringA):
    if stringA[i:i + 1] is "[":
        Home.append(i)
    elif stringA[i:i + 1] is "]":
        End.append(i)
    i += 1
j = 0
while j < len(Home):
    stringA = stringA[Home[j]:End[j]] + stringA[:Home[j]] + stringA[End[j]:]
    j += 1
stringA = stringA.replace("[","")
stringA = stringA.replace("]","")

print(stringA)