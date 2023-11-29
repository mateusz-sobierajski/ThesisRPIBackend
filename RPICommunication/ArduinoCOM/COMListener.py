import serial
import time


# ser = serial.Serial('/dev/ttyACM0',9600)
def listener():
	ser = serial.Serial('/dev/ttyUSB0', 1200)
	ser.reset_input_buffer()
	while True:
		if ser.inWaiting() > 0:
			#print(ser.readline())
			line = ser.readline().decode('utf-8').rstrip()
			splitinfo = line.split(",")
			print(line)
			print(splitinfo)
			#print(splitinfo[1])
			#print(splitinfo[3])

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

