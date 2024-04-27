# import cv2 as cv
# import sys
#
# if __name__ == '__main__':
#     img = cv.imread('./1.jpg')
#     if img is None:
#         print('好像没找到该图片！')
#         sys.exit()
#     else:
#         image = img.astype('float32')
#         image *= 1.0 / 255
#         # HSV = cv.cvtColor(image,cv.COLORMAP_HSV)
#         # YUV = cv.cvtColor(image,cv.COLOR_BGR2YUV)
#         # Lab = cv.cvtColor(image,cv.COLOR_BGR2Lab)
#         GRAY = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
#
#
#         cv.imshow('原图',image)
#         # cv.imshow('HSV',HSV)
#         # cv.imshow('YUV',YUV)
#         # cv.imshow('Lab',Lab)
#         # cv.imwrite('./Lab.jpg',Lab)
#         cv.imshow('GRAY',GRAY)
#
#
#     cv.waitKey(0)
#     cv.destroyAllWindows()
import numpy as np

# 目标函数
def objective_function(x):
    return x**2 + 10*np.sin(x)

# 初始化参数
num_wolves = 10
dim = 1
max_iter = 100

# 初始化灰狼群体
wolves = np.random.uniform(-10, 10, (num_wolves, dim))
alpha, beta, delta = wolves[:3]

# 优化循环
for iter in range(max_iter):
    # 计算每只狼的适应度
    fitness = np.array([objective_function(wolf) for wolf in wolves])

    # 更新Alpha、Beta和Delta
    sorted_indices = np.argsort(fitness)
    alpha, beta, delta = wolves[sorted_indices][:3]

    # 更新其他灰狼的位置
    for i in range(num_wolves):
        if i in sorted_indices[:3]:
            continue

        A1 = 2 * np.random.rand(dim) - 1
        A2 = 2 * np.random.rand(dim) - 1
        A3 = 2 * np.random.rand(dim) - 1

        C1 = 2 * np.random.rand(dim)
        C2 = 2 * np.random.rand(dim)
        C3 = 2 * np.random.rand(dim)

        D_alpha = abs(C1 * alpha - wolves[i])
        D_beta = abs(C2 * beta - wolves[i])
        D_delta = abs(C3 * delta - wolves[i])

        X1 = alpha - A1 * D_alpha
        X2 = beta - A2 * D_beta
        X3 = delta - A3 * D_delta

        wolves[i] = (X1 + X2 + X3) / 3

# 输出结果
best_position = alpha
best_fitness = objective_function(best_position)
print("Best Position:", best_position)
print("Best Fitness:", best_fitness)