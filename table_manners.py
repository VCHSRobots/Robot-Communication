# ---------------------------------------------------------------------
# table_manners.py -- program to manage parameters table, read changes
#                  -- from driverstation, and deliver table to roboRio
#
# 02/02/2017 KJF Created
# ---------------------------------------------------------------------

import socket, threading, time

def readTable(filename):
	f = open(filename, 'r')
	table = dict()
	for line in f:
		key = line[:line.find('=')].strip().lower()
		value = float(line[(line.find('=')+1):].strip())
		table[key] = value
	f.close()
	return table

def writeTableToFile(table, filename):
	f=open('table_parameters.txt', 'wt')
	for k, v in table.items():
		f.write(k + "=" + str(v) + '\n')
	f.close()
	
def getKey(line):
	# write this
	string = ''
	key = line[:line.find('=')].strip().lower()[2:].strip()
	return key
	
def getValue(line):
	# write this 
	value = 0.0
	value = float(line[(line.find('=')+1):].strip()[:-5])
	return value

def sendTable(conn, table):
	for k, v in table.items():
		line = k + " = " + str(v) + "\n"
		byteLine = bytes(line, 'utf-8')
		conn.send(byteLine)
		print("data sent")
	endLine = 'End of file\n'
	byteEndLine = bytes(endLine, 'utf-8')
	conn.send(byteEndLine)
	print("End of file sent.")
	
