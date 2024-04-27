"""
测试break与continue在循环中的效果
"""
## while语句中
# while 1:
#     content = input("请输入你要喷的内容（输入q结束喷人）:")
#     if content == "q":
#         break
#     print("发送给下路:",content)
while 1:
    content = input("发送给射手的内容：")
    if content:
        print(content)
    else:
        break
