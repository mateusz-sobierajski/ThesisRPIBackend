import serial
import time

#from RPICommunication.ArduinoCOM.JSONIFYtemp import get_temp
#from RPICommunication.MariaDB.INSERT_handler import insert_aht10


def listener():
	ser = serial.Serial('/dev/ttyUSB0', 1200)
	ser.reset_input_buffer()
	ii = 0
	while True:
		if ser.inWaiting() > 0:
			ii += 1
			line = ser.readline().decode('utf-8').rstrip()
			splitinfo = line.split(",")
			print(line)
			print(splitinfo)
			#print(splitinfo[1])
			#print(splitinfo[3])
			#for a in splitinfo:
			#	print(a)
			print ("Init ii counter: ")
			print (ii)
			if ii > 4:
				#insert_aht10(splitinfo)
				print(splitinfo[1])
			for i in range(len(splitinfo)):
				print(i)
				type(i)
				print(splitinfo[i])
				type(splitinfo[i])
			#get_temp()


def listener2():
	while True:
		print("listener2")
		time.sleep(2)

