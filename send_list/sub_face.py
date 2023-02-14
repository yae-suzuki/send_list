import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from testpy_mes.msg import GpioMsg
#from openpy.Shuwa import shuwa
#from .video_timeout import start_movie
from .face_movie.movie0 import movie0
from cv_bridge import CvBridge
import cv2
from sensor_msgs.msg import Image
from timeout_decorator import timeout, TimeoutError

import time
import datetime

#from test_py.test_py import test
#class Subscriber(Node, pca9685_test, shuwa):
class Subscriber(Node):
    SELFNODE = 'subscriber'
    def __init__(self):
        #ノードの初期化
        super().__init__('subscriber')
        #subscriptionインスタンスを生成
        self.subscriber = self.create_subscription(GpioMsg, 'topic', self.callback, 10)
        #movie start pub instance create
        self.publisher = self.create_publisher(Image,'result',10)

        #時刻を表示
        dt = datetime.datetime.now()
        print(dt)
        #コンソールに表示
        self.get_logger().info("subscriber initializing...")
        #時刻を表示
        dt = datetime.datetime.now()
        print(dt)
        #コンソールに表示
        self.get_logger().info("subscriber do... ")

        #change cv2 to cvbridge
        self.br = CvBridge()
        
    def __del__(self):
        """
        デストラクタ
        """
        #時刻を表示
        dt2 = datetime.datetime.now()
        print(dt2)
        #コンソールに表示
        self.get_logger().info("subscriber done.")
        
    def movie_0(self):
       
        br = CvBridge()
        cap0 = cv2.VideoCapture(r"/home/ubuntu/ros2_ws/src/send_list/send_list/face_movie/blink_r3.mp4")
        face_num = "0"        
        while True:
            ret1, frame1 = cap0.read()
            if ret1:
                frame1 = cv2.resize(frame1, (1920, 1080))
                movie_br = self.br.cv2_to_imgmsg(frame1,'bgr8') #cv2 to cvbridge //display rqt
                self.publisher.publish(movie_br) #send pub 
                cv2.waitKey(10)
                self.get_logger().info("please movie start")
            else:
                cap0.set(cv2.CAP_PROP_POS_FRAMES, 0)
                break
        
        
        

    def callback(self, msg):

        #movie read
        #video1 = cv2.VideoCapture(r"/home/ros2_ws/src/send_list/send_list/blink.mp4")
        
        #時刻を表示      
        print("callback")
        self.dt3 = datetime.datetime.now()
        print(self.dt3)
        #取得したメッセージを表示、カッコ内任意の数字
        print("Get message:", msg.txt.split(",")[6])
        face_num = msg.txt.split(",")[6]
        if(face_num) == "0":            
            x = r"/home/ubuntu/ros2_ws/src/send_list/send_list/face_movie/blink_r3.mp4"
        elif(face_num) == "1":            
            x = r"/home/ubuntu/ros2_ws/src/send_list/send_list/face_movie/sadness_r3.mp4"
        elif(face_num) == "2":            
            x = r"/home/ubuntu/ros2_ws/src/send_list/send_list/face_movie/joy_r3.mp4"
  
        cap0 = cv2.VideoCapture(x)
        while True:
            ret1, frame1 = cap0.read()
            if ret1:
                frame1 = cv2.resize(frame1, (1920, 1080))
                movie_br = self.br.cv2_to_imgmsg(frame1,'bgr8') #cv2 to cvbridge //display rqt
                self.publisher.publish(movie_br) #send pub 
                cv2.waitKey(10)
                #self.get_logger().info("please movie start")
                face_num = msg.txt.split(",")[3]
            else:
                cap0.set(cv2.CAP_PROP_POS_FRAMES, 0)
                break
        
        """
        #取得したメッセージを表示、カッコ内任意の数字       
        print("Get message:", msg.txt.split(",")[3])
        face_num = msg.txt.split(",")[3]
        #old_msg = face_num
        
        br = CvBridge()
        #new_msg = face_num
        
        
        print(face_num)
        #face_num = input()
        print("input")
        print(face_num)
        if(face_num) == "30":            
            x = r"/home/ubuntu/ros2_ws/src/send_list/send_list/face_movie/surprise.mp4"
        elif(face_num) == "2":            
            x = r"/home/ubuntu/ros2_ws/src/send_list/send_list/face_movie/fear.mp4"
        elif(face_num) == "3":
            print("face_num=3")
            x = r"/home/ubuntu/ros2_ws/src/send_list/send_list/face_movie/disgust.mp4"
        elif(face_num) == "4":            
            x = r"/home/ubuntu/ros2_ws/src/send_list/send_list/face_movie/anger.mp4"
        elif(face_num) == "5":            
            x = r"/home/ubuntu/ros2_ws/src/send_list/send_list/face_movie/joy.mp4"
        elif(face_num) == "6":            
            x = r"/home/ubuntu/ros2_ws/src/send_list/send_list/face_movie/sadness.mp4"
        elif(face_num) == "0":            
            x = r"/home/ubuntu/ros2_ws/src/send_list/send_list/face_movie/blink.mp4"

        
        cap0 = cv2.VideoCapture(x)
        #msg.txt = "0,0,0,0,0,0,0,0,0,0,0,0"
        #face_num = "0"
        
        while True:
            ret1, frame1 = cap0.read()
            if ret1:
                frame1 = cv2.resize(frame1, (1920, 1080))
                movie_br = self.br.cv2_to_imgmsg(frame1,'bgr8') #cv2 to cvbridge //display rqt
                self.publisher.publish(movie_br) #send pub 
                cv2.waitKey(10)
                #self.get_logger().info("please movie start")
                face_num = msg.txt.split(",")[3]
            else:
                cap0.set(cv2.CAP_PROP_POS_FRAMES, 0)
                break
        """
        
        """
        while True:
            #face_num = msg.txt.split(",")[3]
            #old_msg = face_num
            print("Get message:", msg.txt.split(",")[3])
            print("while True")
            new_msg = msg.txt.split(",")[3]
            print("old_num=",old_msg)
            print("new_num=",new_msg)
            if(new_msg != old_msg):
                face_num = new_msg
                print("!=")
            elif(new_msg == old_msg):
                face_num = "0"
                print("==")
            
            
            
            #msg.txt.split(",")[3]
            br = CvBridge()
            print(face_num)
            #face_num = input()
            print("input")
            print(face_num)
            if(face_num) == "30":            
                x = r"/home/ubuntu/ros2_ws/src/send_list/send_list/face_movie/surprise.mp4"
            elif(face_num) == "2":            
                x = r"/home/ubuntu/ros2_ws/src/send_list/send_list/face_movie/fear.mp4"
            elif(face_num) == "3":
                print("face_num=3")
                x = r"/home/ubuntu/ros2_ws/src/send_list/send_list/face_movie/disgust.mp4"
            elif(face_num) == "4":            
                x = r"/home/ubuntu/ros2_ws/src/send_list/send_list/face_movie/anger.mp4"
            elif(face_num) == "5":            
                x = r"/home/ubuntu/ros2_ws/src/send_list/send_list/face_movie/joy.mp4"
            elif(face_num) == "6":            
                x = r"/home/ubuntu/ros2_ws/src/send_list/send_list/face_movie/sadness.mp4"
            elif(face_num) == "0":            
                x = r"/home/ubuntu/ros2_ws/src/send_list/send_list/face_movie/blink.mp4"

            
            cap0 = cv2.VideoCapture(x)
            #msg.txt = "0,0,0,0,0,0,0,0,0,0,0,0"
            #face_num = "0"
            
            while True:
                ret1, frame1 = cap0.read()
                if ret1:
                    frame1 = cv2.resize(frame1, (1920, 1080))
                    movie_br = self.br.cv2_to_imgmsg(frame1,'bgr8') #cv2 to cvbridge //display rqt
                    self.publisher.publish(movie_br) #send pub 
                    cv2.waitKey(10)
                    #self.get_logger().info("please movie start")
                    face_num = msg.txt.split(",")[3]
                else:
                    cap0.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    print("000000000")
                    #print(face_num)
                    print("Get message:", msg.txt.split(",")[3])
                    break
            print(type(face_num))
            #face_num = "0"
            
            """
                
               
