#!/usr/bin/python
import subprocess

while 1: 
  print "rec start"

  subprocess.Popen('padsp julius -quiet -input mic -C julian.jconf 2>/dev/null | ./ros_ardrone1_julius_to_text.py').communicate()



