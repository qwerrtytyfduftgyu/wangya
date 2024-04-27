"""
以下是关于类的一些代码
"""
# class  CuteCat:
#     def  __init__(self,color,name,price):
#         self.color = color
#         self.name = name
#         self.price = price
#
#     def mew(self,Content):
#         print("喵"*self.price +" "+ Content)
#
#
# cat1 = CuteCat("白","糯米",16)
# print(cat1.mew("strong"))
"""
定义一个关于学生的类！！！
"""
class StudentGrade:
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
        self.grades = {"语文": 0, "数学": 0, "英语": 0 }
    def SetGrades(self,course,grade):
        if course in self.grades:
            self.grades[course]=grade
    def print_grades(self):
        print(f"学生{self.name} (学号：{self.ID})")
        for course in self.grades:
            print(f"{course}:{self.grades[course]}")

# Wang = StudentGrade("小汪",210373113)
# Liu = StudentGrade("小刘",210373114)
# Wang.SetGrades("数学",100)
# print(Wang.grades)
# Wang.print_grades()

"""
定义一个关于计算圆周率的类
"""
class Yuan:
    def __init__(self,pi,radius):
        self.pi = pi
        self.radius = radius
        print(pi*radius**2)

Yuan1 = Yuan(3.14,5)
print(Yuan1)