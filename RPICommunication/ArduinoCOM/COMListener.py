import serial
import time


# ser = serial.Serial('/dev/ttyACM0',9600)
def listener():
	ser = serial.Serial('/dev/ttyACM0', 1200)
	s = [0, 1]
	while True:
		read_serial = ser.readline()
		print(ser.readline())
		s[0] = str(int(ser.readline(), 16))
		print(s[0])
		print(read_serial)


def listener2():
	while True:
		print("listener2")
		time.sleep(2)

