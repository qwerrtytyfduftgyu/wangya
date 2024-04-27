# 字典是以键值对进行数据存储的
# dic = {"wy": "5",'2': "8"}
# s = dic["2"]
# print(s)
# 字典的key必须是可哈希的数据类型
# 字典的value可以是任何类型
# dic = {"我的孩子": [1,2,34,]}
# print(dic["我的孩子"])

# 字典的增删改查
# dic = {"fsf":"ws"}
# dic["jay"] = '周杰伦'# 增
# print(dic)
# dic["jay"] = '昆凌'# 存在键相同的情况下添加就是修改操作
# print(dic)
# dic.setdefault("jay","6")# 设置默认值，如果有key，那就不起作用了
# print(dic)
# dic.pop("jay")# 删除操作
# print(dic)
# print(dic["fsf"])# 查询操作
# print(dic.get("fsf"))# 查询操作
# 字典的循环和嵌套
# dict = {
#          "张三": "1",
#          "李四": "2",
#          "王五": "3",
#          "赵六": "4",
#         }
# for key in dict:# 使用for循环遍历字典时默认是key
#     print(key,dict[key])
#
# print(list(dict.keys()))#拿到所有的keys并放到一个列表中
# print(list(dict.values()))#拿到所有的vaules并放到一个列表中
# print(dict.items())#拿到所有的键值对


# 字典的循环删除
dict = {
         "张三": "1",
         "李四": "2",
         "王五": "3",
         "赵六": "4",
        }

temp = []
for i in dict:
    if i.startswith("张"):
        temp.append(i)

for t in temp:
     dict.pop(t)
     print(dict)