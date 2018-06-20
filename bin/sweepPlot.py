#!/usr/bin/python3

import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

#creates a dummy dictionary for testing purposes
def DummyDictionary(size) : 
	d = {}
	for i in range(size) :
		d.setdefault(i, i**2)
	#for i in range(size) :
	#	d.setdefault(i+.5, 2*i)
	d.setdefault(2.5, 200)
	return d

#returns a sorted list of 2-tuples from the given dictionary
def SortDictionary(d) :
	l = d.items()
	l.sort()
	return l
	
#Plots the dictionary d and saves the result to fileName
def PlotSweep(d, fileName) :
	l = SortDictionary(d)
	#print l
	#print l
	#print zip(*l)
	x, y = zip(*l)
	plt.plot(x, y)
	plt.xlabel("Row")
	plt.ylabel("Speed")
	plt.title("FPGA Sweep")
	plt.savefig(fileName)

def Test() :
	d = DummyDictionary(12)
	PlotSweep(d, "plot.png")
	print "a plot has been saved to plot.png"
	

if len(sys.argv) == 1 : #if no arguments are given then run the test
	print "test begun"
	Test()
#todo : add functionality to read a dictionary from a file
else :
	print "error" 



