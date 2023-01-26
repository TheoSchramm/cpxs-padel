from os import makedirs, path
from pathlib import Path
from datetime import datetime

import cv2

class VideoRecorder:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        self.cap.set(cv2.CAP_PROP_CONVERT_RGB, 1)
        self.width = 640
        self.height = 480

        self.fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        
        self.frame_list = []
        self.frame_limit = 30*30

        self.default_path = f'{Path.home()}\\Downloads\\CV2'
        
        if not path.exists(self.default_path):
            makedirs(self.default_path)
        
    def mouse_listener(self, event, x, y, flags, param):
        if event == cv2.EVENT_RBUTTONDOWN:
            date_string = datetime.now().isoformat(timespec= 'seconds', sep='-').replace(':', '-')
            out = cv2.VideoWriter(f'{self.default_path}//{date_string}.mp4', self.fourcc, 30.0, (self.width, self.height))
            for frame in self.frame_list:
                out.write(frame)
            out.release()
    
    def start(self):
        win_name = "Botao direito do mouse para gravar os ultimos 30 segundos ou Esc para fechar o programa"
        cv2.namedWindow(win_name)
        cv2.setMouseCallback(win_name, self.mouse_listener)
        
        while True:
            ret, frame = self.cap.read()
            cv2.imshow(win_name, frame)
            
            self.frame_list.append(frame)
            if len(self.frame_list) > self.frame_limit:
                self.frame_list.pop(0)
            
            if cv2.waitKey(1) & 0xFF == 27: #esc
                break
        cv2.destroyAllWindows()
        self.cap.release()

if __name__ == '__main__':
    VideoRecorder().start()
