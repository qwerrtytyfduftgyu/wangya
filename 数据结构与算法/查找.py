# def linear_search(li,val):
#     for ind,v in enumerate(li):
#         if v == val:
#             return ind
#         else:
#             return None
#
#
# print(linear_search([1,2,3,4,5,6,7],3))
word = input("请输入你想要查询的单词：").upper()# 将输入的单词进行大写便于后面的查询操作
article = input("请输入你要查询的文章：").upper()# 将输入的文本进行大写便于后面的查询操作
words = article.split()
cnt = 0
pos = -1
cnt = words.count(word)
if cnt > 0:
    pos = article.index(word)
print(cnt,pos)
