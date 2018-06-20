#!/usr/bin/python3

import sys
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def main():

    readFile = sys.argv[1]
    writeFile = sys.argv[2]

    with open(readFile, 'r') as inFile:
        contents = inFile.read()
        jsonInput = json.loads(contents)

        toPlot = []
        i = 0
        while (i < len(jsonInput)):
            key = str(i)
            value = jsonInput[key]
            toPlot.append(int(value))
            i += 1

        Plot(toPlot, writeFile)

def Plot(intList, outFile):
    	plt.plot(range(len(intList)), intList)
	plt.xlabel("Row")
	plt.ylabel("Speed")
	plt.title("FPGA Sweep")
	plt.savefig(outFile)

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
	

if __name__ == '__main__':
    if len(sys.argv) == 1:
	print "test begun"
	Test()

    else:
        main()