"""
        def func_callback():
            print("movie0_start")
            br = CvBridge()
            #movie start
            cap0 = cv2.VideoCapture(r"/home/ubuntu/ros2_ws/src/send_list/send_list/face_movie/blink.mp4")
            while True:
                ret1, frame1 = cap0.read()
                if ret1:
                    frame1 = cv2.resize(frame1, (1920, 1080))
                    movie_br = self.br.cv2_to_imgmsg(frame1,'bgr8') #cv2 to cvbridge //display rqt
                    self.publisher.publish(movie_br) #send pub 
                    cv2.waitKey(10)
                    self.get_logger().info("please movie start")
                else:
                    cap0.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    break
"""
                    
"""
        def start_movie():
            while True:       
                try:
                    print("func")
                    func(face_num)
                except TimeoutError:
                    print("func_callback")
                    func_callback()                   
"""
                    
def main(args=None):
    try:
        
        rclpy.init(args=args)  #RCLの初期化
        subscriber = Subscriber()  #Nodeのインスタンス化
        #rclpy.spin(subscriber)  #subscriberのループ
        while True:
            subscriber.movie_0()
            rclpy.spin_once(subscriber)  #subscriberのループ
        
        
    except KeyboardInterrupt:
        pass    #ctl+C(KeyboardInterrupt) node finish
    finally:
        subscriber.destroy_node()  #ノードの破壊
        rclpy.shutdown()  #ROSのシャットダウン

if __name__ == '__main__':
    main()
