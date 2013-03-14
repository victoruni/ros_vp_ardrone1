#!/bin/bash

while [ true ]; do
     padsp julius -quiet -input rawfile -filelist /home/petin/ros_pkgs/vp_ardrone1/nodes/voice.txt -C /home/petin/julius-grammar/julian.jconf
done

