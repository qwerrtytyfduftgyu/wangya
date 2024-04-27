import turtle as t
import random

t.setup(1.0, 1.0)
t.bgcolor('black')
t.ht()
# 雪中悍刀行人物
persons = '''雪中悍刀行—徐凤年—姜泥—徐骁—吴素—徐脂虎—徐渭熊—徐龙象—陈芝豹—南宫仆射
—李义山—赵楷—李淳罡—魏淑阳—王仙芝—洪洗象—裴南苇—赵珣—宁峨眉—青鸟—韩貂寺—舒羞—褚禄山
—楚狂奴—温华—黄阵图—鱼玄机—陈锡亮—赵衡—吕钱塘—赵凤雅—贾佳嘉—红薯—赵宣素—小地瓜-拓跋菩萨'''

persons = persons.replace('\n', '')
words = persons.split('—')
print(words)

# 小说人物类
class Xiaoshuo():
    def __init__(self):
        self.x = random.randint(-1000, 1000)  # 横坐标
        self.y = random.randint(-500, 500)    # 纵坐标
        self.f = random.uniform(-10, 10)   # 左右移动
        self.speed = random.randint(2, 6)  # 移动速度
        self.word = random.choice(words)  # 文字
        # 文字的颜色
        self.color = "#%02x%02x%02x" % (random.randint(0, 255),
                    random.randint(0, 255), random.randint(0, 255))

    # 1.写字
    def draw(self):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()
        t.color(self.color)
        t.write(self.word, font=('楷体', 24))

    # 2.xy坐标变化，实现文字的移动
    def move(self):
        # 当文字还在画布中时
        if self.y <= 500:
            self.y += self.speed  # 设置上下移动,y逐渐增加
            self.x -= self.speed + self.f  # 左右移动速度
        # 当文字漂出了画布时，重新生成文字
        else:
            self.x = random.randint(-1000, 1000)
            self.y = -500
            self.f = random.uniform(-10, 10)  # 左右移动
            self.speed = random.randint(1, 2)  # 移动速度
            self.word = random.choice(words)  # 文字
            # 文字的颜色
            self.color = "#%02x%02x%02x" % (random.randint(0, 255),
                                            random.randint(0, 255), random.randint(0, 255))

# 用列表保存对象
xiaoshuos = []
for i in range(180):
    xiaoshuos.append(Xiaoshuo())

# 开始写字+移动
while True:
    t.tracer(0)
    t.clear()
    for i in range(150):
        xiaoshuos[i].move()
        xiaoshuos[i].draw()
    t.update()

t.done()