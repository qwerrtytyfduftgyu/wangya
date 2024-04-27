'''
gbk编码2字节
UTF-8编码  中文3字节
          英文1字节
          欧文2字节
'''

# s = '汪雅'
# S = s.encode('gbk')# 将字符串以gbk方式解码 b‘xxxx’bytes类型
# S1 = s.encode('UTF-8')# 将字符串以UTF-8方式解码
# print(type(S))
# print(S)

# 将gbk编码变成UTF-8类型
b = b'\xcd\xf4\xd1\xc5'
B = b.decode('gbk')
B1 = B.encode('UTF-8')
print(B1)