#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 12:33:35 2021

@author: saisons
"""
from datetime import datetime
import os
import pynput
from pynput.keyboard import Key, Controller
import time
keyboard = Controller()
number = input("How Many People to Generate?") 
number = int(number)
print(number)
i = 0
while i < number:
    dateTimeObj = datetime.now()
    timestamp = dateTimeObj.strftime("%H:%M:%S.%f")
    print(timestamp)
    filename = timestamp+'.txt'
    os.system('python3 createPocketLint.py > GeneratedPeople/'+filename)
    f = open("GeneratedPeople/"+timestamp+".txt", "r")
    print(f.read())
    i += 1
print("Run Complete")