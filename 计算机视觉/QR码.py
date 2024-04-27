#!D:\anconda\envs\py311
# -*- coding: utf-8 -*-
# @Time    : 2024/4/24 下午8:59
# @Author  : 汪雅
# @School  : 厦门华厦学院
# @FileName: QR码.py
# @Software: PyCharm
import cv2
from pyzbar import pyzbar
import time


def write_to_file(data, file_name):
    # 将单个数据写入文件
    with open(file_name, "a") as file:
        file.write(data + '\n')
        print(f"Data '{data}' written to {file_name}")


def decode_qr_code_from_camera(file_name):
    # 初始化摄像头
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("无法打开摄像头")
        return

    try:
        while True:
            # 从摄像头读取一帧
            ret, frame = cap.read()
            if not ret:
                print("无法读取帧")
                break

            # 转换为灰度图像
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # 解码图像中的所有二维码
            decoded_objects = pyzbar.decode(gray)

            for obj in decoded_objects:
                # 绘制矩形框
                cv2.rectangle(frame, (obj.rect.left, obj.rect.top),
                              (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height), (0, 255, 0), 2)

                # 将解码后的数据写入文件
                barcode_data = obj.data.decode("utf-8")
                write_to_file(barcode_data, file_name)

                # 显示解码后的数据在控制台上
                print(f"Detected QR Code: {barcode_data}")

            # 显示带有二维码的图像
            cv2.imshow("QR Code Scanner", frame)

            # 按 'q' 退出循环
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        # 释放摄像头资源
        cap.release()
        # 关闭所有OpenCV窗口
        cv2.destroyAllWindows()


# 调用函数并传入文件名
decode_qr_code_from_camera("qr_data.txt")
