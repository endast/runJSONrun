#!/usr/bin/env python
# encoding: utf-8
"""
runJSONrun.py

Created by Magnus Wahlberg on 2012-03-15.
Copyright (c) 2012 __RedSwampResarch__. All rights reserved.
"""

from getopt import getopt, GetoptError
from sys import argv, exit, platform
import sys
import os
import csv
import json

VERSION = "0.1"

def getCSVData(csvFile):
	try:
		rawCSV = csv.DictReader(open(csvFile), delimiter=';')
		return rawCSV
		
	except IOError, (errno, strerror):
		print "I/O error(%s): %s" % (errno, strerror)
    	exit(2)


def cleanUpHeaders(csvData):
	for idx, fieldname in enumerate(csvData.fieldnames):
		csvData.fieldnames[idx] = fieldname.replace('(', '_').replace(' ', '').replace('/', '').replace(')', '')
	
	return csvData

def writeJSON(JSONdata, outputFile):
	
	# No outputfile specified, dump to stdout
	if outputFile == None:
		print JSONdata
	else:
		print "Writing JSON data to", outputFile
		
		try:
			jsonFile = open(outputFile,"w")
			jsonFile.writelines(JSONdata)
			jsonFile.close()
		
		except IOError, (errno, strerror):
			print "I/O error(%s): %s" % (errno, strerror)
	    	exit(2)
		
def usage():
	print "\nUsage: runJSONrun.py -i file.csv ..."
	print "Convert runmeter (http://www.abvio.com/runmeter/) csv files to JSON."
	print ""
	print "If you start runJSONrun and only specify a csv file, it will dump the JSON data to standard out."
	print ""
	print "-?, \t\tPrint this help and exit..."
	print "-i, --input\tThe runmeter CSV file to read"
	print "-o, --output\tThe file you wan't the JSON data to be written to"
	print "-V, \t\tPrint the version and exit\n"

def version():
	print "runJSONrun v" + VERSION

def main():

	try:
		opts, args = getopt(argv[1:], "?hi:o:V", ["?", "input=", "output=", "--version"])
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
		elif o in ("-V", "--version"):
			version()
			exit()
		elif o == "-?":
			usage()
			exit()
		else:
			assert False, "unhandled option " + o
			exit(2)
		
	if inputFile != None:

		# Parse the CSV file
		RawcsvData = getCSVData(inputFile)
		csvData = cleanUpHeaders(RawcsvData)
		
		# Add all data points to an array
		dataPoints = []
		for row in csvData:
			dataPoints.append(row)
		
		# Convert the data to JSON
		jsonData = json.dumps(dataPoints)
		
		# Output the jsondata, to stdout
		writeJSON(jsonData, outputFile)
		
	else:
		print "No input file... exiting."
		exit(2)
			
if __name__ == '__main__':
	main()