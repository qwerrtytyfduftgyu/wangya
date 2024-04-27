# # user_input = input("请输入你想要打印的字符串：")
# #
# # for i in user_input:
# #     print(i.upper() + " " + i.lower())
# from datetime import datetime, timedelta
#
#
# def days_before(date_str, days):
#     # 将字符串日期转换为datetime对象
#     date = datetime.strptime(date_str, '%Y-%m-%d')
#
#     # 计算指定天数前的日期
#     new_date = date - timedelta(days=days)
#
#     # 将结果转换回字符串格式
#     return new_date.strftime('%Y-%m-%d')
#
#
# # 示例用法
# current_date_str = '2024-03-15'
# days_to_subtract = 5
#
# date_before = days_before(current_date_str, days_to_subtract)
# print(f"The date {days_to_subtract} days before {current_date_str} is {date_before}.")
def BMI (Height,Weight):
    Bmi = Weight/(Height**2)
    if user_sex == "男":
        sex = "先生"
    else:
        sex = "女士"
    if Bmi < 18.5:
        JIANYI = "体重过低，需增加营养"
    elif 18.5<=Bmi<24:
        JIANYI = "正常范围值"
    elif 24<=Bmi<28:
        JIANYI = "超重，注意控制饮食，减肥"
    elif Bmi>=28:
        JIANYI = "肥胖，需严格控制饮食，尽快减肥"
    print(f"{sex}您好，医生建议您：{JIANYI}")
    return Bmi

user_high = float(input("请输入你的身高(单位：米)："))
user_weight = float(input("请输入你的体重(单位：kg)："))
user_sex = input("请输入您的性别：")
print(f"您的BMI指数为{BMI(user_high,user_weight)}")