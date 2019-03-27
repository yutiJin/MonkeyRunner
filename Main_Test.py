
#!/usr/bin/python
# coding: utf-8
import sys
sys.path.append('E:/Projects/MonkeyTest/smartTree')

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By
import Install, Monkey, Login, Logout, OpenClose

# Connect device
device = MonkeyRunner.waitForConnection()
if not device:
    print("Please connect a device to start!")
else:
    print("Device Connected successfully!")
   
# Install 
Install.Install(device)

# open and close
OpenClose.OpenClose(device)

# Easy Device   init easymonkeydevice object ,this is init method
print('init easymonkeydevice')
edevice = EasyMonkeyDevice(device)

# # Launch Interval
# MonkeyRunner.sleep(1)

# Login:student  monkeytest  Logout
Login.Student_In(device, edevice)
Monkey.MonkeyTest(device, edevice) 
Logout.Logout(device, edevice)
MonkeyRunner.sleep(1)

# Login:teacher
Login.Teacher_In(device, edevice)
Monkey.MonkeyTest(device, edevice)
Logout.Logout(device, edevice)
MonkeyRunner.sleep(1)

# Login:roommanager
Login.RoomManager_In(device, edevice)
Monkey.MonkeyTest(device, edevice)
Logout.Logout(device, edevice)
MonkeyRunner.sleep(1)

# Login:worker
Login.Worker_In(device, edevice)
Monkey.MonkeyTest(device, edevice)
Logout.Logout(device, edevice)
MonkeyRunner.sleep(1)

# Login:parent
Login.Parent_In(device, edevice)
Monkey.MonkeyTest(device, edevice)
Logout.Logout(device, edevice)
MonkeyRunner.sleep(1)

# uninstall
Install.Uninstall(device)