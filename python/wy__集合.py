# # set集合
# # s ={}
# # print(type(s))###集合内没有元素就是字典
# # s = {1,2,3,'呵呵哒',6}
# # print(s)
# # python在对set集合进行创建时，需要考虑到数据类是否能哈希的问题
# # 一般能哈希的数据类型时不可变的数据类型，包括 int，str，（），bool
#
# # 创建空集合并实现集合的增删改查
# s = {2,3,5,6}
# s.add('1')#增
# s.add(1)
# print(s)
# s.remove(1)#删
# print(s)
# s.remove("1")#修改得先删后增
# s.add(23)
# print(s)
# for i in s:#查
#     print(i)
