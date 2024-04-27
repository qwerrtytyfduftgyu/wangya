import cv2
import numpy as np
import onnxruntime

# 加载ONNX模型
model = onnxruntime.InferenceSession("yolov5s.onnx")
input_name = model.get_inputs()[0].name
output_name = model.get_outputs()[0].name

# 打开摄像头
cap = cv2.VideoCapture(0)

while True:
    # 读取摄像头帧
    ret, frame = cap.read()
    if not ret:
        break

    # 对帧进行预处理
    # 将BGR图像转换为RGB图像
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # 调整图像大小
    img = cv2.resize(img, (224, 224))
    # 将图像数据转换为float32类型，并归一化到[0, 1]
    img_float = img.astype(np.float32) / 255.0
    # 增加批量维度
    img_float = np.expand_dims(img_float, axis=0)

    # 运行模型并获取结果
    outputs = model.run([output_name], {input_name: img_float})
    result = outputs[0][0]

    # 根据结果对帧进行标记（这里只是示例，具体取决于你的模型输出）
    # 假设result是一个包含概率的数组，我们只标记概率大于0.5的对象
    mask = result[0] > 0.5
    frame_mask = np.zeros_like(frame)
    frame_mask[mask] = frame[mask]

    # 显示结果
    cv2.imshow("Detection", frame_mask)

    # 等待键盘输入
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放摄像头和关闭窗口
cap.release()
cv2.destroyAllWindows()