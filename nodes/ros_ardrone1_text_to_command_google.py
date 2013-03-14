#!/usr/bin/env python
#-*-coding:utf-8 -*-

# 
#  Слушатель ros_ardrone1_sub_voice
#  чтение сообщений из темы ardrone1_textspeech (строка голосовой команды)
#  и отправка команд и установка параметров
#  для управления ardrone 2.0
#


import roslib; roslib.load_manifest('vp_ardrone1')
import rospy
import subprocess
import shlex

from ardrone_autonomy.msg import *
from ardrone_autonomy.srv import *
from std_msgs.msg import String
from std_msgs.msg import Int32
from std_msgs.msg import Empty
from geometry_msgs.msg import Twist

arr_commands=[["DRONE","Роберт"],
              ["привет","пока","молодец"],
              ["взлет","посадка","база"],
              ["вперед","назад","влево","вправо","поворот","вверх","вниз","висеть","сальто"],
              ["один","два","три","четыре","пять","шесть","семь","восемь","девять"],
              ["быстрее","медленнее"]]
digits=[100000,10000,1000,100,10,1]
ok_fraza=[
     "110000","010000",                       
     "101000","001000",
     "100100","000100","100110","000110"
     "100001","000001","100101","000101"]              

def controller(data):

    if(data.data>0):
      str = data.data
    
    rospy.loginfo(str)

    arr_str=str.split();
    count1=0;count2=0;
    # разбор предложения
    #str1="";str2="";
    for word in arr_str:
      for ind1,frazes in enumerate(arr_commands):
        for ind2,fraza in enumerate(frazes):
          if fraza==word:
            count1=count1+digits[ind1]
            count2=count2+digits[ind1]*(ind2+1)
    rospy.loginfo(String(count2))
    pub1=rospy.Publisher('ardrone1_move', Int32)
    pub1.publish(count2) 
    #rospy.loginfo(str)


      
def listener():
   #pub = rospy.Publisher('ardrone1_move', Int32)
   rospy.init_node('ros_ardrone1_sub_voice')
   sub = rospy.Subscriber("ardrone1_textspeech",String,controller)
   rospy.spin()
 
if __name__ == '__main__':
   listener()
   
