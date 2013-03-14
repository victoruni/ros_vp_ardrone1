#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Узел ardrone1_julius_talker, получающий результат программы julius(распознование речи) из stdin 
# (скрипт ros_ardrone1_julius_init.py) и публикующий строку в тему ardrone1_textspeech
#


import roslib; roslib.load_manifest('vp_ardrone1') 
import rospy
from std_msgs.msg import String
import os
import subprocess
import sys

def Control(file_object):
       pub = rospy.Publisher('ardrone1_textspeech', String)
       rospy.init_node('ardrone1_julius_talker')
       startstring = 'sentence1: <s> '
       endstring = ' </s>'

       while not rospy.is_shutdown():
	 line = file_object.readline()
	 if not line:
				break
	   
         end = len(line)-6
         if line[0:9] == 'sentence1':
	    word = line[15:end]
	    print word
            str = word
            rospy.loginfo(str)
            pub.publish(String(str))
         rospy.sleep(0.001)
if __name__ == '__main__':
       try:
           Control(sys.stdin)
       except rospy.ROSInterruptException: pass
       except KeyboardInterrupt:
       		sys.exit(1)
   
   
