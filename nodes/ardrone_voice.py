#!/usr/bin/python
import subprocess

while 1: 
  print "rec start"

  subprocess.Popen('rec -q -c 1 -r 16000 current.wav silence 1 0.3 3%  1 0.3 3%',shell=True,cwd = '/home/petin/ros_pkgs/vp_ardrone1/nodes/').communicate()

  print "wav - ok"
  subprocess.Popen('flac -f -s current.wav -o current.flac',shell=True,cwd = '/home/petin/ros_pkgs/vp_ardrone1/nodes/').communicate()
  print "flac - ok"
  proc3=subprocess.Popen('php textfromgoogle.php',shell=True, stdout = subprocess.PIPE,cwd = '/home/petin/ros_pkgs/vp_ardrone1/nodes/')  
  result=proc3.communicate()[0]
  str = "result api google = %s"%result
  print str


