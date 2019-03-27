#!/usr/bin/python
# coding: utf-8

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By
import random, time

def MonkeyTest(device,edevice):
	num = 100
	dw = device.getProperty("display.width")
	dh = device.getProperty("display.height")
	# Device Screen
	print('[Device] Screen: %dx%d' % (int(dw), int(dh)))

	for i in range(1, num):
		nx = random.randint(1,int(dw))
		ny = random.randint(1,int(dh))
		device.touch(nx, ny, MonkeyDevice.DOWN_AND_UP)
		time.sleep(0.1)
		
		if i % 20 == 0:
			if edevice.exists(By.id('id/main_tab_mine_icon')):
				print("On the homepage")
			else:
				device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
				print("%d times" % i)
	print("over!!!")