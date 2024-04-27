# import cv2 as cv
# if __name__ == '__main__':
#      video = cv.VideoCapture(0)
#      while video.isOpened():
#          ret,frame = video.read()
#          if ret is True:
#              frame = cv.flip(frame,1)
#              cv.imshow('video',frame)
#              cv.waitKey(int(60/video.get(cv.CAP_PROP_FPS)))
#              if cv.waitKey(1) & 0xFF == ord('q'):
#                 break
#          else:
#            break
#      print('视频中图像的宽度为：',format(video.get(cv.CAP_PROP_FRAME_WIDTH)))
#      print('视频中图像的高度为：',format(video.get(cv.CAP_PROP_FRAME_HEIGHT)))
#      print('视频帧率为：',format(video.get(cv.CAP_PROP_FPS)))
#      print('视频总帧数为：',format(video.get(cv.CAP_PROP_FRAME_COUNT)))
#      video.release()
#      cv.destroyAllWindows()
#
