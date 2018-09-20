# camera.py

import configparser
from torchvision import datasets, models, transforms
import torch
import PIL.Image as Image
from torch.autograd import Variable
import detecor
import cv2
import numpy as np
import  math

detector = detecor.Dector()



class VideoCamera(object):
    def __init__(self):
        self.i = 0
        self.sum_area = 0


        self.video = cv2.VideoCapture('/home/liev/PycharmProjects/wrj_1/video/123.mp4')

    def __del__(self):
        self.video.release()
    def get_frame(self):
        # self.video.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)  # 2560x1920 2217x2217 2952×1944 1920x1080
        # self.video.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
        global w,frames
        ret, frame = self.video.read()  # 逐帧采集视频流

        if ret:
            timer = cv2.getTickCount()
            frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

            b, g, r = cv2.split(frame)
            img = cv2.merge([r, g, b])
            im = Image.fromarray(img, "RGB")
            boxes = detector.detect(im)
            _img_dataset = []
            font = cv2.FONT_HERSHEY_SIMPLEX
            # print(boxes)
            if len(boxes) != 0:
                for k in range(len(boxes)):
                    x1, y1, x2, y2 = int(boxes[k][0]), int(boxes[k][1]), int(boxes[k][2]), int(boxes[k][3])
                    green = (0, 0, 255)
                    if self.i == 0:
                        w = x2 - x1
                        h = y2 - y1

                        cv2.line(frame, (x1, y1), (x1 + int(w / 4), y1), green)
                        cv2.line(frame, (x1, y1), (x1, y1 + int(h / 4)), green)
                        cv2.line(frame, (x1 + w, y1), (x1 + int(3 * w / 4), y1), green)
                        cv2.line(frame, (x1 + w, y1), (x1 + w, y1 + int(h / 4)), green)
                        cv2.line(frame, (x2 - w, y2), (x2 - int(3 * w / 4), y2), green)
                        cv2.line(frame, (x2 - w, y2), (x2 - w, y2 - int(h / 4)), green)
                        cv2.line(frame, (x2, y2), (x2 - int(w / 4), y2), green)
                        cv2.line(frame, (x2, y2), (x2, y2 - int(h / 4)), green)

                    if self.i % 10 == 0 and self.i > 0:
                        aver_area = np.abs(int(self.sum_area / 10))
                        w = int(math.sqrt(aver_area))
                        # cv2.rectangle(frame,(int(boxes[0][0]), int(boxes[0][1])), (int(boxes[0][2]), int(boxes[0][3])), (0, 0, 255), 1)
                        self.sum_area = 0
                        green = (0, 0, 255)

                    cx = int((x2 - x1) / 2 + boxes[0][0])
                    ch = int((y2 - y1) / 2 + boxes[0][1])
                    cv2.line(frame, (int(cx - w / 2), int(ch - w / 2)), (int(cx - w / 2) + int(w / 4), int(ch - w / 2)),
                             green)
                    cv2.line(frame, (int(cx - w / 2), int(ch - w / 2)), (int(cx - w / 2), int(ch - w / 2) + int(w / 4)),
                             green)

                    cv2.line(frame, (int(cx + w / 2), int(ch - w / 2)), (int(cx + w / 2) - int(w / 4), int(ch - w / 2)),
                             green)
                    cv2.line(frame, (int(cx + w / 2), int(ch - w / 2)), (int(cx + w / 2), int(ch - w / 2) + int(w / 4)),
                             green)

                    cv2.line(frame, (int(cx - w / 2), int(ch + w / 2)), (int(cx - w / 2) + int(w / 4), int(ch + w / 2)),
                             green)
                    cv2.line(frame, (int(cx - w / 2), int(ch + w / 2)), (int(cx - w / 2), int(ch + w / 2) - int(w / 4)),
                             green)

                    cv2.line(frame, (int(cx + w / 2), int(ch + w / 2)), (int(cx + w / 2) - int(w / 4), int(ch + w / 2)),
                             green)
                    cv2.line(frame, (int(cx + w / 2), int(ch + w / 2)), (int(cx + w / 2), int(ch + w / 2) - int(w / 4)),
                             green)

                    self.i += 1
                    area = (x2 - x1) * (y2 - y1)
                    self.sum_area = self.sum_area + area
                    # print(sum_area,66666666666666666666)
                img = np.array(img, dtype=np.uint8)
                # #转换通道BGR
                r, g, b = cv2.split(img)
                img = cv2.merge([b, g, r])
                # Calculate Frames per second (FPS)
            fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
            # print(fps, 'fps..................')
            # cv2.putText(frame, "FPS : " + str(int(fps)), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 250), 2);
            # cv2.imshow('img', frame)
            ret, jpeg = cv2.imencode('.jpg', frame)
            frames = frame
            # print(frame)
            # 对于 python2.7 或者低版本的 numpy 请使用 jpeg.tostring()
        else:

            ret, jpeg = cv2.imencode('.jpg', frames)
            self.video = cv2.VideoCapture('/home/liev/PycharmProjects/wrj_1/video/22.mp4')
            print()




        return jpeg.tobytes(),fps


if __name__=='__main__':
    a = VideoCamera()