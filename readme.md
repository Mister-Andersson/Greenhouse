# Building a Greenhouse monitoring sensor

###### tags: `MicroPython` `IoT` `LoRaWAN` `TTN` `Home Assistant`
#### Author: Jonas Andersson
#### Course: Applied Internet of Things (Professional Education), 4DV119, Linneus University, 2022
#### Approximate time consumption to finish with tutorial: 3-5 hours

---
**Table of Contents**

- [Project Overview](#project-overview)
- [Project Objective](#project-objective)
- [Material](#material)
- [Environment Setup](#environment-setup)
- [Putting everything together](#putting-everything-together)

### Project Overview
This tutorial will explain how to build and program the behavior of a device with sensors measuring air temperature, humidity and soil moisture.
I will explain how I built the device and what tools I used.
This is a project in the course, Applied Internet of Things (4DV119) at Linnaeus University of Kalmar and Växjö.

### Project Objectives
I chose this project to learn more about MicroPython. I have tested it before but never really done anything useful with it. I was also interested in using LoRaWAN as a communication protocol and see if I could show the data in my Home Assistant installation at home.
I decided to make a Greenhouse sensor for surveillance of the temperature and the moisture in the soil. If it gets to hot in the summer, we will have to open the doors to evacuate some of the heat and if the soil gets to dry, we need to water the plants (of course). Knowing the status by looking in a mobile app or getting a notification when some limit values are reached is appealing for me and the missus.


### Material

>| Component |Cost |Store | Function         |
>| --------- | ---- | ------------------------- | --------------------------------------|
>| Pycom Lopy4 | 38€ | https://www.digikey.se/ | Microcontroller with MicroPython environment|
>| Pycom Expansion board | 17€ | https://www.digikey.se/ | For connecting things |
>| Mini breadboard | 3€ | https://www.electrokit.com/ | For connecting more things |
>| BME280 | 7€ | https://www.amazon.se/ | Sensor with air-temperature, humidity and pressure sensor. Communicates over I2C-bus|
>| Capacitive Soil Moisture Sensor | 7€ | https://www.amazon.se/ | For measuring soil moisture. Analog signal. Needs calibrating! |
>| LiPo Battery 3,7V 2200mAh | 10€ | https://www.electrokit.com/ | Lithium battery with JST PH 2.0mm connector |
>| Old USB cable | ?€ | My drawer | For connecting the Soil Moisture Sensor |





### Environment setup

I used Microsoft Visual Studio Code as my code editor. It is free and available for Windows, Mac OS and Linux. You can download it here:
https://code.visualstudio.com/

PyMakr extension is good for managing the Pycom microcontroller. You can find it in VS Code Extension library. Just klick “Install”. 
For more information visit:
https://docs.pycom.io/gettingstarted/software/vscode/

I also used Pycom Firmeware updater to update the firmware of my LoPy4.
https://docs.pycom.io/updatefirmware/


### Putting everything together
*work in progress*

![How to connect](Pictures/Greenhouse_sketch.png)

### Platforms and infrastructure

As soon as I choose my project, I identified a challenge with connectivity. My Wi-Fi and Z-wave networks in the house was to far away. Mobile connectivity was a possibility, but the cost was too much for my taste. I have worked with LoRaWAN before, so the choice was easy.
I started with a Heltec LoRa enabled device with a small display. It looked nice and the display was a nice bonus. Unfortunately, the display broke after a week and when I was trying to disconnect the antenna the PCB connector broke! Back to the drawing board!
A Pycom LoPy4 with a nice Expansion board was my backup plan and it turn out to work really well.

I already had a Things Network gateway at home so that decision was simple. The Things Network Community Edition is a cloud service that allows you to manage LoRaWAN gateways and devices with their Things Stack service. They allow you to setup a temporary storage for your data and has several integrations with other platforms that is better suited for analysis and visualization. Setting up an integration with my Home Assistant at home was smooth and didn’t produce any problems.
A nice thought thou would be to have my own LoRaWAN network server at home. Perhaps even on the same Raspberry Pi that I run home assistant on!
I had a look at Chirpstack, and it looks really interesting. The problem is that I need more time to test this and the course at the university is time limited. I will come back to this another time. Everything else in my home automation is non-cloud and I intend to keep it like that so I will certainly come back to Chirpstack.



### The code
#### Calibrating the moisture sensor
I needed to calibrating the moisture sensor and I found this example:
https://stackoverflow.com/questions/64744090/how-to-convert-the-adc-output-of-the-capacitive-soil-humidity-sensor-v1-2-to-act

After experimenting a bit took the easy way and wrote down the values for the sensor in the air, not touching anything and the values with the sensor in a glass of water. In my case these values where 1230 and 3450. I use them in my code.

```
def remap(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)
```

And then I use it like this:
```
moist_float = remap(adcpin(), 1230, 3450, 100, 1)
```

#### The data model
I have worked a little bit with LoRaWAN devices before and I knew there wasn’t a standardized way of structuring the payload containing my sensor data. I have worked with devices manufactured by a Swedish company named Elsys and I knew they had a simple but solid payload encoding. And they published code examples on their web site! Nice!
https://www.elsys.se/en/elsys-payload/
I know this isn’t a hard thing to invent your self but if I would want to send the data to an other IoT-platform I know that Elsys-decoders are common. I also looked at CayenneLPP decoder but the Elsys had more options without having to split up the data in data channels.
https://docs.mydevices.com/docs/lorawan/cayenne-lpp

The data types I’m using in the code
```
type_temp = 0x01
type_rh = 0x02
type_pressure = 0x14
type_ext_temp1 = 0x0c
type_waterleak = 0x12
type_vdd = 0x07
```

I use struct to translate the data to the right 
https://docs.python.org/3/library/struct.html

```
s.send(struct.pack('!bHbBbLbB', type_temp, temp, type_rh, hum, type_pressure, pres, type_waterleak, moist))
```



### The physical network layer
*work in progress*


### Visualisation and user interface
*work in progress*


### Finalizing the design
*work in progress*


---