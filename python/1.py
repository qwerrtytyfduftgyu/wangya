# # SUM=0
# # I=1
# # while I<=100:
# #     SUM=SUM+I
# #     I+=1
# #     print(SUM)
# # SUM=0
# # I=1
# # for I in range(1,101) :
# #     SUM+=I
# #     I+=1
# #     print(SUM)
# # data = {'tokyo': 1 , 'new york': 2}
# # for key, value in data.items():
# #     print(key,end=':')
# #     print(value)
# # class Company:
# #     def _init_(self, sales, cost, persons):
# #         self.sales = sales
# #         self.cost = cost
# #         self.persons = persons
# #
# #
# #     def get_profit(self) :
# #         return self.sales - self.cost
# #
# # company_A = Company(100,80,10)
# # company_B = Company(40,60,20)
# #
# # print(company_A.sales)
# # print(company_A.get_profit())
#
# # print('%x.%X'%(15,15))
# # list1 = [1,2,3,10.9,'abc',5,6,8,9,70]
# # list2 =[]
# # # print(list1[::2])
# # # list1.insert(2,6)
# # # del list1[6]
# # list1.remove('abc')
# # print(list2.append('abc'))
# # print(list1)
# # set1 =set('SFsfsfdfssd')
# # print(set1)
# # set1.remove('s')
# # print(set1)
# dict1 ={'name': '汪雅','age':'20','sex':'男'}
# # print(dict1.get('name'))
# # for (key,value) in dict1.items():
# #     print(key,value)
# dict1['weight']=140
# # print(dict1)
# # del dict1['weight']
# # print(dict1)
# # dict1.pop('age')
# print(dict1)
#  dict1.popitem()
#  print(dict1)
# print(list(dict1.keys()))
# print(list(dict1.values()))
# dict1.update({'name': 'wangya', 'age': '19'})
# print(dict1)
# print('a' in dict1)
# print('name' in dict1)
# def information(name,age,*args_tuple,**args_dict):
#     """注释行"""
#     print('name:',name)
#     print('age:',age)
#     print(args_tuple)
#     print(args_dict)
#     return
# information('汪雅',19,'szgs',wangya='19')
# result=lambda number1,number2:number1+number2
# print(result(10,20))
# a='''你好，我叫小明
# 今年18岁了
# 希望得到大家的认可'''
# print(a)
# name = '汪雅'
# age = '18岁'
# # print(name+age*5)
"""
简易的一个计算器
"""
# a = int(input("请输入一个数字："))
# b = int(input("请输入一个数字："))
# print('两数之和为%s'%(a+b))
# print(type(a))
# money = 500
# if money > 699:
#     print('晚上吃好的')
# print('别吃了，回宿舍躺着吧')
# money = int(input("请输入你的余额："))
# if money >= 1000:
#     print('今晚找妹子去')
# else:
#     print('回宿舍躺着')、
## 嵌套IF
# money = int(input("请输入你口袋里面的钱："))
# if money > 1000:
#     if money > 1888:
#         print("88号")
#     else:
#         print("1号")
# else:
#     print("回家呆着吧")
# money = int(input("请输入你口袋里面的钱："))
# if money > 5000:
#     print("充卡")
# elif money > 1000:
#     print("洗脚")
# elif money > 500:
#     print("门口看着吧")
# else:
#     print("回家吧")
a = 10
b = bool(a)
print(b)
