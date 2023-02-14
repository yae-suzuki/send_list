import cv2
from cv_bridge import CvBridge

"""
def movie0(cap0):
    print("movie0 start")
    #cap0 = cv2.VideoCapture(r"blink.mp4")
    while True:
        ret1, frame1 = cap0.read()
        if ret1:
            frame1 = cv2.resize(frame1, (1920, 1080))
            cv2.imshow("frame1", frame1)
            cv2.waitKey(10)
        else:
            cap0.set(cv2.CAP_PROP_POS_FRAMES, 0)
            break
        
if __name__ == "__main__":
    cap0 =  cv2.VideoCapture(r"blink.mp4")
    movie0(cap0)
"""
def movie0(self):
    print("movie0___start")
    #change cv2 to cvbridge
    br = CvBridge()
    cap0 =  cv2.VideoCapture(r"/home/ubuntu/ros2_ws/src/send_list/send_list/face_movie/blink.mp4")
    while True:
        print("a")
        ret1, frame1 = cap0.read()
        if ret1:
            print("b")
            frame1 = cv2.resize(frame1, (1920, 1080))
            self.movie1_br = br.cv2_to_imgmsg(frame1,'bgr8') #cv2 to cvbridge //display rqt
            print("c")
            #publisher.publish(movie1_br) #send pub
            return self.movie1_br
            #publisher.publish(movie1_br) #send pub 
            cv2.waitKey(10)
            self.get_logger().info("please movie start")
        else:
            cap0.set(cv2.CAP_PROP_POS_FRAMES, 0)
            break
    
