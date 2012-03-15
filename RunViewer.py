#!/usr/bin/env python
# encoding: utf-8
"""
RunViewer.py

Created by Magnus Wahlberg on 2012-03-15.
Copyright (c) 2012 __RedSwampResarch__. All rights reserved.
"""

import sys
import os
import csv
import json

def getCSVData(csvFile):
	rawCSV = csv.DictReader(open(csvFile), delimiter=';')
	return rawCSV

def cleanUpHeaders(csvData):
	for idx, fieldname in enumerate(csvData.fieldnames):
		csvData.fieldnames[idx] = fieldname.replace('(', '_').replace(' ', '').replace('/', '').replace(')', '')
	
	return csvData

def main():

	RunMeterCSVFile = "Runmeter-Cycle-20120315-0804.csv"
	RawcsvData = getCSVData(RunMeterCSVFile)
	csvData = cleanUpHeaders(RawcsvData)

	headers = csvData.fieldnames
	print headers

	points = []
	for row in csvData:
		points.append(row)
	
#	print json.dumps(points)
		# Lon = row['Longitude']
		# Lat = row['Latitude']
		# print Lat, Lon

if __name__ == '__main__':
	main()