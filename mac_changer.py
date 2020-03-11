import subprocess
import optparse
import re

def get_arguments():
   parser = optparse.OptionParser()
   parser.add_option("-i","--interface",dest="interface", help="interface to change the MAC")
   parser.add_option("-m","--mac",dest="mac",help="the new MAC address")

   (options, arguments) = parser.parse_args()

   if not options.interface:
          parser.error("Please specify the interface, for more info write --help")
   elif not options.mac:
          parser.error("Please specify the new MAC, for more info write --help")

   return options

def change_mac(interface, new_mac):
   print("[+]Changing MAC address for " + interface + ", to the new address " + new_mac)
   subprocess.call(["sudo", "ifconfig", interface,  "down"])
   subprocess.call(["sudo", "ifconfig", interface,  "hw", "ether", new_mac])
   subprocess.call(["sudo", "ifconfig", interface, "up"])

def get_current_mac(interface):
   ifconfig_result = subprocess.check_output(["sudo", "ifconfig", interface])
   mac_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

   if mac_search_result:
      return mac_search_result.group(0)
   else:
      print("Couldn't read the MAC address")

options = get_arguments()
current_mac = get_current_mac(options.interface)
print("The current MAC is : " + str(current_mac))

change_mac(options.interface, options.mac)
current_mac = get_current_mac(options.interface)

if current_mac == options.mac: 
   print("MAC address was successfully changed to " + current_mac)
else:
   print("Couldn't change the MAC address")
