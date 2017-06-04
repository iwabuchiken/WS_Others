#ref https://pypi.python.org/pypi/PyGnuplot

#ref http://blog1.erp2py.com/2010/10/pythonpath.html
import sys
sys.path.append('.')
#ref https://stackoverflow.com/questions/714881/how-to-include-external-python-code-to-use-in-other-files
from libs import *
# import libs

import getopt

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
#import math
#import numpy as np
#from matplotlib import pyplot
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

# 	E		= 2.6660079		# energy of an electron
# 	tick	= 0.1
# 	width	= 20
	max_num		= int(width / tick)
# 	max		= width / tick
	
	V = 0.0		# potential energy
	
	print "E = %f" % E
	
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

def shooting():

	psys, fs = calculate(tick=0.2, E = 2.676)
# 	psys, fs = calculate(tick=0.2)
# 	psys, fs = calculate()
	
	#debug
	a = 10
	max_num = len(psys)
 	
	for i in range(max_num - 1 - a, max_num - 1) :
# 	for i in range(max_num / 2, max_num / 2 + 10) :
 		
		print "[%s:%d] psys[%d] = %f" % (thisfile(), linenum(), i, psys[i])
	

# 	E		= 2.6660079		# energy of an electron
# 	tick	= 0.1
# 	width	= 20
# 	max_num		= int(width / tick)
# # 	max		= width / tick
# 	
# 	V = 0.0		# potential energy
# 	
# 	print "E = %f" % E
# 	
# 	psys = [None] * max_num
# 	fs = [None] * max_num
# # 	psys = [max_num]
# # 	fs = [max_num]
# 	
# 	print "[%s:%d] max_num = %d" % (thisfile(), linenum(), max_num)
# 	
# 	# initial values
# 	psy_0 = 0.0;
# 	f_0 = 0.1;
# 	
# 	psy_cur	= 0.0;
# 	f_cur	= 0.0;
# 
# 	psy_prev = psy_0;
# 	f_prev = f_0;
# 
# 	h2_2m = 38.14;
# 
# 	
# 	psys[0] = psy_0
# 	fs[0] = f_0
# 	
# # 	print "[%s:%d] meesge" % location()
# 	
# 	# iterate
# # 	for i in range(1, max_num - 1, 1):
# 	for i in range(1, max_num, 1):
# # 	for i = 1; i <= max; i ++:
# 		
# 		if i * tick < 5 or i * tick >= 15 : V = 50.0
# 		else : V = 0.0
# 
# 		psy_cur = tick * f_prev + psy_prev
# 
# 		f_cur = -1 * tick * psy_prev * (E - V) / h2_2m + f_prev
# 
# # 		#debug
# # 		print "[%s:%d] i = %d" % (thisfile(), linenum(), i)
# 
# 
# 		psys[i]	= psy_cur
# 		fs[i]	= f_cur
# 
# 		# update prev
# 		psy_prev	= psy_cur
# 		f_prev		= f_cur
# 
# 		
# # 		// V : potential energy
# # 		if (i * tick < 5 || i * tick >= 15) V = 50.0;
# # 		else V = 0.0;
# # 
# # 		// calc
# # 		psy_cur = tick * f_prev + psy_prev;
# # 
# # 		f_cur = -1 * tick * psy_prev * (E - V) / h2_2m + f_prev;
# # 
# # 		psys[i]	= psy_cur;
# # 		fs[i]	= f_cur;
# # 
# # //		printf("[%s:%d] psy_cur = %2.7f / f_cur = %2.7f\n",
# # //				basename(__FILE__, '\\'), __LINE__, psy_cur, f_cur);
# # 
# # 
# # 		// update prev
# # 		psy_prev	= psy_cur;
# # 		f_prev		= f_cur;
# # 
# # 	}//for (i = 0; i < 20; ++i) {
# 	#]] for
# 
# # 	#debug
# # 	a = 10
# # 	
# # 	for i in range(max_num - 1 - a, max_num - 1) :
# # # 	for i in range(max_num / 2, max_num / 2 + 10) :
# # 		
# # 		print "[%s:%d] psys[%d] = %f" % (thisfile(), linenum(), i, psys[i])
# 
# 	# return
# 	return (psys, fs)
	
if __name__ == '__main__':
	
	shooting()
	
	#test
#	__line__()
	num = linenum()
	print num
	
	name = thisfile()
# 	name = _file()
	
	print name
	

else:
	print "no"

#test_4()
