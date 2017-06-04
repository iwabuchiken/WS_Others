#ref https://pypi.python.org/pypi/PyGnuplot
# pushd C:\WORKS_2\WS\WS_Others\free\K6H7DD_schroedinger\28_1

#ref http://blog1.erp2py.com/2010/10/pythonpath.html
import sys
from sympy.logic.boolalg import false
sys.path.append('.')
#ref https://stackoverflow.com/questions/714881/how-to-include-external-python-code-to-use-in-other-files
from libs import *
# import libs

import getopt
import os
import inspect

#import PyGnuplot as gp
#import numpy as np
#
#X = np.arange(10)
#Y = np.sin(X/(2*np.pi))
#Z = Y**2.0
#
#gp.s([X,Y,Z])
#
##gp.c('plot cos(x)')
##gp.c('plot sin(x)')
#
#gp.c('plot "tmp.dat" u 1:2 w lp')
#gp.c('replot "tmp.dat" u 1:3 w lp')
##gp.c('plot "tmp.dat" u 1:2 w lp')
##gp.c('replot "tmp.dat" u 1:3 w lp')
##gp.p('myfigure.ps')
#gp.p('myfigure.png')

##ref http://programming-study.com/technology/python-matplotlib/#matplotlib-2
import math
import numpy as np
from matplotlib import pyplot
#
#
#
#pi = math.pi
#
#x = np.linspace(0, 2*pi, 100)
#y = np.sin(x)
#
#pyplot.plot(x, y)
#pyplot.show()

def test_4():
	#https://sites.google.com/site/tibracode/python/matplotlib/savefig
	import matplotlib.pyplot as plt
	
	x = [1,2,3,4,5,6]
	y = [2,5,4,6,8,7]
	plt.plot(x,y)
	
	filename = "output-2.png"
	plt.savefig(filename)

#ref http://d.hatena.ne.jp/kwatch/20100410/1270851205
#depend ==> inspect
def location(depth=0):
	frame = inspect.currentframe(depth+1)
	return (frame.f_code.co_filename, frame.f_lineno)
     
# def linenum():
# 	print "line"

def calculate(E = 2.6660079, V_ceiling = 50.0, tick	= 0.1, width	= 20):

	print "[%s:%d] E => %f" % (thisfile(), linenum(), E)


# 	E		= 2.6660079		# energy of an electron
# 	tick	= 0.1
# 	width	= 20
	max_num		= int(width / tick)
# 	max		= width / tick
	
	V = 0.0		# potential energy
	
# 	print "E = %f" % E
	
	psys = [None] * max_num
	fs = [None] * max_num
# 	psys = [max_num]
# 	fs = [max_num]
	
	print "[%s:%d] max_num = %d" % (thisfile(), linenum(), max_num)
	
	# initial values
	psy_0 = 0.0;
	f_0 = 0.1;
	
	psy_cur	= 0.0;
	f_cur	= 0.0;

	psy_prev = psy_0;
	f_prev = f_0;

	h2_2m = 38.14;

# 	V_ceiling = 50.0
	
	psys[0] = psy_0
	fs[0] = f_0
	
# 	print "[%s:%d] meesge" % location()
	
	# iterate
# 	for i in range(1, max_num - 1, 1):
	for i in range(1, max_num, 1):
# 	for i = 1; i <= max; i ++:
		
		if i * tick < 5 or i * tick >= 15 : V = V_ceiling
# 		if i * tick < 5 or i * tick >= 15 : V = 50.0
		else : V = 0.0

		psy_cur = tick * f_prev + psy_prev

		f_cur = -1 * tick * psy_prev * (E - V) / h2_2m + f_prev

		psys[i]	= psy_cur
		fs[i]	= f_cur

		# update prev
		psy_prev	= psy_cur
		f_prev		= f_cur
		

	# return
	return (psys, fs)
	
#]]def calculate():

def plot_PsysData(psys, fs, E, width, output = false):
	
	print "[%s:%d] plot_PsysData(psys, fs)" % (thisfile(), linenum())

	#ref https://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html
	x = np.arange(0, 20, 0.1)
	
	print "[%s:%d] len(x) => %d" % (thisfile(), linenum(), len(x))

# 	x = np.linspace(0, 20, len(psys))
	y = np.sin(x)

# 	pyplot.plot(x, y)
	pyplot.plot(x, psys)
	pyplot.show()
	
# 	filename = "-E2.721589094"
# 	pyplot.savefig(filename)
	
#]]plot_PsysData(psys, fs)	
	

def shooting():

	#ref https://www.tutorialspoint.com/python/python_command_line_arguments.htm
# 	print sys.argv
# 	print sys.argv[1:]

	# variables
	E = None

	#test
	opts = get_opt(sys.argv[1:])
	
	if len(opts) > 0 :
		
		for elem in opts :
			
			if elem[0] == '-E' :
				
# 				E = round(float(elem[1]), 9)
# 				E = round(float(elem[1]), 7)
				E = float(elem[1])
				
				print "[%s:%d] E is now => %f" % (thisfile(), linenum(), E)
	
	##]if len(opts) > 0 :
	
	# put value to E
	if E == None : E = 2.676

	'''
	Calculate
	'''
	width = 20
	
	psys, fs = calculate(E, width, tick=0.1)
	
	#ref multiline comment https://stackoverflow.com/questions/7696924/way-to-create-multiline-comments-in-python ""answered Oct 8 '11 at 12:58
	'''
	report ==> last index value
	'''
	print "[%s:%d] psys[%d] = %f" %\
		 (thisfile(), linenum(), len(psys) - 1, psys[len(psys) - 1])

	'''
	generate : data file
	'''
# 	plot_PsysData(psys, fs)
# 	plot_PsysData(psys, fs, E, width, output = false)

#]]def shooting()
	
if __name__ == '__main__':
	
	shooting()
	
# 	#test
# #	__line__()
# 	num = linenum()
# 	print num
# 	
# 	name = thisfile()
# # 	name = _file()
# 	
# 	print name
	

else:
	print "no"

#test_4()
