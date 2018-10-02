#! /usr/bin/env python

import subprocess

mac = input("Type a new Mac Adress")
subprocess.call("ifconfig eth0 down", shell = True)
subprocess.call("ifconfig eth0 hw ether", mac, shell = True)
subprocess.call("ifconfig eth0 up", shell=True)
