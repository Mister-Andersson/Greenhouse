import pycom
import time
from machine import ADC, I2C
import BME280

adc = ADC(0)
i2c = I2C(0, I2C.MASTER, baudrate=100000)
adcpin = adc.channel(pin='P13', attn = ADC.ATTN_11DB)   # create an analog pin on P13, range 0..3.3V
val = adcpin()                    # read an analog value

while True:
  bme = BME280.BME280(i2c=i2c)
  temp = bme.temperature
  hum = bme.humidity
  pres = bme.pressure
  # uncomment for temperature in Fahrenheit
  #temp = (bme.read_temperature()/100) * (9/5) + 32
  #temp = str(round(temp, 2)) + 'F'
  print('--------------------')
  print('Temperature: ', temp)
  print('Humidity: ', hum)
  print('Pressure: ', pres)
  print('Soil: ', adcpin())
  time.sleep(5)


# pycom.heartbeat(False)
# while True:
#     pycom.rgbled(0xFF0000)  # Red
#     time.sleep(1)
#     pycom.rgbled(0x00FF00)  # Green
#     time.sleep(1)
#     pycom.rgbled(0x0000FF)  # Blue
#     time.sleep(1)