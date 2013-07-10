import threading
from inputs.microphone import microphone
from gl import queue
import time
import os
class Producer(threading.Thread):
    def __init__(self,debugInit):
        threading.Thread.__init__(self)
        self.debug=debugInit

    def run(self):
        global  queue
        while 1:
            timestamps=int(time.time());
            WAVPATH="/home/vincent/coding/python/piRobot/output%d.wav"%timestamps
            audioInput = microphone(WAVPATH,self.debug)
            audioInput.recordAudio()
            if audioInput.getSleepFLag() == 0:
                os.remove(WAVPATH)
            else:
                self.debug.saytxt("producter file:%s"%WAVPATH)
                queue.put(WAVPATH)
            time.sleep(3)

