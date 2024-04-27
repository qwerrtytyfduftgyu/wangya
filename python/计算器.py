print("哈喽，我是一个计算加减乘除的小程序！")
user_input1 = float(input("请输入第一个你要计算的数字："))
user_input2 = input("请输入你要计算的方式(加减乘除)：")
user_input3 = float(input("请输入第二个你要计算的数字："))
user_input4 = input("输入=将进行计算 ")
while  user_input4 != "=":
    if user_input2 == "+":
        print(user_input1+user_input3)
    elif user_input2 == "-":
        print(user_input1+user_input3)
    elif user_input2 == "*":
        print(user_input1*user_input3)
    elif user_input2 == "/":
        if user_input3 == 0:
           print("输入不能为0")
           break
        else:
           print(user_input1/user_input3)
           exit()
    else:
        print("输入有误请重新输入")
        break