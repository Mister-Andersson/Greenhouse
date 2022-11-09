# Building a Greenhouse monitoring sensor

###### tags: `MicroPython` `IoT` `LoRaWAN` `TTN` `Home assistant`
#### Author: Jonas Andersson
#### Course: Applied IoT, 4DV119 (Expertkompetens IoT), Linneus University, 2022

---
**Table of Contents**

- [ ] Project Overview
- [ ] Project Objective
- [ ] Material
- [ ] Environment Setup
- [ ] Title

[TOC]

### Project Overview
This tutorial will explain how to build and program the behavior of a device with sensors measuring air temperature, humidity and soil moisture.
I will explain how I built the device and what tools I used.
This is a project in the course 4DV119 (Expertkompetens IoT) at Linnaeus University of Kalmar and Växjö.

### Project Objectives
I chose this project to learn more about MicroPython. I have tested it before but never really done anything useful with it. I was also interested in using LoRaWAN as a communication protocol and see if I could show the data in my Home Assistant installation at home.
I decided to make a Greenhouse sensor for surveillance of the temperature and the moisture in the soil. If it gets to hot in the summer, we will have to open the doors to evacuate some of the heat and if the soil gets to dry, we need to water the plants (of course). Knowing the status by looking in a mobile app or getting a notification when some limit values are reached is appealing for me and the mrs.


### Material

>| Component | Function         |
>| --------- | ---------------- |
>| Pycom Lopy4 | Microcontroller with MicroPython environment|
>| Pycom Expansion board | For connecting things |
>| Mini breadboard | For connecting more things |
>| BME280 | Sensor with air-temperature, humidity and pressure sensor. Communicates over I2C-bus|
>| Capacitive Soil Moisture Sensor | For measuring soil moisture. Analog signal. Needs calibrating. |





### Environment setup

I used Microsoft Visual Studio Code as my code editor. It is free and available for Windows, Mac OS and Linux. You can download it here:
https://code.visualstudio.com/

PyMakr extension is good for managing the Pycom microcontroller. You can find it in VS Code Extension library. Just klick “Install”. 
For more information visit:
https://docs.pycom.io/gettingstarted/software/vscode/

I also used Pycom Firmeware updater to update the firmware of my LoPy4.
https://docs.pycom.io/updatefirmware/


### Putting everything together

### Platforms and infrastructure

### The code

### The physical network layer

### Visualisation and user interface

### Finalizing the design

---