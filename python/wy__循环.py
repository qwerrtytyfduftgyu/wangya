"""
循环语句while与for计算1加到100的值

"""
## while语句
# i = 1
# SUM = 0
# while i < 101:
#     SUM = SUM + i
#     i = i + 1
#     print("1加到100的和为%s" % SUM)


""""
while计算1-2+3-4.......-100

"""
# i = 1
# SUM = 0
# while i < 101:
#     i = i + 1
#     if i % 2 == 0:
#         SUM = SUM - i
#     else:
#         SUM = SUM + i
#     print(SUM)
"""
for循环计数及计算器代码
"""
# i = 1
# for i in range(10):
#     print(i)
# for i in range(3,10):
#     print(i)
# for i in range(3,10,2):
#       print(i)
# s = "你好啊，我叫胡桃"
# for i in s:
#     print("这几个字符分别是," ,i)
SUM = 0
for i in range(101):
    SUM = SUM + i
    print(SUM)
