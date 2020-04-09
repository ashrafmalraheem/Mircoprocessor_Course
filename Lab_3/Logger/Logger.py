'''/*****************************************************************************
 * Copyright (C) 2020 by R&D SEDC
 *
 * Redistribution, modification or use of this software in source or binary
 * forms is permitted as long as the files maintain this copyright. Users are
 * permitted to modify this and use it to learn about the field of embedded
 * software. SEDC are not liable for any misuse of this material.
****************************************************************************/'''
'''/**
 * @file Logger.py
 * @brief 
 *
 *  
 *
 * @author: R&D SEDC
 * @Modifyed: 
 * @date February 13, 2020, 2:20 PM
 *
 */'''


'''/*
 * Section: Included Files
 */'''
import serial
import time
import os
import datetime
## Constants
BAUD_RATE = 2400
TX_BUFFER_MAX_SIZE = 100
''' Logging Directory and File'''
DIR = "Logs/"
if not os.path.exists(DIR):
    os.makedirs(DIR)
Log_file_name = DIR + "Log_" + str(datetime.date.today()) + ".log"
print(Log_file_name)
log_file = open(Log_file_name,'a+')
if log_file == None:
    log_file = open(Log_file_name,'w+')
print("Logger Program")
''' Communication port opening '''
spec_file = open('../specs.mk','r')
x = 'hello'
while x != '':
    x = spec_file.readline()
    if x.find('COM = ') != -1:
        COM_PORT = 'COM' + x.strip('COM = \n')
ser = serial.Serial(COM_PORT,baudrate=BAUD_RATE, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, timeout=None, exclusive = 1)
#ser.open(COM13)
#ser.write(b'hello')
print(COM_PORT)
while True :
    y = ser.read_until(b'\n',size = TX_BUFFER_MAX_SIZE)
    x = str(y,'utf-8')
    x = x.strip('\n')
    print(COM_PORT,datetime.datetime.now(),x)
    print(COM_PORT,datetime.datetime.now(),x,file = log_file)
    #Remove the close when you find a way to exit from Keyboard
    log_file.close()
    log_file = open(Log_file_name,'a+')
ser.close()
log_file.close()