#!/usr/bin/env python
import subprocess

interface = input("interface > ")
new_mac = input("MAC address > ")

print ("[+] changing mac adress for "+ interface+ " to " + new_mac)

subprocess.call("ifconfig "+ interface +" down",shell=True)
subprocess.call("ifconfig "+ interface +" hw ether "+new_mac,shell=True)
subprocess.call("ifconfig "+ interface + " up",shell=True)