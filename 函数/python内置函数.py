"""
python内部已经写好的函数，可以直接拿来用的函数
"""
### 数据类型的内置函数
# s = "123"
# A = int(s)
# B = float(s)
# C = bool(s)
# print(A,B,C)
# # complex()数学里面的复数

### 进制转换的内置函数(bin,oct,hex)
# a = 125# 十进制
# print(bin(a))# 转二进制
# print(oct(a))# 转八进制
# print(hex(a))# 转十六进制
# print(int(0x6d))# 转十进制

### 数学运算的内置函数(pow,sum,mim,max)
# a = 10
# b = 3
# print(pow(a,b))# a的b次幂
# list = (1,55,666,89854,444,-255,-89521)
# print(min(list))
# print(max(list))
# print(sum(list))

### 数据结构的内置函数
# a = {1,2,3,4,5,6,1,9,8,5,}
# list = list(a)# list内部一定会有一个for循环
# print(list)
## format 格式化输出 ord,chr
# a = 18
# print(format(a,'08b'))# b:二进制,o:八进制,x:十六进制
# a = '国'  #python的内存中使用的是unicode
# print(ord(a))  # a这个字符在unicode中的码位为----
# print(chr(22269)) # 根据编码位置输出
# for i in range(65536):
#     print(chr(i)+" ",end=" ")
# s = "adfmllfk"
# print(len(s))

# enumerate,all,any
# print(any([0,2,"3"]))# 当成or来看就行
# print(all([0,"",123]))# 当成and来看就行

# lst = ["汪雅","张","赵","李"]
# for i in enumerate(lst):
#     print(i)

# hash,id,help
# a = '666'
# print(hash(a))
# print(id(a))

# help,dir
s = '666'
print(help(str))
print(dir(s))
