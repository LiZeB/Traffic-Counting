import os
from moviepy.editor import *
import cv2


def moivePy_clip():
    """"
    用moivepy库进行视频剪辑
    """

    start = 30
    end = 60
    file = os.path.join(os.getcwd(), 'data/result.mp4')
    name, ext = file.split('.')
    clip = VideoFileClip(file).subclip(start, end)
    new_file = name + '_edited.' + ext
    clip.write_videofile(new_file)


def opencv_clip():
    """
    用python-opencv进行视频剪辑
    """

    videoCapture = cv2.VideoCapture('data/006M.flv')
    fps = 25    # 保存视频的帧率
    size = (704, 576)   # 保存视频的大小
    start = 30
    end = 60
    file = os.path.join(os.getcwd(), 'data/006M.flv')
    name, ext = file.split('.')
    new_file = name + '_edited.' + ext

    videoWriter = cv2.VideoWriter(
        new_file, cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'), fps, size)
    i = 0

    while True:
        success, frame = videoCapture.read()
        if success:
            i += 1
            if(i >= start and i <= end):
                print('i = ', i)
                videoWriter.write(frame)
            elif i > end:
                break


if __name__ == "__main__":
    opencv_clip()
