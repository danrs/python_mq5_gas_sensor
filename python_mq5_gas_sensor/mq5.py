# Copyright (c) 2016 Daniel Smith
# Author: Daniel Smith
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import re
import Adafruit_BBIO.ADC as ADC
ADC.setup()

class mq5:
    # Default pin
    def __init__(self, pin="AIN0", voltage=3.3):
        """
        The Adafruit_BBIO library will accept pins as numbers (eg. "P9_39")
        or pin names (eg "AIN0"). The following analog pins are available:
        Number | Name | Notes
        ---------------------------------------------
        P9_39  | AIN0 | J3 Connector on Grove BB Cape
        P9_40  | AIN1 | J3 Connector on Grove BB Cape (NC to MQ5)
        P9_37  | AIN2 | J7 Connector on Grove BB Cape
        P9_38  | AIN3 | J7 Connector on Grove BB Cape (NC to MQ5)
        P9_33  | AIN4 |
        P9_36  | AIN5 |
        P9_35  | AIN6 |
        
        Note that the grove analog pins used 3V3, but the
        analog header pins VDD_ADC (P9_32) and GNDA_ADC (P9_34)
        use 1.8V.
        """
        
        pin_number_re = re.compile('P9_([34][0-9])', re.IGNORECASE)
        pin_name_re = re.compile('AIN([0-6])', re.IGNORECASE)
        if not re.match(pin_name_re,pin):
            match = re.match(pin_number_re,pin)
            if match is None:
                raise ValueError('pin must be valid analog input pin like AIN0 or GPIO9_39')
            elif int(match.group(1)) > 40 or int(match.group(1)) < 33:
                raise ValueError('pin chosen must be an analog input (GPIO9_33-GPIO9_40)')
        self.pin = pin
        self.voltage = voltage # voltage supplied to the sensor

    def read(self):
        return ADC.read(self.pin)
    def read_raw(self):
        return ADC.read_raw(self.pin)
    def sensitivity_adjust(self,value):
        """
        Assists sensitivity adjustment by continually reading the sensor until the specified value is reached.
        To use, place the sensor in a known concentration of gas and then run this function with value
        set to the desired ADC output for that concentration. Then, adjust the potentiometer until
        the value is reached.
        """
        print 'Adjust the potentiometer until the desired value is reached'
        while self.read_raw() != value:
            pass
        print 'STOP NOW, value reached'

