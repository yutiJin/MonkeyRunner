from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
from com.android.monkeyrunner.easy import EasyMonkeyDevice, By

def Logout(device,edevice):
	while (not edevice.exists(By.id('id/main_tab_mine_icon'))):
		device.press('KEYCODE_BACK', MonkeyDevice.DOWN_AND_UP)
		MonkeyRunner.sleep(1)
	edevice.touch(By.id('id/main_tab_mine_icon'), MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.5)
	edevice.touch(By.id('id/menu_item_logout'), MonkeyDevice.DOWN_AND_UP)
	MonkeyRunner.sleep(0.5)
	print('Has Log out')