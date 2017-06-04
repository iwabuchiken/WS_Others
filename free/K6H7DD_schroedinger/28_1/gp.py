'''
<Usage>
gp.py -E2.721589094 --PLOT_GO --SAVE_GO

gp.py -E2.721589094 --PLOT_GO --SAVE_IMAGE_GO

'''

#ref https://pypi.python.org/pypi/PyGnuplot
# pushd C:\WORKS_2\WS\WS_Others\free\K6H7DD_schroedinger\28_1

#ref http://blog1.erp2py.com/2010/10/pythonpath.html
import sys
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

'''
	@param E ---> "gp.py -E2.72159" ==> 'psys[199] = 0.018659'
'''
#ref 'False' https://www.codecademy.com/en/forum_questions/509f1eaedc99f2a6050000c0 "Pickles123"
def plot_PsysData(psys, fs, E, width, output = False, tick=0.1):
# def plot_PsysData(psys, fs, E, width, output = false):

	print "[%s:%d] plot_PsysData(psys, fs)" % (thisfile(), linenum())

	x = np.arange(0, width, tick)
# 	x = np.arange(0, 20, 0.1)
	
# 	print "[%s:%d] x => " % (thisfile(), linenum()), x

	#ref https://stackoverflow.com/questions/8209568/how-do-i-draw-a-grid-onto-a-plot-in-python "answered Nov 21 '11 at 11:00"
	fig = pyplot.figure()
	ax = fig.gca()
	ax.set_xticks(np.arange(0, 20, 5))
# 		ax.set_xticks(numpy.arange(0, 1, 0.1))
	ax.set_yticks(np.arange(0, 40, 5))
# 	ax.set_yticks(np.arange(0, 1., 0.1))
	
	pyplot.grid()
	
	pyplot.title("Psys : E=%2.9f" % E)

	pyplot.plot(x, psys)
# 	pyplot.show()

	'''
	output
	'''
# 	if output == True :
		
	filename = "data/psy_fs.%s.E-%2.9f.psys-%3.6f.png" % \
			(get_TimeLabel_Now(mili=True), E, psys[len(psys) - 1])
# 		filename = "data/psy_fs.%s.E-%2.9f.png" % (get_TimeLabel_Now(), E)
# 		filename = "data/psy_fs.%s.E-%2.9f.dat" % (get_TimeLabel_Now(), E)
		
	print "[%s:%d] filename => %s" % (thisfile(), linenum(), filename)

	if output == True :
		pyplot.savefig(filename)
		
		print "[%s:%d] file => saved : '%s'" % (thisfile(), linenum(), filename)

		
	#ref http://qiita.com/irs/items/cd1556c568887ff2bdd7
# 		pyplot.grid(which='major',color='gray',linestyle='*')
# 		pyplot.grid(which='minor',color='black',linestyle='-')

# 		fig = pyplot.figure()
# 		ax = fig.gca()
# 		ax.set_xticks(np.arange(0, 20, 1))
# # 		ax.set_xticks(numpy.arange(0, 1, 0.1))
# 		ax.set_yticks(np.arange(0, 1., 0.1))
# 		
# 		pyplot.grid()
	
	pyplot.show(True)
# 		pyplot.show()
	

#]]def plot_PsysData(psys, fs, E, width, output = false):


def calculate(E = 2.6660079, V_ceiling = 50.0, tick	= 0.1, width	= 20):

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

def shooting():

	#ref https://www.tutorialspoint.com/python/python_command_line_arguments.htm
# 	print sys.argv
# 	print sys.argv[1:]

	# variables
	E = None
	
	flag_Plot = False

	flag_SaveImage = False

	#test
	opts = get_opt(sys.argv[1:])
	
	print "[%s:%d] opts => " % (thisfile(), linenum()), opts

# 	print opts
	
	
	
	if len(opts) > 0 :
		
# 		print opts[0][1], " ", "is ", opts[0][1] * 2	#=> '2.68   is  2.682.68'
# # 		print opts[0][1]
# 		print float(opts[0][1]), " ", "is ", float(opts[0][1]) * 2	#=> '2.68   is  5.36'
# # 		print float(opts[0][1])
	
		for elem in opts :
			
			if elem[0] == '-E' :
				
				#ref https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points "answered Jun 30 '11 at 18:53"
				E = round(float(elem[1]), 9)
# 				E = float(elem[1])
				
				print "[%s:%d] E is now => %.9f" % (thisfile(), linenum(), E)
# 				print "[%s:%d] E is now => %f" % (thisfile(), linenum(), E)

			elif elem[0] == 'PLOT_GO' :
				
				flag_Plot = True
	
			elif elem[0] == 'SAVE_IMAGE_GO' :
				
				flag_SaveImage = True
	
			
	
# 	try:
# 		
# 		print "[%s:%d] getopt => calling..." % (thisfile(), linenum())
# 
# 		opts, args = getopt.getopt(sys.argv[1:],"Ei:o:",["ifile=","ofile="])
# # 		opts, args = getopt.getopt(sys.argv[1:],"hi:o:",["ifile=","ofile="])
# # 		opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
# 
# 		#debug
# 		print opts
# 
# 	except getopt.GetoptError:
# 		print 'test.py -i <inputfile> -o <outputfile>'
# 		sys.exit(2)

	# put value to E
	if E == None : E = 2.676

# 	print "[%s:%d] passing E value => %f" % (thisfile(), linenum(), E)
	
	width_ = 20
	
	tick_ = 0.1

	psys, fs = calculate(E, tick=tick_, width=width_)
# 	psys, fs = calculate(E, tick=0.1, width=width_)
# 	psys, fs = calculate(E, tick=0.1)
# 	psys, fs = calculate(E, tick=0.2)
# 	psys, fs = calculate(tick=0.2, E = 2.676)
# 	psys, fs = calculate(tick=0.2)
# 	psys, fs = calculate()
	
# 	#debug
# 	a = 10
# 	max_num = len(psys)
#  	
# 	for i in range(max_num - a, max_num) :
# # 	for i in range(max_num - 1 - a, max_num - 1) :
# # 	for i in range(max_num / 2, max_num / 2 + 10) :
#  		
# 		#ref multiline https://stackoverflow.com/questions/53162/how-can-i-do-a-line-break-line-continuation-in-python "answered Sep 9 '08 at 23:52"
# 		print "[%s:%d] psys[%d] = %f / fs[%d] = %f" \
# 				% (thisfile(), linenum(), i, psys[i], i, fs[i])

	#ref multiline comment https://stackoverflow.com/questions/7696924/way-to-create-multiline-comments-in-python ""answered Oct 8 '11 at 12:58
	'''
	report ==> last index value
	'''
	print "[%s:%d] psys[%d] = %f" %\
		 (thisfile(), linenum(), len(psys) - 1, psys[len(psys) - 1])

	'''
	Plot
	'''
	if flag_Plot == True :
		#plot_PsysData(psys, fs, E, width, output = False)
		output_ = False
		
		if flag_SaveImage == True : output_ = True
		
		plot_PsysData(psys, fs, E, width_, output = output_, tick=tick_)
# 		plot_PsysData(psys, fs, E, width_, output = True, tick=tick_)
	# 	plot_PsysData(psys, fs, E, width_, output = False, tick=tick_)

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
	
# 	#debug
# 	print "[%s:%d] time label => %s" % (thisfile(), linenum(), get_TimeLabel_Now(string_type="serial", mili=True))
		

else:
	print "no"

#test_4()
