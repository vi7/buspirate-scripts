#!/usr/bin/env python3

# Bus Pirate UART configuration and interaction guide: http://dangerousprototypes.com/docs/UART_(binary)

# MAINTAINERS (keep in alphabetical order):
# - vi7

import click
from pyBusPirateLite.UART import *

BUS_PIRATE_UART_SPEED_MASKS = {
  300: UARTSpeed._300,
  1200: UARTSpeed._1200,
  2400: UARTSpeed._2400,
  4800: UARTSpeed._4800,
  9600: UARTSpeed._9600,
  19200: UARTSpeed._19200,
  33250: UARTSpeed._33250,
  38400: UARTSpeed._38400,
  57600: UARTSpeed._57600,
  115200: UARTSpeed._115200
}
# Consult http://dangerousprototypes.com/docs/UART_(binary)#100wxxyz_.E2.80.93_Configure_UART_settings for the values
BUS_PIRATE_UART_PIN_OUTPUT =      1  # 3.3V
BUS_PIRATE_UART_DATABITS_PARITY = 0  # 8,NONE
BUS_PIRATE_UART_STOPBITS =        0  # 1
BUS_PIRATE_UART_RX_POLARITY =     0  # Idle 1

def generate_uart_cfg_mask(output, databits, stopbits, polarity):
  cfg_mask = (output << 4) & (databits << 2) & (stopbits << 1) & polarity
  return cfg_mask

def set_uart_speed(bus_pirate, speed_mask):
  bus_pirate.write(0x60 | speed_mask)
  bus_pirate.timeout(0.1)
  return bus_pirate.response(1, binary=True)

def set_uart_cfg(bus_pirate, cfg_mask):
  bus_pirate.write(0x80 | cfg_mask)
  bus_pirate.timeout(0.1)
  return bus_pirate.response(1, binary=True)

########
# MAIN #
########
@click.command()
@click.option("--device", default="/dev/tty.usbserial", show_default=True, help="Bus Pirate device path")
@click.option("--speed", default=115200, show_default=True, help="Bus Pirate connection speed")
@click.argument('uart_speed', default=9600)
def bp_transparent_bridge(uart_speed, device, speed):
  """Script enables transparent UART bridge mode on the Bus Pirate

  UART_SPEED - overrides UART mode speed if passed. Default: 9600
  """
  print('\nBus Pirate transparent UART bridge mode enabler. Hi!\n')
  bp = UART(device, speed)
  bp.enter()
  print(f'Mode name: {bp.mode}\nMode version: {bp.modestring}\n')

  bp_uart_cfg = generate_uart_cfg_mask(
    BUS_PIRATE_UART_PIN_OUTPUT,
    BUS_PIRATE_UART_DATABITS_PARITY,
    BUS_PIRATE_UART_STOPBITS,
    BUS_PIRATE_UART_RX_POLARITY
    )
  set_uart_cfg(bp, bp_uart_cfg)
  set_uart_speed(bp, BUS_PIRATE_UART_SPEED_MASKS[uart_speed])

  print('Enabling transparent UART bridge\n')
  bp.enter_bridge_mode()

if __name__ == '__main__':
    bp_transparent_bridge()
