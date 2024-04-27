import cv2
from paddleocr import PaddleOCR, draw_ocr
import sys
import getopt
from PIL import Image

#使用 paddleocr识别 文本 并且框出文本位置 以及 用txt文件保存文本内容
def ocr_and_save_image(img_path):
    ocr = PaddleOCR(use_angle_cls=False, lang="ch")  # 只需要运行一次以下载和加载模型到内存中
    result = ocr.ocr(img_path, cls=False)

    res = result[0]  # 因为只有一张图片，所以结果只有1个，直接取出
    boxes = []  # 检测框坐标
    txt = ""  # 检测识别结果
    for line in res:
        txt += line[1][0] + "\n"  # 取出文本
        boxes.append(line[0])  # 取出检测框

    with open('file_txt2.txt', 'w') as f:  # 以w方式打开，没有就创建，有就覆盖
        f.write(txt)
    image = Image.open(img_path).convert('RGB')  # 读取原图片
    im_show = draw_ocr(image, boxes)  # 画检测框
    im_show = Image.fromarray(im_show)  # 转换
    save_path = 'res2.jpg'
    im_show.save(save_path)  # 保存

    return txt, save_path

cap = cv2.VideoCapture(1)
# VideoCapture 开启摄像头 0 为计算机自带摄像头 1 为外置摄像头
if not cap.isOpened():
    print("无法打开摄像头")
    exit()
should_exit = False
while not should_exit:
    # 读取摄像头帧
    ret, frame = cap.read()

    # 检查帧是否成功读取
    if not ret:
        print("无法读取摄像头帧")
        break

    # 显示帧
    cv2.imshow("摄像头", frame)

    # 按下 's' 键拍摄照片
    if cv2.waitKey(1) == ord('s'):
        # 保存照片
        cv2.imwrite("photo.jpg", frame)
        print("照片已保存")
        should_exit = True
# 释放摄像头和关闭窗口

img_path = 'photo.jpg'

ocr_and_save_image(img_path)
#需要先存储一张photo.jpg才会输出 file_text2.txt 和 res2.jpg
cap.release()
cv2.destroyAllWindows()
