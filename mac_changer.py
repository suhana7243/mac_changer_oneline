import subprocess
import optparse

parser = optparse.OptionParser()

parser.add_option("-i","--interface",dest="interface",help="interface to change its mac address")
parser.add_option("-m","--mac",dest="macadd",help="new mac address")
(option,arguments)=parser.parse_args()

interface=option.interface
macadd=option.macadd

subprocess.call(["ifconfig",interface,"down"])
subprocess.call(["ifconfig",interface,"hw","ether",macadd])
subprocess.call(["ifconfig",interface,"up"])