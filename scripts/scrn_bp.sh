#!/usr/bin/env bash

# wrapper for establishing a screen session with the Bus Pirate

# !! WARNING: port discovery might possibly conflict with other USB-to-Serial devices (Arduino etc.)

screen -h 10000 $(ls -1 /dev/cu.usbserial-14* | head -n1) 115200,N,1
