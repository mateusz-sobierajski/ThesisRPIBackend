import serial
import time

from RPICommunication.MariaDB.INSERT_handler import insert_aht10


# ser = serial.Serial('/dev/ttyACM0',9600)
def listener():
	ser = serial.Serial('/dev/ttyUSB0', 1200)
	ser.reset_input_buffer()
	i = 0
	while True:
		if ser.inWaiting() > 0:
			#print(ser.readline())
			i+=1
			line = ser.readline().decode('utf-8').rstrip()
			splitinfo = line.split(",")
			print(line)
			print(splitinfo)
			#print(splitinfo[1])
			#print(splitinfo[3])
			#for a in splitinfo:
			#	print(a)
			if i > 10:
				insert_aht10(splitinfo)
			print(splitinfo[1])
			for i in range(len(splitinfo)):
				print(i)
				type(i)
				print(splitinfo[i])
				type(splitinfo[i])

	#while True:
	#	read_serial = ser.readline()
	#	print(ser.readline())
		#s[0] = str(int(ser.readline(), 16))
		#print(s[0])
	#	print(read_serial)


def listener2():
	while True:
		print("listener2")
		time.sleep(2)

