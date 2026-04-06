import os,time

class KERNEL:
	def __init__(self,version):
		self.version=version


if not __name__ == "__main__":
	kernel=KERNEL("0.0.1")

	os.system("cls")
	print("KERNEL RUNNING\nKERNEL VER:",kernel.version)
	time.sleep(5)
	os.system("cls")

	import osm