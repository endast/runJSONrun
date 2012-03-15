#!/usr/bin/env python
# encoding: utf-8
"""
RunViewer.py

Created by Magnus Wahlberg on 2012-03-15.
Copyright (c) 2012 __RedSwampResarch__. All rights reserved.
"""

from getopt import getopt, GetoptError
from sys import argv, exit, platform
import os
import csv
import json

VERSION = "0.1"

def getCSVData(csvFile):
	rawCSV = csv.DictReader(open(csvFile), delimiter=';')
	return rawCSV

def cleanUpHeaders(csvData):
	for idx, fieldname in enumerate(csvData.fieldnames):
		csvData.fieldnames[idx] = fieldname.replace('(', '_').replace(' ', '').replace('/', '').replace(')', '')
	
	return csvData


def usage():
	print "Usage: remotestick-server [OPTION] ..."

def version():
	print "runJSONrun v" + VERSION

def main():
	try:
		opts, args = getopt(argv[1:], "?hi:o:V", ["?", "input=", "output="])
	except GetoptError, err:
		print str(err)
		usage()
		exit(2)
	inputFile = None
	outputFile = None
	
	for o, a in opts:
		if o in ("-i", "--input"):
			inputFile = a
		elif o in ("-o", "--output"):
			outputFile = a
		elif o == "-?":
			usage()
			exit()
		else:
			assert False, "unhandled option " + o


	RunMeterCSVFile = inputFile

#	RunMeterCSVFile = "Runmeter-Cycle-20120315-0804.csv"
	if inputFile != None:
		
		RawcsvData = getCSVData(RunMeterCSVFile)
		csvData = cleanUpHeaders(RawcsvData)
		
		points = []
		for row in csvData:
			points.append(row)

		print json.dumps(points)
			# Lon = row['Longitude']
			# Lat = row['Latitude']
			# print Lat, Lon
		
	else:
		print "Could not read input"
		exit(2)
			
if __name__ == '__main__':
	main()