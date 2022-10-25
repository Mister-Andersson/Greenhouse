import pycom
from machine import ADC, I2C
from network import LoRa, Bluetooth
import socket
import time
import machine
import struct
import ubinascii
from lora_secrets import my_app_eui
from lora_secrets import my_app_key
import BME280
# from machine import WDT
# wdt = WDT(timeout=2000)  # enable it with a timeout of 2 seconds
# wdt.feed()

i2c = I2C(0, I2C.MASTER, baudrate=100000)               # initiate I2C bus
adc = ADC(0)
adcpin = adc.channel(pin='P13', attn = ADC.ATTN_11DB)   # create an analog pin on P13, range 0..3.3V
val = adcpin()                                          # read an analog value

type_temp = 0x01                                        # Elsys payload format https://www.elsys.se/en/elsys-payload/
type_rh = 0x02
type_pressure = 0x14
type_ext_temp1 = 0x0c
type_waterleak = 0x12
type_vdd = 0x07

bme = BME280.BME280(i2c=i2c)                            # define BME280 sensor
temp = bme.temperature
hum = bme.humidity
pres = bme.pressure

def remap(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

def init_lora():
  lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868, device_class=LoRa.CLASS_A)
  app_eui = ubinascii.unhexlify(my_app_eui)
  app_key = ubinascii.unhexlify(my_app_key)
  lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
  while not lora.has_joined():
    time.sleep(2)
    print('Not yet joined...')
  print('Joined LoRaWAN network!')
  print('DevEui:',ubinascii.hexlify(lora.mac()).upper().decode('utf-8'))


def send_data():
  s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)                                  # create a LoRa socket
  s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)                                      # set the LoRaWAN data rate
  s.setblocking(True)                                                                 # make the socket blocking
  s.send(struct.pack('!bHbBbLbB', type_temp, temp, type_rh, hum, type_pressure, pres, type_waterleak, moist))  # send data
  s.setblocking(False)                                                                # make the socket non-blocking
  data = s.recv(64)                                                                   # get any data received (if any...)
  if data:
    print(data)

init_lora()

while True:
  for i in range(90):
    bme = BME280.BME280(i2c=i2c)
    temp = bme.temperature//10
    hum = bme.humidity//1024
    pres = bme.pressure*10
    moist_float = remap(adcpin(), 1230, 3450, 100, 1)                                # calibrated air and water values
    moist = int(moist_float)
    # moist = adcpin()
    print('--------------------')
    print('Temperature: ', temp)
    print('Humidity: ', hum)
    print('Pressure: ', pres)
    print('Soil: ', moist)
    time.sleep(10)
  print('Sending data...')
  send_data()
  i=0
