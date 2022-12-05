import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from testpy_mes.msg import GpioMsg
#from openpy.Shuwa import shuwa
#from .video_timeout import start_movie
import cv2
from sensor_msgs.msg import Image
from timeout_decorator import timeout, TimeoutError
from .move_servo_motor.move_servo_motor import servo_start

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

        
    def __del__(self):
        """
        デストラクタ
        """
        #時刻を表示
        dt2 = datetime.datetime.now()
        print(dt2)
        #コンソールに表示
        self.get_logger().info("subscriber done.")
        
    def callback(self, msg):
        #時刻を表示      
        print("callback")
        self.dt3 = datetime.datetime.now()
        print(self.dt3)
        #取得したメッセージを表示、カッコ内任意の数字
        print("Get message:", msg.txt.split(",")[3])
        servo_start(int(msg.txt.split(",")[3]))
        
        
        
def main(args=None):
    try:
        
        rclpy.init(args=args)  #RCLの初期化
        subscriber = Subscriber()  #Nodeのインスタンス化
        rclpy.spin(subscriber)  #subscriberのループ        
        
    except KeyboardInterrupt:
        pass    #ctl+C(KeyboardInterrupt) node finish
    finally:
        subscriber.destroy_node()  #ノードの破壊
        rclpy.shutdown()  #ROSのシャットダウン

if __name__ == '__main__':
    main()        
        
        
        