#!/usr/bin/env python
#-*-coding:utf-8 -*-
import roslib; roslib.load_manifest('vp_ardrone1')
import rospy
import subprocess
import shlex

from ardrone_autonomy.msg import *
from ardrone_autonomy.srv import *
from std_msgs.msg import String
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist

matrix = [["поехали","поех","ехал"],["посадка","садка","конец"],["замр","вис",""],["назад","насат"],["перед","перет"],["лев","лего"],["прав"],["верх","выше"],["низ","нис","ниж"],["поворот","орот", "ород"],["круж","круг"],["ыстр","истр"],["медл","лини","тише"]]

def talker():
    pub = rospy.Publisher('ardrone1_textspeech', String)
    rospy.init_node('ardrone1_google_talker')
    twist=Twist()

    while not rospy.is_shutdown():
      subprocess.Popen('rec -q -c 1 -r 16000 current.wav silence 1 0.3 3% 1 0.3 3%',shell=True,cwd = '/home/petin/ros_pkgs/vp_ardrone1/nodes/').communicate()      
      pub.publish("wav - ok") 
      subprocess.Popen('flac -f -s current.wav -o current.flac',shell=True,cwd = '/home/petin/ros_pkgs/vp_ardrone1/nodes/').communicate()
      pub.publish("flac - ok") 
      proc3=subprocess.Popen('php textfromgoogle.php',shell=True, stdout =   subprocess.PIPE,cwd = '/home/petin/ros_pkgs/vp_ardrone1/nodes/') 
      result=proc3.communicate()[0]
      str = "result api google = %s"%result
      index=0
      for ind,elements in enumerate(matrix):
        for element in elements:
          if result.count(element)>0:
            pub.publish(element)
            index=ind+1
            break
      rospy.loginfo(index)
      pub.publish(String(str))
      
if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException: pass

