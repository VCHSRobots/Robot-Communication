import socket
import time
import table_manners
import datetime

def run(conn, addr):
	#table = table_manners.readTable('table_parameters.txt')
	while 1:
		data = conn.recv(1024)
		if data == (b'Requesting table\n' or b'Requesting table\r\n'):
			table = table_manners.readTable('table_parameters.txt')
			table['timestamp'] = time.time()
			table_manners.writeTableToFile(table, 'table_parameters.txt')
			table_manners.sendTable(conn, table)
		if data == (b'Requesting timestamp\n'):
			table = table_manners.readTable('table_parameters.txt')
			timestamp = table['timestamp']
			stringtimestamp = str(timestamp) + '\n'
			bytetimestamp = bytes(stringtimestamp, 'utf-8')
			conn.send(bytetimestamp)
		if data == (b'\r\n' or b'null\r\n'):
				print(str(data))
				print("null recieved.")
				break
