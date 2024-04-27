# import cv2 as cv
# # import sys
# # import numpy as np
# # import matplotlib.pyplot as plt
# #
# # if __name__ == '__main__':
# #     img = cv.imread('./1.jpg')
# #     if img is None:
# #         print('没找到该图片')
# #         sys.exit()
# #     else:
# #         zeros = np.ones(img.shape[:2],dtype=img.dtype) * 100
# #         result = cv.merge([img,zeros])
# #         print('原图的通道数为{}'.format(img.shape[2]))
# #         print('处理后的通道数为{}'.format(result.shape[2]))
# #
# #         plt.imshow(result)
# #         plt.show()
# #
# #         cv.imread('./1.png',result)
# if __name__ == '__main__':
#     fourcc = cv.VideoWriter__fourcc(*'DIVX')
#     video = cv.VideoCapture(0)
#     result = cv.VideoWriter('./save_VIDEO.avi',fourcc,20.0,(640,480))
#     while video.isOpened():
#         ret,frame = video.read()
#         if ret is True:
#             frame = cv.flip(frame,1)
#             result.write(frame)
#             cv.imshow('Video',frame)
#             cv.waitKey(25)
#             if cv.waitKey(1) & 0xFF == ord('q'):
#                 break
#         else:
#             break
# video.release()
# result.release()
# cv.destroyAllWindows()
#
import cv2 as cv
import numpy as np


if __name__ == '__main__':
    array = np.array([1,2,3,4,5,10,6,7,8,9,10,0])
    img1 = array.reshape((3,4))
    minval_1, maxval_1, minloc_1, maxloc_1 = cv.minMaxLoc(img1)
    print('图像img1中最小值为%s，其位置为%s' % (minval_1,minloc_1))
    print('图像img1中最大值为%s，其位置为%s' % (maxval_1, maxloc_1))

    img2 = array.reshape((3,2,2))
    img2 = img2.reshape((1,-1))
    minval_2, maxval_2, minloc_2, maxloc_2 = cv.minMaxLoc(img2)
    print('图像img2中最小值为%s，其位置为%s' % (minval_2, minloc_2))
    print('图像img2中最大值为%s，其位置为%s' % (maxval_2, maxloc_2))