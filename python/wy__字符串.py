'''
字符串的操作等
'''
# 索引
# s = '我叫汪雅'
# print(s[2])
# print(s[-1])
# 切片  从左往右
# s = '我叫周杰伦,你叫周润发吗？'
# print(s[0:5])
# print(s[:5])
# print(s[6:10])
# print(s[6:])
# print(s[-3:-1])
# 切片 从右往左
# s = '我爱你'
# print(s[::-1])
# s = 'wqdfsvsFGsgfg'
# print(s[1:10:2])
# print(s[-1:-10:-3])
## 字符串基本操作

# s = 'python'
# s1 = s.capitalize()#单个单词首字母大写
# print(s1)

# s = 'i have a dream'
# s1 = s.title()#所有单词首字母大写
# print(s1)

# s = 'I HAVE A DREAM'
# s1 = s.lower()# 单词大写变小写
# print(s1)

# s = 'i have a dream'
# s1 = s.upper()#将所有小写字母变大写
# print(s1)
# 网站验证码忽略大小写
# verity_code = 'sADdaAS'
# while 1:
#         user_input = input('请输入密码：')
#         if verity_code.upper()==user_input.upper():
#              print("验证码正确")
#              break
#         else:
#              print("验证码错误")
#              continue

## 字符串替换和切割
# user_name = input("请输入你的用户名：").strip()#用户登录案例
# user_pd = input("请输入你的密码：").strip()
# if user_name == 'admin':
#     if user_pd == '123456':
#         print("登录成功")
#     else:
#         print("登陆失败")

# s = '你好，我叫胡桃'#字符串替换
# s1 = s.replace("胡桃",'汪雅')
# print(s1)

# s = 'hello i am hutao'
# s1 = s.replace(" ","")#去除字符串中的空格
# print(s1)
# a = 'python_c_javascript_c#'
# a1 = a.split("_ ")
# print(a1)

## 字符串查找和判断
# s = "你好啊，我叫周润发"
# ret = s.find("周润发")
# ret1 = s.index("周润发")
# print(ret)
# print(ret1)
# print("周润发" in s)
# print("周润发" not in s)
# name = input("请输入你的名字：")#判断字符串是以什么开头 endswith以什么结尾
# if name.startswith("张"):
#     print("我猜你姓张")
# else:
#     print("我猜你不姓张")

# money = input("请输入你的钱钱：")
# if money.isdigit():
#     print("可以花钱了！")
# else:
#     print("对不起，你输入的有误")
##  字符串补充和总结
# s = "hero is you"#字符串长度
# print(len(s))
# s = ("python_c_java_c#_javascript")#字符串分割
# ret = s.split("_")
# print(ret)

lst = ['python', 'c', 'java', 'c#', 'javascript']#字符串合并
s = "_".join(lst)
print(s)