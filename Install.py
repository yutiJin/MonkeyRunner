from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice

def Install(device):
	# Install 
	apkFilePath = "E:/sdmp-v0.1.476-debug.apk";
	device.installPackage(apkFilePath);

	# Launch app
	package = "cn.edu.zstu.sdmp";
	activity = "cn.edu.zstu.sdmp.main.view.SplashActivity";
	runComponent = package + "/" + activity;
	print("Start smartTree")
	device.startActivity(component=runComponent);
	# wait
	print("Wait 3s")
	MonkeyRunner.sleep(3);

def Uninstall(device):
	try:
		package = "cn.edu.zstu.sdmp";
		device.removePackage(package)
	except:
		print("Package uninstall failed!")