#!/usr/bin/python

import pickle
import sys

def main():
	file = open('inventory.inv', 'r')
	inventoryarr = pickle.load(file)
	file.close()

	while True:
		print "Enter the EAN code of an item you wish to modify."
		linetmp = sys.stdin.readline()
		if not linetmp:
			break
		#line = linetmp.rstrip()[7:]
		line = linetmp.rstrip()
		try:
			tmp = inventoryarr[line]
		except:
			print "This EAN doesn't exist in the database."
			break
		print "Please enter the approximate amount of shelf-life for this item (in days):"
		length = sys.stdin.readline()
		if length:
			predate = inventoryarr[line][0][0]
			inventoryarr[line][0][0]=int(length)
			print "Expiry time updated from " + str(predate) + " days to " + length.rstrip() + " days."


	file = open('inventory.inv', 'w')
	pickle.dump(inventoryarr,file)
	file.close()

if __name__ == "__main__":
	main()
