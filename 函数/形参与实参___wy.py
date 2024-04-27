# def chi(zhu,fu,tang,tian):
#     print(zhu,fu,tang,tian)
#
#
# chi("饭",'生蚝','紫菜蛋花汤','蛋糕')

# def chi(*food):
#     print(food)
#
# chi("饭",'生蚝','紫菜蛋花汤')


# def chi(**food):
#     print(food)
#
#
# chi(zhu='饭',fu='生鱼片')
def suiji(a, b, *o, c="6", **bv):
    print(a, b, c, o, bv)


suiji(1, 2, (12, 35, 955), c=str(69), A="QW")
