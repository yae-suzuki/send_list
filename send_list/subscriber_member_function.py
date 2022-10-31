import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from testpy_mes.msg import GpioMsg
from openpy.Shuwa import shuwa

import time
import datetime

#from test_py.test_py import test
#class Subscriber(Node, pca9685_test, shuwa):
class Subscriber(Node, shuwa):
	SELFNODE = 'subscriber'
	def __init__(self):
		# ノードの初期化
		super().__init__('subscriber')
		# subscriptionインスタンスを生成
		self.subscriber = self.create_subscription(GpioMsg, 'topic', self.callback, 10)
		# 時刻を表示
		dt = datetime.datetime.now()
		print(dt)
		# コンソールに表示
		self.get_logger().info("subscriber initializing...")
		# 時刻を表示
		dt = datetime.datetime.now()
		print(dt)
		# コンソールに表示
		self.get_logger().info("subscriber do... ")
	def __del__(self):
		"""
		デストラクタ
		"""
		# 時刻を表示
		dt2 = datetime.datetime.now()
		print(dt2)
		# コンソールに表示
		self.get_logger().info("subscriber done.")

	def callback(self, msg):
		self.count += 1
		self.get_logger().info("Subscriber [%s]" % (self.count))
		# 時刻を表示
		self.dt3 = datetime.datetime.now()
		print(self.dt3)
		#取得したメッセージを表示		
		print("Get message:", msg.txt)
		#サーボを制御
		if msg.txt == 'a':
			self.a()
		elif msg.txt == 'i':
			self.i()
		elif msg.txt == 'u':
			self.u()
		elif msg.txt == 'e':
			self.e()
		elif msg.txt == 'o':
			self.o()
		elif msg.txt == 'test1':
			self.test1()
		elif msg.txt == 'test2':
			self.test2()
		elif msg.txt == 'test3':
			self.test3()
		elif msg.txt == 'test4':
			self.test4()
		elif msg.txt == 'test5':
			self.test5()
		elif msg.txt == 'test6':
			f=open('timedata.txt',w)
			f.write('[time:',self.dt3,', count:',self.count,']:\n')
			f.close()
		else:
			print("No action found")
			
def main(args=None):
	try:
		rclpy.init(args=args)  # RCLの初期化
		subscriber = Subscriber()  # Nodeのインスタンス化
		rclpy.spin(subscriber)  # subscriberのループ
		
	except KeyboardInterrupt:
		pass	#ctl+C(KeyboardInterrupt) node finish
	finally:
		subscriber.destroy_node()  # ノードの破壊
		rclpy.shutdown()  # ROSのシャットダウン
	
if __name__ == '__main__':
	main()

