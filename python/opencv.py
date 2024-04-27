import cv2
video = cv2.VideoCapture(0)
fps = video.get(cv2.CAP_PROP_FPS)
print(fps)
size = (int(video.get(cv2.CAP_PROP_FRAME_WIDTH)), int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)))
print(size)
user_input = input("终端输入\"Q”或者\"q“终止运行")
while True:
    ret, frame = video.read()
    cv2.imshow("frame", frame)
    c = cv2.waitKey(1)
    if user_input == "Q" or "q":
        break
video.release()
cv2.destroyAllWindows()
# import cv2 as cv
# #设置摄像头 0默认为
# cap = cv.VideoCapture(0)
# #cap.set(cv.CAP_PROP_FRAME_WIDTH,320)
# #cap.set(cv.CAP_PROP_FRAME_HEIGHT,240)
# while True:
#     #每次读取一帧摄像头或者视频
#     ret,frame = cap.read()
#     #将一帧frame显示出来，第一个参数为窗口名
#     cv.imshow('frame',frame)
#     #每次等待1ms 当esc按键被按下时退出显示
#     #ESC按键对应的键值为27
#     if(cv.waitKey(1)&0xff) == 27:
#         break
# #常规操作 释放资源
# cap.release()
# cv.destroyAllWindows()
