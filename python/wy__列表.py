# ## 列表也有索引和切片
# # lst = ["张三丰","张无忌","guodegang"]
# # print(lst[0])
# # print(lst[0:3])
# # print(len(lst))
# # for i in lst:
# #     print(i)
# ## 列表的增删改查
# lst=[]
# lst.append("陈鑫")
# lst.append("刘源")
# lst.insert(0,"汪雅")
# lst.extend(["张三","李四"])
# print(lst)
#
# ## 删除
# ret = lst.pop(3)
# print(lst)
# print(ret)
# lst.remove("李四")
# print(lst)
#
# ## 修改
# lst[0] = "钟"
# print(lst)
#
# ## 查找
# print(lst[2])




'''
小练习----------修改姓张的人名为王
'''
## 遍历修改所有人名
# lst = ["张三","张无忌","张绍刚","张三","李四","王阿姨"]
# for item in range(len(lst)):
#     i = lst[item]
#     if i.startswith("张"):
#         new_name = "王"+i[1:]
#         print(new_name)
#         lst[item] = new_name
# print(lst)

## 列表补充
#  删除列表中姓张的人名
# lst = ['张三','张无忌','李四','李5']
# temp = []#增加一个临时存放的列表进行辅助·
# for i in lst:
#     if i.startswith("张"):
#         lst.remove(i)
#         continue
# print(lst)
## 安全稳妥的删除方式，新建一个新的列表，在其中存放要删除的列表，在用这个去删除要删除列表的东西
a = []
for i in range(1,101):
    a.append(i*i)
    if i == 100:
       print(a)
       break