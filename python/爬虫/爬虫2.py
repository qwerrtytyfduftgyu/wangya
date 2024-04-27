# 列表
# shopping_list =[]
# shopping_list.append("键盘")
# shopping_list.append("键帽")
# shopping_list.append("电竞椅")
# # print(len(shopping_list))
# # print(shopping_list)
# # print(shopping_list[0])
# price = [600,50,6098,70]
# max_price = max(price)
# min_price = min(price)
# sorted_price = sorted(price)
# print(max_price,min_price,sorted_price)
# 元组与字典
# liuxinyu_2023  = {}
# liuxinyu_2023["新质生产力"] = "“新质生产力”代表一种生产力的跃迁，是科技创新发挥主导作用的生产力，是摆脱了传统增长路径、符合高质量发展要求的生产力，是数字时代更具融合性、更体现新内涵的生产力。“新质生产力”丰富了马克思主义生产力理论的内涵，为新时代全面推进我国经济持续健康、高质量发展，整合科技创新资源，引领发展战略性新兴产业和未来产业，提供了科学理论指导和行动指南。"
# liuxinyu_2023["双向奔赴"] = "本指相关方朝着共同的目标，一起努力，相互靠近。多用于人与人之间，表达了人们相互爱慕、相互亲近的美好愿望。“正是善意友好的涓滴汇流，让宽广太平洋不再是天堑；正是人民的双向奔赴，让中美关系一次次从低谷重回正道。”从用于个人到用于国家，“双向奔赴”的使用范围得到了延伸扩展，价值内涵得到了丰富升华。"
# liuxinyu_2023["人工智能大模型"] = "在人工智能领域，大模型是指拥有超大规模参数(通常在10亿个以上)、超强计算资源的机器学习模型，能够处理海量数据，完成各种复杂任务，如自然语言处理、图像识别等。计算机硬件性能不断提升，深度学习算法快速优化，大模型的发展日新月异。一系列基于大模型的人工智能应用相继问世，其中ChatGPT、“文心一言”等已经在社会生产、生活方面产生了广泛影响。大模型的普遍应用，也对隐私保护、信息安全等带来巨大挑战，迫切需要相关法律和管理措施的有效应对。"
# liuxinyu = input("请输入你想要查询的流行语：")
# if liuxinyu in liuxinyu_2023:
#     print("该流行语存在于2023年的流行语中,流行语内容如下：")
#     print(liuxinyu_2023[liuxinyu])
#     print("2023年的流行语共有"+str(len(liuxinyu_2023))+"条")
# else:
#     print("抱歉，不存在")
# Temperature = {"110":33.2,"111":33.9,"112":35.6,"113":39.3,"114":36.5,"115":32.9,"116":39.6}
# t = {}
# for gonghao,wendu in Temperature.items():
#     if wendu >= 38:
# # print("发烧的人有"+str(len(Temperature)))
#        print(gonghao)
# print("哈喽，我是一个计算平均值的python程序")
# total = 0
# count = 0
# user_input = input("请输入你想要求平均数的数字(最后输入q进行计算)：")
# while user_input != "q":
#       num =float(user_input)
#       total +=num
#       count +=1
#       user_input = input("请输入你想要求平均数的数字(最后输入q进行计算)：")
# if count == 0:
#       result=0
# else:
#       result = total/count
# print(result)
"""
爬取http://books.toscrape.com/源文件
"""
import requests
from bs4 import BeautifulSoup
response = requests.get("http://books.toscrape.com/")
if response.ok:
    print(response.text)
else:
    print("请求失败")
soup = BeautifulSoup(response.text,"html.parser")
"""
获取价格
"""
# all_prices = soup.findAll("p",attrs={"class":"price_color"})
# for price in all_prices:
#     print(price.string[2:])
"""
获取书名标题
"""
all_name = soup.findAll("h3")
for title in all_name:
    all_title = title.findAll("a")
    for Name in all_title:
        print(Name.string)
