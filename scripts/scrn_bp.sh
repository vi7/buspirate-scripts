#!/usr/bin/env bash

# wrapper for establishing a screen session with the Bus Pirate

screen -h 10000 /dev/tty.usbserial 115200,N,1
