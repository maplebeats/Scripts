#!/bin/bash

#this script is used to resolve the nvidia card power on at random 
#Tips: I can't ensure it's correctness

optirun $1
sudo rm /dev/nvidia*
