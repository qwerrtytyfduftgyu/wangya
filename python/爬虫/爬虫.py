import math
# print("Dad!!")
# print("Hello" + " World" + "!")
# print("He said \"I let\"s go")
# print("Hello!\nWorld!")
# print("""
#      静夜思
# 床前明月光，疑是地上霜。
# 举头望明月，低头思故乡。
# """)
# greet = " 您好，吃了吗 "
# print(greet + "zhangsan")
# a = -1
# b = -2
# c = 3
# print((-b + math.sqrt(b**2-4*a*c))/(2*a))
# print((-b - math.sqrt(b**2-4*a*c))/(2*a))
# a = "123456"
# b = a[2]
# print(b)
""" 查看字符串长度以及使用索引查找字符 """
# a = "Hello World!"
# print(len(a))
# print(a[len(a)-1])
"""用户输入测试"""
# user_age = input("请输入你的年龄：")
# user_name = input("请输入你的姓名：")
# print("知道了你的名字是 " + user_name + " 年龄是 20" + user_age)
"""BMI指数计算器"""
user_high = input("请输入你的身高(单位：米)：")
user_weight = input("请输入你的体重(单位：kg)：")
user_sex = input("请输入您的性别：")
user_BMI = float(user_weight)/(float(user_high)**2)
if  user_sex=="男":
    if user_BMI<=18.4:
       print("先生你好 "+"你的BMI指数为：" + str(user_BMI) + " 体质正常")
    elif user_BMI<=23.9:
       print("先生你好 "+"你的BMI指数为：" + str(user_BMI) + " 体质过重")
    elif user_BMI<=27.9:
       print("先生你好 "+"你的BMI指数为：" + str(user_BMI) + " 体质肥胖")
    elif user_BMI<=32.0:
       print("先生你好 "+"你的BMI指数为：" + str(user_BMI) + " 重度肥胖")
    else :
       print("先生你好 "+"你的BMI指数为：" + str(user_BMI) + " 没有参考")
else:
    if user_BMI<=18.4:
       print("女士你好 "+"你的BMI指数为：" + str(user_BMI) + " 体质正常")
    elif user_BMI<=23.9:
       print("女士你好 "+"你的BMI指数为：" + str(user_BMI) + " 体质过重")
    elif user_BMI<=27.9:
       print("女士你好 "+"你的BMI指数为：" + str(user_BMI) + " 体质肥胖")
    elif user_BMI<=32.0:
       print("女士你好 "+"你的BMI指数为：" + str(user_BMI) + " 重度肥胖")
    else :
       print("女士你好 "+"你的BMI指数为：" + str(user_BMI) + " 没有参考")


