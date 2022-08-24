#!/usr/bin/env python
import subprocess
import optparse
def get_arguments():

    parser = optparse.OptionParser()
    parser.add_option("-i","--interface",dest="interface",help="interface to change it mac address")
    parser.add_option("-m","--mac",dest="new_mac",help="new mac address")
    (options,arguments)=parser.parse_args()
    if not options.interface:
        parser.error("[-] pls specify  the interface ,use --help for more info ")
    elif not options.new_mac:
        parser.error("[-] pls specify  the mac address  ,use --help for more info ")
    return options
def mac_changer(interface,new_mac):

    print ("[+] changing mac adress for "+ interface+ " to " + new_mac)
    subprocess.call(["ifconfig",interface,"down"])
    subprocess.call(["ifconfig",interface,"hw","ether",new_mac])
    subprocess.call(["ifconfig",interface,"up"])
options = get_arguments()
mac_changer(options.interface,options.new_mac)