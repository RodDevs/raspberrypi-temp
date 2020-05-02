import lcddriver
import urllib.request
from time import sleep, strftime
from gpiozero import CPUTemperature
from subprocess import *

cpu = CPUTemperature()
lcd = lcddriver.lcd()
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

def run_cmd(cmd):
        p = Popen(cmd, shell = True, stdout = PIPE)
        output = p.communicate()[0]
        return output

lcd.lcd_clear()

while True:
        lcd.lcd_display_string(strftime('TIME: ' '%I:%M:%S %p'), 1)
        lcd.lcd_display_string(strftime('%a, %b %d %Y'), 2)
        lcd.lcd_display_string("CPU Temp: %.2f" % cpu.temperature + chr(223) + "C", 3)
        lcd.lcd_display_string("IP:" + external_ip, 4)
        sleep(1)
