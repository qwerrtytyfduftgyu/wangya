def hanoi(n,a,b,c):
    if n > 0:
        hanoi(n-1,a,c,b)
        print("从%s移动到%s" % (a,c))
        hanoi(n-1,b,a,c)

hanoi(3,"A","B","C")