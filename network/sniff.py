#! /usr/bin/env python
import scapy.all as scapy

def sniff(interface):
	scapy.sniff(iface=interface, store=False, prn=cb)

def cb(packet):
	print(packet) 

#choose your interface
sniff("eth0")
	
  
#Vernieri  
