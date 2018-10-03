#! /bin/usr/env python

import scapy.all as scapy

ip = input("Digite o IP")

def scan(ip):
  scapy.arping(ip)

scan(ip)
