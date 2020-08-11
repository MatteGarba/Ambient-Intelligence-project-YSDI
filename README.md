# Ambient Intelligence System project

Details can be found:
 - on the project website: https://ami-2018.github.io/YSDI/
 - on YouTube: https://www.youtube.com/watch?v=eV60kDTFtd4
 - on the original repository: https://github.com/AmI-2018/YSDI-code
 
 (The current repository is only a fork of the original one for a better visualization on my GitHub account, 
 but still it is identical to the original and contains the same files, exception made for this README containing this message)



# How to navigate this repository

There are 3 main folders:

  - Multithreading
  - UserClient
  - ArduinoCode

##### Multithreading

It's the folder containing the code and the modules for the raspberry computational node.
That Multithreading SW will host the web user interface, manage sensor data and some sensors and actuators as luminosity sensor, smart plugs, hue lights.


##### UserPC_App
Contains the code of the SW running on the user's PC and monitoring their web activities and the microphone.


##### Arduino_codes
It contains the programs for the arduino boards controlling the pressure sensor (the load-cell on the desk) and the variable resistance sensor (pressure sensor on the chair ).
