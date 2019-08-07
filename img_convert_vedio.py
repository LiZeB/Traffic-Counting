"""
将处理过后的图片生成完整的显示视频
"""
import os
import cv2
import glob
import numpy as np
import win_unicode_console
win_unicode_console.enable()

image_path = './out3/processed_*.png'
fps = 25  # 视频每秒25帧
size = (704, 576)  # W×H

video = cv2.VideoWriter("./data/result4.mp4",
                        cv2.VideoWriter_fourcc('I', '4', '2', '0'), fps, size)

for item in glob.glob(image_path):
    print(item)
    img = cv2.imread(item)
    video.write(img)
video.release()
cv2.destroyAllWindows()
