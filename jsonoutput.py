from Adafruit_BME280 import *
import calendar
import time
import socket

sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

degrees = sensor.read_temperature()
pascals = sensor.read_pressure()
hectopascals = pascals / 100
humidity = sensor.read_humidity()

timestamp = calendar.timegm(time.gmtime())

print '{{ timestamp: {3}, device: {4}, temp: {0:0.3f}, pressure: {1:0.2f}, humidity: {2:0.2f} }}'.format(degrees, hectopascals, humidity, timestamp, socket.gethostname())
