import time
import cv2
#import pyautogui
import sys
import datetime
from timeout_decorator import timeout, TimeoutError

#cap0 = cv2.VideoCapture(r"blink.mp4")
cap1 = cv2.VideoCapture(r"surprise.mp4")
#cap2 = cv2.VideoCapture(r"fear.mp4")
cap3 = cv2.VideoCapture(r"disgust.mp4")
cap4 = cv2.VideoCapture(r"anger.mp4")
cap5 = cv2.VideoCapture(r"joy.mp4")
cap6 = cv2.VideoCapture(r"sadness.mp4")

  
@timeout(8)    
def func(inputNum):
    inputNum = input()
    print("ros get num",inputNum)
    if inputNum == "1":
        movie1()
    elif inputNum == "2":
        movie2()
    elif inputNum == "3":
        movie3()
    elif inputNum == "4":
        movie4()
    elif inputNum == "5":
        movie5()
    elif inputNum == "6":
        movie6()
        """
    elif inputNum == "7":
        sys.exit()
        """
    
    time.sleep(5)

def callback():
    print("callback")
    movie0()
    
def movie0():
    print("movie0 start")
    cap0 = cv2.VideoCapture(r"blink.mp4")
    """
    pyautogui.moveTo(300,1060)
    pyautogui.click()
    """
    while True:
        ret1, frame1 = cap0.read()
        if ret1:
            frame1 = cv2.resize(frame1, (1920, 1080))
            #cv2.namedWindow('WinName',cv2.WINDOW_NORMAL)
            #cv2.setWindowProperty('WinName',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.imshow("frame1", frame1)
            cv2.waitKey(10)
        else:
            cap0.set(cv2.CAP_PROP_POS_FRAMES, 0)
            break

def movie1():
    print("movie1 start")
    while True:
        ret1, frame1 = cap1.read()
        if ret1:
            frame1 = cv2.resize(frame1, (1920, 1080))
            #cv2.namedWindow('WinName',cv2.WINDOW_NORMAL)
            #cv2.setWindowProperty('WinName',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.imshow("frame1", frame1)
            cv2.waitKey(10)
        else:
            cap1.set(cv2.CAP_PROP_POS_FRAMES, 0)
            break
        
def movie2():
    print("movie2 start")
    cap2 = cv2.VideoCapture(r"fear.mp4")
    while True:
        ret1, frame1 = cap2.read()
        if ret1:
            frame1 = cv2.resize(frame1, (1920, 1080))
            #cv2.namedWindow('WinName',cv2.WINDOW_NORMAL)
            #cv2.setWindowProperty('WinName',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
            cv2.imshow("frame1", frame1)
            cv2.waitKey(10)
        else:
            cap2.set(cv2.CAP_PROP_POS_FRAMES, 0)
            break
        
def movie3():
    print("movie3 start")
    while True:
        ret1, frame1 = cap3.read()
        if ret1:
            frame1 = cv2.resize(frame1, (1920, 1080))
            cv2.imshow("frame1", frame1)
            cv2.waitKey(10)
        else:
            cap3.set(cv2.CAP_PROP_POS_FRAMES, 0)
            break

def movie4():
    print("movie4 start")
    while True:
        ret1, frame1 = cap4.read()
        if ret1:
            frame1 = cv2.resize(frame1, (1920, 1080))
            cv2.imshow("frame1", frame1)
            cv2.waitKey(10)
        else:
            cap4.set(cv2.CAP_PROP_POS_FRAMES, 0)
            break

def movie5():
    print("movie5 start")
    while True:
        ret1, frame1 = cap5.read()
        if ret1:
            frame1 = cv2.resize(frame1, (1920, 1080))
            cv2.imshow("frame1", frame1)
            cv2.waitKey(10)
        else:
            cap5.set(cv2.CAP_PROP_POS_FRAMES, 0)
            break

def movie6():
    print("movie6 start")
    while True:
        ret1, frame1 = cap6.read()
        if ret1:
            frame1 = cv2.resize(frame1, (1920, 1080))
            cv2.imshow("frame1", frame1)
            cv2.waitKey(10)
        else:
            cap6.set(cv2.CAP_PROP_POS_FRAMES, 0)
            break

    

def start_movie(face_num):
    #inputNum = b
    while True:       
        try:
            func(face_num)
        except TimeoutError:
            callback()

if __name__ == "__main__":
    face_num = 1
    start_movie(face_num)
