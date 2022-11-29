###肩　上げる　動作　プログラム
###使用ドライバ->L6470
### --- ステッピングモータ制御　--- ###

import wiringpi as wp
import RPi.GPIO as GPIO
import struct
import time
import sys

### --- 接続用パラメータ --- ###
SPI_CH = 0                            # SPI チャンネル
SPI_HZ = 1000000                        # SPI 通信速度

GPIO_Nbr = 25 # GPIO-NO
GPIO.setmode(GPIO.BCM)               # GPIO-NO 指定
GPIO.setup(GPIO_Nbr,GPIO.IN)       # GPIO INPUT 指定

### --------------------------- ###

# L6470初期設定
def INIT_L6470():
    spi_send([0x00,0x00,0x00,0xc0]) # Reset Device
    spi_send([0x05,0x00,0x05]) # Acceleration (12)
    spi_send([0x06,0x00,0x05]) # Deceleration (12)
    spi_send([0x07,0x00,0x03]) # Maximum speed (10)
    spi_send([0x08,0x00,0x01]) # Minimum speed (13)
    spi_send([0x15,0x03,0xFF]) # Full-step speed (10)
    spi_send([0x16,0x03]) # Micro Step (8)
    spi_send([0x09,0x50]) # Holding Kval (8)
    spi_send([0x0A,0x50]) # Constant Speed Kval (8)
    spi_send([0x0B,0x10]) # Acceleration starting Kval (8)
    spi_send([0x0C,0x10]) # Deceleration starting Kbal (8)


# SPI データ送信
def spi_send(spi_dat_ary):
    for itm in spi_dat_ary:
        tmp=struct.pack("B",itm)
        wp.wiringPiSPIDataRW(SPI_CH, tmp)


# データ加工・送信（共通）
def L6470_SEND_MOVE_CMD( cmd , DAT ):
    tmp=[]
    tmp.append(cmd)
    tmp.append((0x0F0000 & DAT) >> 16)
    tmp.append((0x00FF00 & DAT) >> 8)
    tmp.append((0x00FF & DAT))

    print(tmp)

    spi_send(tmp)


# JOG (SPEED指定 : 0---30000)
def L6470_run(run_spd):
    # 方向検出
    if (run_spd > 0):
        dir = 0x50 #Run(と回転方向)
        spd = run_spd
    else:
        dir = 0x51 #Run(と回転方向)
        spd = -1 * run_spd

    L6470_SEND_MOVE_CMD( dir , spd )

# 移動量指定移動
def L6470_POSITIONING(MV_DIST):
    # 方向検出
    if (MV_DIST > 0):
        dir = 0x40 #Move(と回転方向)
    else:
        dir = 0x41 #Move(と回転方向)
        MV_DIST = -1 * MV_DIST

    L6470_SEND_MOVE_CMD( dir , MV_DIST )

# 絶対位置指定移動
def L6470_MOVE_ABS(MV_DIST):
    dir = 0x60 #GoTo
    if (MV_DIST < 0):
        MV_DIST = -1 * MV_DIST

    L6470_SEND_MOVE_CMD( dir , MV_DIST )

# 停止
def L6470_STOP():
    spi_send([0xB0]) # SoftStop
    time.sleep(0.2)
    spi_send([0xA8]) # HardHiZ
    time.sleep(0.2)

# 原点設定
def L6470_SET_ORIGIN():
    spi_send([0xD8]) # Reset Position
    time.sleep(0.5)

# 原点移動
def L6470_MOVE_ORIGIN():
    spi_send([0x70]) # GoHome
    time.sleep(0.5)

# ドライバーBUSY解除待ち
def wait_until_not_busy():
    while True:
        time.sleep(0.2)
        mtr_sts = GPIO.input(GPIO_Nbr)
        #print(mtr_sts)

        if GPIO.input(GPIO_Nbr) == GPIO.HIGH :
            print("L6470 NOT BUSY")
            break
    time.sleep(0.2)

def move_ac_stepping_motor(ac_num):
    wp.wiringPiSPISetup(SPI_CH,SPI_HZ) # SPI 接続
    INIT_L6470() # L6470初期設定

    # 移動量指定回転
    print("動作角度入力->")
    #inputNum = input()
    #inputNum = int(inputNum)
    ac_num = int(ac_num)
    rng=1
    step = int(ac_num*1600/360)
    for i in range(rng):
        L6470_POSITIONING(step) # 移動量指定移動
        #wait_until_not_busy() # ドライバーBUSY解除待ち
    print("STEP ROTATION FINISHED")
    print("")

 

##################################
# メインプログラム
##################################

if __name__ == "__main__":
    wp.wiringPiSPISetup(SPI_CH,SPI_HZ) # SPI 接続

    INIT_L6470() # L6470初期設定
    

    """

    # 速度指定回転
    print("CONSTANT SPEED ROTATION START")

    spd_run = 8000
    L6470_run(spd_run)
    print("Speed : %d" % spd_run)
    time.sleep(5)

    L6470_STOP()
    print("STOP")

    time.sleep(1)

    spd_run = -8000
    L6470_run(spd_run)
    print("Speed : %d" % spd_run)
    time.sleep(5)

    L6470_STOP()
    print("STOP")

    time.sleep(1)

    print("CONSTANT SPEED ROTATION FINISHED")
    print("")

    """
    while True:
        # 移動量指定回転
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

    """
    # 絶対位置指定回転
    print("ABS ROTATION START")
    L6470_SET_ORIGIN() # 原点位置設定(0)
    rng=10
    step = int(3*(1600 / rng))
    for i in range(rng):
        L6470_MOVE_ABS((i+1)*step) # 絶対位置指定移動
        wait_until_not_busy() # ドライバーBUSY解除待ち

    L6470_MOVE_ORIGIN() # 原点位置移動
    print("ABS ROTATION FINISHED")
    """

    GPIO.cleanup()
