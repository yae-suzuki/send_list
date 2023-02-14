import Adafruit_PCA9685
import time
import concurrent.futures
import threading

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50) #周波数50Hzに設定

def mae1():
    for i in range (310,357,1):
        pwm.set_pwm(11,0,i)
        time.sleep(0.01)
        
def mae2():
    for i in range (305,258,-1):
        pwm.set_pwm(15,0,i)
        time.sleep(0.01)
        
def ushiro1():
    for i in range (357,310,-1):
        pwm.set_pwm(11,0,i)
        time.sleep(0.01)
        
def ushiro2():
    for i in range (258,305,1):
        pwm.set_pwm(15,0,i)
        time.sleep(0.01)

def una():
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    executor.submit(mae1)
    executor.submit(mae2)
    time.sleep(1)
    executor.submit(ushiro1)
    executor.submit(ushiro2)
    time.sleep(1)

while True:
    una()



"""
import wiringpi as wp
import RPi.GPIO as GPIO
import struct
import time
import sys
import Adafruit_PCA9685

pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50) #周波数50Hzに設定


if __name__ == "__main__":
    wp.wiringPiSPISetup(SPI_CH,SPI_HZ) # SPI 接続

    INIT_L6470() # L6470初期設定
    
    while True:
        print("動作角度入力->")
        inputNum = input()
        inputNum = int(inputNum)
        rng=1
        step = int(inputNum*1600/360)
        for i in range(rng):
            L6470_POSITIONING(step) # 移動量指定移動
            #wait_until_not_busy() # ドライバーBUSY解除待ち
        print("STEP ROTATION FINISHED")
        print("")
        
        GPIO.cleanup()
        """