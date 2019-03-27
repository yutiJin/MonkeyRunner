from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

def OpenClose(device):
	package = "cn.edu.zstu.sdmp";
	activity = "cn.edu.zstu.sdmp.main.view.SplashActivity";
	runComponent = package + "/" + activity;
	for i in range(1,4):
		device.press("KEYCODE_BACK", MonkeyDevice.DOWN_AND_UP);
		MonkeyRunner.sleep(3);
		device.startActivity(component=runComponent);
		MonkeyRunner.sleep(3);