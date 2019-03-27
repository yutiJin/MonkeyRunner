#!/usr/bin/python
# coding: utf-8

from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By

# Student
def Student_In(device, edevice):
	# Login?
	# Connect device
	if edevice.exists(By.id('id/room_main_terminal_unlock')):
		print('Has Logined')
	else:
		print('Not Login, Start Logining...')
		# Login
		MonkeyRunner.sleep(0.5)
		edevice.touch(By.id('id/login_role_student_layout'), MonkeyDevice.DOWN_AND_UP)
		print('press the student button')
		MonkeyRunner.sleep(0.5)
		# press a button clean the input
		text = (edevice.getText(By.id('id/main_login_account_text'))).encode('utf-8')
		print(text)
		while (text != ''):
			edevice.touch(By.id('id/main_login_icon_clean'), MonkeyDevice.DOWN_AND_UP)
			MonkeyRunner.sleep(0.5)
			text = (edevice.getText(By.id('id/main_login_account_text'))).encode('utf-8')
		print('text is null')
		# input the phone number
		edevice.type(By.id('id/main_login_account_text'), '17816118870')
		MonkeyRunner.sleep(0.5)

		# Hide the Keyboard  two-way
		# edevice.touch(By.id('id/main_login_code_send'), MonkeyDevice.DOWN_AND_UP)
		# MonkeyRunner.sleep(0.50.50.5);
		# device = MonkeyRunner.waitForConnection()
		device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(1)

		# press the login button
		edevice.touch(By.id('id/main_login_submit_btn'), MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(1)
		print('Has Logined')

# Teacher
def Teacher_In(device, edevice):
	if edevice.exists(By.id('id/room_main_terminal_unlock')):
		print('Has Logined')
	else:
		print('Not Login, Start Logining...')
		edevice.touch(By.id('id/login_role_teacher_layout'), MonkeyDevice.DOWN_AND_UP)
		text = (edevice.getText(By.id('id/main_login_account_text'))).encode('utf-8')
		print(text)
		while (text != ''):
			edevice.touch(By.id('id/main_login_icon_clean'), MonkeyDevice.DOWN_AND_UP)
			MonkeyRunner.sleep(0.5)
			text = (edevice.getText(By.id('id/main_login_account_text'))).encode('utf-8')
		print('text is null')
		edevice.type(By.id('id/main_login_account_text'), '17816118870')
		MonkeyRunner.sleep(0.5)
		device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(1)
		edevice.touch(By.id('id/main_login_submit_btn'), MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(1)
		print('Has Logined')

# RoomManager
def RoomManager_In(device, edevice):
	if edevice.exists(By.id('id/room_main_terminal_unlock')):
		print('Has Logined')
	else:
		print('Not Login, Start Logining...')
		edevice.touch(By.id('id/login_role_room_manager_layout'), MonkeyDevice.DOWN_AND_UP)
		text = (edevice.getText(By.id('id/main_login_account_text'))).encode('utf-8')
		print(text)
		while (text != ''):
			edevice.touch(By.id('id/main_login_icon_clean'), MonkeyDevice.DOWN_AND_UP)
			MonkeyRunner.sleep(0.5)
			text = (edevice.getText(By.id('id/main_login_account_text'))).encode('utf-8')
		print('text is null')
		edevice.type(By.id('id/main_login_account_text'), '17816118870')
		MonkeyRunner.sleep(0.5)
		device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(1)
		edevice.touch(By.id('id/main_login_submit_btn'), MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(1)
		print('Has Logined')

# Worker
def Worker_In(device, edevice):
	if edevice.exists(By.id('id/room_main_terminal_unlock')):
		print('Has Logined')
	else:
		print('Not Login, Start Logining...')
		edevice.touch(By.id('id/login_role_worker_layout'), MonkeyDevice.DOWN_AND_UP)
		text = (edevice.getText(By.id('id/main_login_account_text'))).encode('utf-8')
		print(text)
		while (text != ''):
			edevice.touch(By.id('id/main_login_icon_clean'), MonkeyDevice.DOWN_AND_UP)
			MonkeyRunner.sleep(0.5)
			text = (edevice.getText(By.id('id/main_login_account_text'))).encode('utf-8')
		print('text is null')
		edevice.type(By.id('id/main_login_account_text'), '17816118870')
		MonkeyRunner.sleep(0.5)
		device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(1)
		edevice.touch(By.id('id/main_login_submit_btn'), MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(1)
		print('Has Logined')	  


# Parent
def Parent_In(device, edevice):
	if edevice.exists(By.id('id/room_main_terminal_unlock')):
		print('Has Logined')
	else:
		print('Not Login, Start Logining...')
		edevice.touch(By.id('id/login_role_parent_layout'), MonkeyDevice.DOWN_AND_UP)
		text = (edevice.getText(By.id('id/main_login_account_text'))).encode('utf-8')
		print(text)
		while (text != ''):
			edevice.touch(By.id('id/main_login_icon_clean'), MonkeyDevice.DOWN_AND_UP)
			MonkeyRunner.sleep(0.5)
			text = (edevice.getText(By.id('id/main_login_account_text'))).encode('utf-8')
		print('text is null')
		edevice.type(By.id('id/main_login_account_text'), '13588301118')
		MonkeyRunner.sleep(0.5)
		device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(1)
		edevice.touch(By.id('id/main_login_submit_btn'), MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(1)
		print('Has Logined')