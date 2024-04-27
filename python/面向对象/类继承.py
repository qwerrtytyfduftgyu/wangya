"""
关于类继承的一些代码
"""
class  Employee:
    def __init__(self,name,ID):
        self.name = name
        self.ID = ID
    def print(self):
        print(f"员工名字: {self.name},员工号: {self.ID}")
class  Fulltime(Employee):
    def __init__(self,name,ID,mouthly_salary):
        super().__init__(name,ID)
        self.mouthly_salary = mouthly_salary
    def caculate_mouthly_pay(self):
       return self.mouthly_salary
class PartTime(Employee):
    def __init__(self,name,ID,daily_salary,works_days):
        super().__init__(name,ID)
        self.daily_salary = daily_salary
        self.works_days = works_days
    def caculate_mouthly_pay(self):
       return  self.daily_salary*self.works_days

People1 = Fulltime("汪雅",210373113,10000)
print(People1.caculate_mouthly_pay())