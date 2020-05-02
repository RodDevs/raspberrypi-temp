# raspberrypi-temp
Raspberry Pi - Time, Date, CPU Temperature and Public IP display on LCD 20x4


Make sure to have all python and raspberry pi dependencies to work with LCDs, here is a good guide on how to install packages needed.

https://www.abelectronics.co.uk/kb/article/1/i2c--smbus-and-raspbian-linux

Installing I2C Tools and Python Libraries

sudo apt-get update
sudo apt-get install python-smbus python3-smbus python-dev python3-dev i2c-tools

You can test if i2ctools is working by listing all of the I2C devices connected to your Raspberry Pi.

sudo i2cdetect -y 1


i2cdetect will display a grid of numbers with the addresses of any i2c devices shown within the grid.  In the following example two I2C devices are show on addresses 0x68 and 0x69.

 0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- 68 69 -- -- -- -- -- --
70: -- -- -- -- -- -- -- --

Setting the I2C Bus Speed

The I2C bus supports several bus speeds, typically 100KHz, 400KHz, 1MHz, 3.4MHz and 5.0MHz.  You can set the bus speed by editing /boot/config.txt.  Open the file with nano using the command:

sudo nano /boot/config.txt

Add the following text to the bottom of the file; The number is the frequency of the I2C bus in hertz:

dtparam=i2c_baudrate=400000

Save your changes, exit the nano editor and reboot

sudo reboot

---------------------------------

SETUP AND RUN:

- Upload all three files into same directory - I have made one called 'lcd'
- run temp.py file within directory as: 

sudo python3 temp.py
