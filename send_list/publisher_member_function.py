from ast import Str
from socket import MsgFlag
import string
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_msgs.msg import String
from std_msgs.msg import Int64MultiArray 
from testpy_mes.msg import GpioMsg
import time
import datetime
from .make_list.get_move_csv import load_id_get_angle

class Publisher(Node):
	def __init__(self):
		# ノードの初期化
		super().__init__('publisher')
		# 時刻を表示
		dt = datetime.datetime.now()
		print(dt)
		# コンソールに表示
		self.get_logger().info("publisher initializing... ")
		# publisherインスタンスを生成
		set_ac_num = 39 #アクチュエータ数の設定
		#self.get_logger().info("acの数は",set_ac_num)
		self.publisher = self.create_publisher(GpioMsg,	'topic', set_ac_num) #create_publisher(char,name,num)
		# タイマーのインスタンスを生成（1秒ごとに発生）
		self.create_timer(1.0, self.callback)
		# カウンタをリセット
		self.count = 0
		# 時刻を表示
		dt = datetime.datetime.now()
		print(dt)
		# コンソールに表示
		self.get_logger().info("publisher do... ")
	
	def __del__(self):
		"""
		デストラクタ
		"""
		# 時刻を表示
		dt2 = datetime.datetime.now()
		print(dt2)
		# コンソールに表示
		self.get_logger().info("publisher done.")

	def callback(self):
		# 時刻を表示
		dt3 = datetime.datetime.now()
		print(dt3)
		# コンソールに表示
		self.get_logger().info("Publish [%s]" % (self.count))
		# メッセージの型を設定
		msg = GpioMsg()
		print("Please enter a word!")
		#入力された値を変数に代入
		#msg.txt = str(input())
		#入力された文字を動作角度に変換
		#msg = GpioMsg()
		#print(type(msg))
		
		#msg.ang, msg.ang1, msg.ang2, msg.ang3, msg.ang4, msg.ang5, msg.ang6, msg.ang7, msg.ang8, msg.ang9 =10,10,10,10,10,10,10,10,10,10
		msg.txt = load_id_get_angle()
		self.get_logger().info("msgにははいったね")
		#print(msg)
		#print(type(msg))
		

		if msg == "test6":
			num = 0
			print("入力されたのはtest6 -> chat code")
			while num < 16:
				msg = GpioMsg()
				msg= "test6"		
				self.publisher.publish(msg)
				dt = datetime.datetime.now()
				f=open('pubtimedata.txt','a')
				f.write('\n[time:')
				f.write(str(dt))
				f.write(', count:')
				f.write(str(num))
				f.write(']')
				f.close()
				num += 1
				time.sleep(1)
				
		#入力された値を送信
		else:
			self.publisher.publish(msg)
			print("msgに入っているもの->",msg)
			print("msg type",type(msg)) 
		# カウンタをインクリメント
		self.count += 1

"""
class PublisherTempleate(Node):

	def __init__(self):
		# ノードの初期化
		super().__init__('publisher')
		# 時刻を表示
		dt = datetime.datetime.now()
		print(dt)
		# コンソールに表示
		self.get_logger().info("publisher initializing... ")
		# publisherインスタンスを生成
		set_ac_num = 39 #アクチュエータ数の設定
		#self.get_logger().info("acの数は",set_ac_num)
		self.publisher = self.create_publisher(String, 	'topic', set_ac_num) #create_publisher(char,name,num)
		# タイマーのインスタンスを生成（1秒ごとに発生）
		self.create_timer(1.0, self.callback)
		# カウンタをリセット
		self.count = 0
		# 時刻を表示
		dt = datetime.datetime.now()
		print(dt)
		# コンソールに表示
		self.get_logger().info("publisher do... ")
	
	def __del__(self):
		
		#デストラクタ
		
		# 時刻を表示
		dt2 = datetime.datetime.now()
		print(dt2)
		# コンソールに表示
		self.get_logger().info("publisher done.")

	def callback(self):
		# 時刻を表示
		dt3 = datetime.datetime.now()
		print(dt3)
		# コンソールに表示
		self.get_logger().info("Publish [%s]" % (self.count))
		# メッセージの型を設定
		#msg = GpioMsg()
		print("Please enter a word!")
		#入力された値を変数に代入
		#msg.txt = str(input())
		#入力された文字を動作角度に変換
		msg = String()
		print(type(msg))
		msg = load_id_get_angle()
		self.get_logger().info("msgにははいったね")

		if msg == "test6":
			num = 0
			print("入力されたのはtest6 -> chat code")
			while num < 16:
				msg = GpioMsg()
				msg= "test6"		
				self.publisher.publish(msg)
				dt = datetime.datetime.now()
				f=open('pubtimedata.txt','a')
				f.write('\n[time:')
				f.write(str(dt))
				f.write(', count:')
				f.write(str(num))
				f.write(']')
				f.close()
				num += 1
				time.sleep(1)
				
		#入力された値を送信
		else:
			print(type(msg))
			self.publisher.publish(msg)
			print("msgに入っているもの->",msg)
			print("msg type",type(msg)) 
		# カウンタをインクリメント
		self.count += 1
"""

def main(args=None):
	try:
		rclpy.init(args=args)  # RCLの初期化
		publisher = Publisher()  # Nodeのインスタンス化
		rclpy.spin(publisher)  # publisherのループ
		
	except KeyboardInterrupt:
		pass
	finally:
		publisher.destroy_node()  # ノードの破壊
		rclpy.shutdown()  # ROSのシャットダウン
		
if __name__ == '__main__':                                                    
	main()                          


