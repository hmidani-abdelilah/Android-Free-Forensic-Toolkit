#!/usr/bin/env python

import os, time, sys


def main(casefolder):
	print("\n --> Imaging command sent\n")
	print(" --> Giving device 10 seconds to process command\n")
	time.sleep(10)
	imagedir = os.path.join(casefolder, "image")
	image = os.path.join(imagedir, "image.dd")
	cwd = os.path.dirname(os.path.realpath(__file__))
	winadb = os.path.join(cwd, '..', 'bin', 'adb.exe')
	winnc = os.path.join(cwd, '..', 'bin', 'nc.exe')
	os.system(winadb + ' forward tcp:5555 tcp:5555' if os.name == 'nt' else 'adb forward tcp:5555 tcp:5555')
	winnc_exec = winnc + ' 127.0.0.1 5555 > ' + image
	linnc_exec = 'nc 127.0.0.1 5555 > ' + image
	print(" --> Writing image to host PC\n")
	os.system(winnc_exec if os.name == 'nt' else linnc_exec)
	if sys.platform in ('linux', 'linux2'):
		mountdir = os.path.join(casefolder, "mount")
		if not os.path.exists(mountdir):
			os.makedirs(mountdir)
#		os.system('gdisk -l ' + image + ' > ' + os.path.join(imagedir, "partitioninfo"))
#		os.system('cat ' + os.path.join(imagedir, "partitioninfo") + ' | awk \'f;/Number/{f=1}\' > ' + os.path.join(imagedir, "tmpdata"))
#		mountinfo = os.path.join(casefolder, "mount", "mountinfo")
#		os.system("cat " + os.path.join(imagedir, 'tmpdata') + " | awk '{print $2, $7}' > " + mountinfo)


		
	
	
	
	
