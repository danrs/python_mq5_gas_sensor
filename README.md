python MQ5 Gas Sensor
=====================

Python library for using the MQ5 gas sensor on BeagleBone Black or BeagleBone Green. This sensor is just an analog input, so this library is pretty simple. However, the sensor is available as a Grove module, so this library will be useful to anyone experimenting with Grove sensors on the BeagleBone in Python. Any analog sensor will work in the same way as the mq5 gas sensor (and you could in fact use this library to read any analog input).

To install, download this library (git clone or click the download zip button) and place the unzipped contents somewhere handy on your BeagleBone Black or BeagleBone Green. Then cd to the directory of the library and execute the following command:

sudo python setup.py install

Ensure you have internet access so that you can install any required dependancies.

See usage examples in the examples folder.

MQ5 Gas sensors may be purchased as Grove modules from Seeed studio:
http://www.seeedstudio.com/depot/Grove-Gas-SensorMQ5-p-938.html

Written by Daniel Smith for UNSW Australia and LaTrobe University.
MIT license and all text above must be included in any redistribution
