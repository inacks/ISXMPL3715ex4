# Example Reference Code: ISXMPL3715ex4

## Objective
Demonstrate how to write a program in Python for the IS3715 I2C DMX Controller on a Raspberry Pi. 

## Required Material
- Kappa3715Rasp Board (INACKS evaluation board featuring the IS3715)
- Raspberry Pi B Board
- DMX-compatible light fixture

## Setup
Connect the Kappa371Rasp to the Raspberry Pi, and attach a DMX light to the Kappa371Rasp.  
Run the command to verify that the IS3715 is detected:  

`sudo i2cdetect -y 1`

Finally, execute the example with sudo.

## How it works
The Python code continuously increments the `DMX_Values[1]` by 1.  
This value is written to register address 1 of the IS3715, which causes the DMX channel value to increase continuously.

## Other
Download the example code at: https://inacks.com/is3715  
Find Kappa3715Rasp product information at: https://inacks.com/kappa3715rasp

## Example of chip detection on the I2C-Serial interface
To verify that the Raspberry Pi is properly connected to the IS3715, scan the I2C-Serial interface for connected devices.  
The IS3715 should appear at address 21 (0x15)  

Run:

`sudo i2cdetect -y 1`

The command output should show a detected device at 21 (0x15):

```
pi@raspberrypi:~ $ sudo i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- 15 -- -- -- -- -- -- -- -- -- --
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --

