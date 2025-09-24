"""
This example continuously increments the value of DMX Channel 1.
When the value reaches 255, it rolls over to 0. 

This example uses the Kappa3715 Evaluation Board featuring the IS3715.

Verify that your Raspberry Pi can see the IS3715 on the I2C Serial Interface:
$ sudo i2cdetect -y 1
The device should appear at address 0x15.

Run this script with sudo:
$ sudo python ISXMPL3715ex4-IS3715_RaspberryPi_Example.py

For more information, visit www.inacks.com
"""

from smbus2 import SMBus, i2c_msg
import time

I2C_BUS = 1  # Use 1 for most Raspberry Pi models
I2C_DEVICE_ADDRESS = 21  # I2C device address of the IS3715

# IS3715 Memory Map Addresses:
CHIP_ID = 513
CHIP_REV = 514

def write_register(start_register, data_bytes):
    """
    Write a block of data starting at a 16-bit register address.
    
    :param start_register: The 16-bit register address to start writing to.
    :param data_bytes: A list of bytes to write.
    """
    high_addr = (start_register >> 8) & 0xFF # High byte of 16-bit address
    low_addr = start_register & 0xFF # Low byte of 16-bit address
    with SMBus(I2C_BUS) as bus:
        # Send 16-bit address followed by data bytes
        msg = i2c_msg.write(I2C_DEVICE_ADDRESS, [high_addr, low_addr] + data_bytes)
        bus.i2c_rdwr(msg)

def read_registers(start_register, length):
    """
    Read a block of data starting at a 16-bit register address.
    
    :param start_register: The 16-bit register address to start reading from.
    :param length: Number of bytes to read.
    :return: A list of bytes read from the device.
    """
    high_addr = (start_register >> 8) & 0xFF # High byte of 16-bit address
    low_addr = start_register & 0xFF # Low byte of 16-bit address
    with SMBus(I2C_BUS) as bus:
         # First send the 16-bit register address (write without stop / repeated start)
        write_msg = i2c_msg.write(I2C_DEVICE_ADDRESS, [high_addr, low_addr])
        # Then read the requested number of bytes
        read_msg = i2c_msg.read(I2C_DEVICE_ADDRESS, length)
        bus.i2c_rdwr(write_msg, read_msg)
        return list(read_msg)


# Detect the IS3715 on the I2C bus
print("Reading CHIP_ID register...")
chip_id_value = read_registers(CHIP_ID, 1) # Read the chip ID
chip_rev_value = read_registers(CHIP_REV, 1) # Read the chip revision
print "CHIP_ID: ", chip_id_value
print "CHIP_REV: ", chip_rev_value

# Verify if the chip ID matches expected value (21)
if chip_id_value[0] == 21:
    print("IS3715 Detected!")
else:
    print("ERROR: IS3715 not detected!")

# Initialize the DMX array
DMX_Values = [0] * 513 # 0 to 512
DMX_Channel = 1 # We will increment channel 1

while True:
    # Print the current DMX value being written to channel 1
    print "Writing on DMX Channel", DMX_Channel, "value", DMX_Values[1]
    
    # Write the entire DMX memory map starting from start code (address 0)
    write_register(0, DMX_Values)
    
    # Increment the DMX channel value, rollover after 255
    DMX_Values[DMX_Channel] = DMX_Values[DMX_Channel] + 1
    if DMX_Values[DMX_Channel] > 255: 
        DMX_Values[DMX_Channel] = 0
    
    
    
    
