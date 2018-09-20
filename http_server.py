# -*- coding:utf-8 -*-
from flask import Flask, render_template, Response
from camera import VideoCamera
import json
# from test.camera import VideoCamera
# from camera_opencv import Camera


app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

def gen(camera):
    global fps
    while True:

        frame ,fps= camera.get_frame()
        fps_feed()
        # print(fps)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')




@app.route('/video_feed')
def video_feed():
    global fps
    fps = 20
    print(json.dumps(fps))
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')
@app.route('/fps')
def fps_feed():

    print(json.dumps(fps))
    return json.dumps(fps)


if __name__ == '__main__':

    # app.run(host='192.168.2.50', debug=True,port=5000)
    app.run(host='0.0.0.0', debug=True,port=5000)


