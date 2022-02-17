import os
import time
import datetime

print(" WideTech [Version 1.0]")
print("(c) WideTech corporation. All rights reserved.")

while True:
  now = datetime.datetime.now()
  CMD = input("C:\ Users\ User>")
  if CMD == "time".lower():
    print("Current date and time is:")
    print(now.strftime("%y-%m-%d %H:%M:%S"))

  elif CMD == "help":
    time.sleep(3)
    print("help = see all commands")  
    time.sleep(0.3)
    print("time = to see the time")
    time.sleep(0.3)
    print("rename = rename a file")
    time.sleep(0.3)
    print("ver = to know all information about your computer")

  elif CMD == "ver".lower():
    print("getting windows information..:")
    time.sleep(2)  
    print("Device name: LAPTOP-50JCSL66")
    time.sleep(0.3)
    print("processor: 11th Gen Intel(R) Core(TM) i3-1115G4 @ 3.00GHz   3.00 GHz")
    time.sleep(0.3)
    print("installed RAM: 4.00 GB (3.65 GB usable)")
    time.sleep(0.3)
    print("Device ID: 2A623F54-5891-4E56-9B0F-C6A54E3F9345")
    time.sleep(0.3)
    print("product ID: 00356-02405-84072-AAOEM")
    time.sleep(0.3)
    print("system type: 64-bit operating system, x64-based processor")
    time.sleep(0.3)
    print("Pen and touch: No pen or touch input is available for this display")
    time.sleep(0.1)
    print("-----------------------------------------------------------------------")

  elif CMD == "rename".lower():
    input("Enter file name: ")
    input("New file name: ")
    print("File name changed")  

  elif CMD == "":
    print("please write a command")  
    continue
  
  elif CMD == "Stuff":
    continue
  else:
    print("Command undetected")
    continue