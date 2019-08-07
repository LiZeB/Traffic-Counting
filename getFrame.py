import cv2
cap = cv2.VideoCapture('./data/videoplayback.mp4')  # 创建一个视频获取对象
flag = 0
while (cap.isOpened()):
    # cap.set(cv2.CAP_PROP_POS_MSEC, flag)  # 设置时间标记
    cap.set(cv2.CAP_PROP_POS_FRAMES, flag)  # 设置帧数标记
    ret, im = cap.read()  # 获取图像
    # cv2.waitKey(2000)#延时
    # cv2.imshow('a',im)#显示图像，用在循环中可以播放视频
    cv2.imwrite('./test1{}.jpg'.format(flag), im)  # 保存图片
    if not ret:
        break
