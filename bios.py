import os
import winsound,time
os.system("cls")
frequency=1000
delay=5000
class BIOS:
	def __init__(self,CPU,RAM):
		self.CPU=CPU
		self.RAM=RAM

	def run(self):
		for i in range(2):
			freq=800
			delay=1500
			winsound.Beep(freq,delay)
			time.sleep(0.5)
		self.CPU.run()
		self.RAM.run()
		time.sleep(5)

	class CPU:
		def __init__(self,name,speed):
			self.name=name
			self.speed=speed
		def show(self):
			time.sleep(100//CPU.speed)
			print(f"CPU: {self.name}")


		def check(self):
			if self.speed > 1000:
				winsound.Beep(frequency,delay)
				quit()
			elif self.speed < 50:
				time.sleep(100//CPU.speed)
				print("CPU TEST: SLOW")

				time.sleep(10)
				quit()
			else:
				time.sleep(100//CPU.speed)
				print("CPU TEST: OK")


		def run(self):
			self.show()
			self.check()

	class RAM:
		def __init__(self,amount):
			self.amount=amount

		def show(self):
			time.sleep(100//CPU.speed)
			print(f"RAM: {self.amount} MB")


		def check(self):
			if self.amount < 128:
				time.sleep(100//CPU.speed)
				print("RAM TEST: NOT ENOUGH")
				time.sleep(5)
				quit()
			else:
				time.sleep(100//CPU.speed)
				print("RAM TEST: OK")

		def run(self):
			self.show()
			self.check()


CPU = BIOS.CPU("ibCPU 50Hz",50)
RAM = BIOS.RAM(128)
BIOS=BIOS(CPU,RAM)
BIOS.run()
import bload
	
