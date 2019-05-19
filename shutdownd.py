#!/usr/bin/python3 
# coding:utf-8 
import time
import RPi.GPIO as GPIO
import os
import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)

pinnumber=23
GPIO.setmode(GPIO.BCM)

#GPIO23pinを入力モードとし、pull up設定とします 
GPIO.setup(pinnumber,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    GPIO.wait_for_edge(pinnumber, GPIO.FALLING)
    sw_counter = 0

    while True:
        sw_status = GPIO.input(pinnumber)
        if sw_status == 0:
            sw_counter = sw_counter + 1
            if sw_counter >= 50:
                # print("長押し検知！")
                os.system("sudo shutdown -h now")
                break
        else:
            # print("短押し検知")
            break

        time.sleep(0.01)

    # print(sw_counter)
