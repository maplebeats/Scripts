#!/bin/bash

#this script is used to resolve the nvidia random start
#Tips: I can't ensure it's correctness

optirun $1
sudo rm /dev/nvidia*
