class Car(object):
	def __init__(self,model,color,company,speedlimit):
		self.model=model
		self.color=color
		self.company=company
		self.speedlimit=speedlimit
	def start(self):
		print("started")
	def stop(self):
		print("stopped")
	def changegear(self,geartype):
		print("gear changed")
	def accelerate(self):
		print("accelerating")
bmw=Car("bmw","white","bmw", 80)
print(bmw.start())


	
		