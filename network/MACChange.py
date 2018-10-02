#! /usr/bin/env python

import subprocess

interface = raw_input()
mac = input("Type a new Mac Adress")
subprocess.call("ifconfig "+interface+" down", shell = True)
subprocess.call("ifconfig +"interface"+ hw ether"+ mac, shell = True)
subprocess.call("ifconfig "+interface+" up", shell=True)
