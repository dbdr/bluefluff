#!/usr/bin/env python3

import binascii
import argparse
import math
import sys
import os

# Parse path to DLC file
parser = argparse.ArgumentParser()
parser.add_argument("dlcfile", help="Path to DLC file")
args = parser.parse_args()

# Create new image, height depends on DLC file size
dlcsize = os.path.getsize(args.dlcfile)

def printBuf(buf):
	hexLine = ''
	for byte in buf:
		hexLine += format(byte, '02x') + ' '
	print(hexLine)
	
with open(args.dlcfile, "rb") as dlc:
	magic = dlc.read(10)

	if magic != b'F\x00U\x00R\x00B\x00Y\x00':
		print('Not a Furby DLC file')
		exit(1)
	
	header = dlc.read(68)

	printBuf(header)
