
# #单行代码实现八皇后
# _=[__import__('sys').stdout.write
#    ("\n".join('.' * i + 'Q' + '.' * (8-i-1) for i in vec) + "\n===\n")
#    for vec in __import__('itertools').permutations(range(8))
#    if 8 == len(set(vec[i]+i for i in range(8))) == len(set(vec[i]-i for i in range(8)))]

#base64加密形式实现八皇后
# import base64
# exec(base64.b64decode('ZnJvbSBpdGVydG9vbHMgaW1wb3J0ICoNCmNvbHMgPSByYW5nZSg4KQ0KY291bnQgPSAwDQpmb3IgdmVjIGluIHBlcm11dGF0aW9ucyhjb2xzKToNCiAgICBpZiAoOCA9PSBsZW4oc2V0KHZlY1tpXStpIGZvciBpIGluIGNvbHMpKQ0KICAgICAgICAgID09IGxlbihzZXQodmVjW2ldLWkgZm9yIGkgaW4gY29scykpKToNCiAgICAgICAgcHJpbnQodmVjKQ0KICAgICAgICBjb3VudCArPSAxDQpwcmludChjb3VudCk='))

#加密源码
# from itertools import *
# cols = range(8)
# count = 0
# for vec in permutations(cols):
#     if (8 == len(set(vec[i]+i for i in cols))
#           == len(set(vec[i]-i for i in cols))):
#         count += 1
# print(count)