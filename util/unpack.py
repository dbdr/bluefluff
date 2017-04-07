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

def parseEntry(dlc):
	entryHeader = dlc.read(18)
	if entryHeader[0] == 0xff and entryHeader[1] == 0x7f:
		return False
	if entryHeader[0] == 0:
		# skip the rest of the (empty) entry
		dlc.read(20)
		return True
	if entryHeader != b'D\x00L\x00C\x00_\x000\x000\x000\x000\x00.\x00':
		print('Surprising entry header %s' % entryHeader)
		exit(1)
	entryType = dlc.read(8)
	type = '%c%c%c' % (entryType[0],entryType[2],entryType[4])
	print(type)
	entry = dlc.read(12)
	printBuf(entry)
	return True

with open(args.dlcfile, "rb") as dlc:
	magic = dlc.read(10)

	if magic != b'F\x00U\x00R\x00B\x00Y\x00':
		print('Not a Furby DLC file')
		exit(1)
	
	header = dlc.read(68)

	#printBuf(header)

	while parseEntry(dlc):
		pass
