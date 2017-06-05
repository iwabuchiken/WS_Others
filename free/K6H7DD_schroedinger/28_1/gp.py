'''
<Usage>
pushd C:\WORKS_2\WS\WS_Others\free\K6H7DD_schroedinger\28_1

gp.py -E2.721589094 --PLOT_GO
gp.py -E2.721589094 --PLOT_GO --SAVE_GO

gp.py -E2.721589094 --PLOT_GO --SAVE_IMAGE_GO

### session : 31#1
pushd C:\WORKS_2\WS\WS_Others\free\K6H7DD_schroedinger\28_1
gp.py -E2.721589094 --PLOT_GO --SAVE_IMAGE_GO -s10.62 -e 10.92 -t0.01
gp.py -E2.721589094 --PLOT_GO --SAVE_IMAGE_GO -s10.62 -e 10.92 -t0.001
gp.py -E2.721589094 --PLOT_GO --SAVE_IMAGE_GO -s10.62 -e 10.92 -t0.001

'''

#ref https://pypi.python.org/pypi/PyGnuplot
# pushd C:\WORKS_2\WS\WS_Others\free\K6H7DD_schroedinger\28_1

#ref http://blog1.erp2py.com/2010/10/pythonpath.html
import sys
from sympy.functions.combinatorial.numbers import nP
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
def psysData_Plot(psys, fs, E, width, dpath, output = False, tick=0.1):
# def plot_PsysData(psys, fs, E, width, output = False, tick=0.1):
# def plot_PsysData(psys, fs, E, width, output = false):

	print "[%s:%d] psysData_Plot(psys, fs)" % (thisfile(), linenum())

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

# 	'''
# 	output
# 	'''
# # 	if output == True :
# 		
# # 	filename = "data/psy_fs.%s.E-%2.9f.psys-%3.6f.png" % \
# # 			(get_TimeLabel_Now(mili=True), E, psys[len(psys) - 1])
# 	file_path = "%s/psy_fs.E-%2.9f_psys-%3.6f_width-%3d_tick-%2.2f.png" % \
# 			(dpath, E, psys[len(psys) - 1], width, tick)
# # 		filename = "data/psy_fs.%s.E-%2.9f.png" % (get_TimeLabel_Now(), E)
# # 		filename = "data/psy_fs.%s.E-%2.9f.dat" % (get_TimeLabel_Now(), E)
# 		
# 	print "[%s:%d] file path => %s" % (thisfile(), linenum(), file_path)
# # 	print "[%s:%d] filename => %s" % (thisfile(), linenum(), filename)
# 
# 	# basename
# 	file_name = os.path.basename(file_path)
# 	
# 	print "[%s:%d] file_name => %s" % (thisfile(), linenum(), file_name)
	

# 	# dir path
# 	#ref http://www.gesource.jp/programming/python/code/0009.html
# 	os.makedirs(dpath)

# 	if output == True :
# 		
# 		pyplot.savefig(file_path)
# 		
# 		print "[%s:%d] file => saved : '%s'" % (thisfile(), linenum(), file_path)

		
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
	

#]]def psysData_Plot(psys, fs, E, width, output = false):

# def plot_PsysData(psys, fs, E, width, output = False, tick=0.1):
def psysData_SaveImage(psys, fs, E, width, dpath, output = False, tick=0.1, suffix=None):
# def psysData_SaveImage(psys, fs, E, width, dpath, output = False, tick=0.1):
# def plot_PsysData(psys, fs, E, width, output = false):

	print "[%s:%d] psysData_Plot(psys, fs)" % (thisfile(), linenum())

	x = np.arange(0, width, tick)

	#ref https://stackoverflow.com/questions/8209568/how-do-i-draw-a-grid-onto-a-plot-in-python "answered Nov 21 '11 at 11:00"
	fig = pyplot.figure()
	ax = fig.gca()
	ax.set_xticks(np.arange(0, 20, 2.5))
# 	ax.set_xticks(np.arange(0, 20, 5))
# 		ax.set_xticks(numpy.arange(0, 1, 0.1))
	ax.set_yticks(np.arange(-400, 400, 5))
# 	ax.set_yticks(np.arange(0, 40, 5))
# 	ax.set_yticks(np.arange(0, 1., 0.1))

	ax.set_ylim([-50, 50])
	
	pyplot.grid()
	
	pyplot.title("Psys : E=%2.9f" % E)

	pyplot.plot(x, psys)

	'''
	output
	'''
	if suffix != None :
# 		file_path = "%s/psy_fs.(%d).E-%2.9f_psys-%3.6f_width-%3d_tick-%2.2f.png" % \
		file_path = "%s/psy_fs.(%d).E-%2.9f_psys-%3.6f_width-%3d_tick-%2.3f.png" % \
				(dpath, suffix, E, psys[len(psys) - 1], width, tick)
	else :
# 		file_path = "%s/psy_fs.E-%2.9f_psys-%3.6f_width-%3d_tick-%2.2f.png" % \
		file_path = "%s/psy_fs.E-%2.9f_psys-%3.6f_width-%3d_tick-%2.3f.png" % \
				(dpath, E, psys[len(psys) - 1], width, tick)
		
	print "[%s:%d] file path => %s" % (thisfile(), linenum(), file_path)

	# basename
	file_name = os.path.basename(file_path)
	
	print "[%s:%d] file_name => %s" % (thisfile(), linenum(), file_name)
	
	# dir path
	#ref http://www.gesource.jp/programming/python/code/0009.html
	#ref https://stackoverflow.com/questions/273192/how-can-i-create-a-directory-if-it-does-not-exist "answered Nov 7 '08 at 19:06"
	if not os.path.exists(dpath):
		
		os.makedirs(dpath)

	pyplot.savefig(file_path)
		
	print "[%s:%d] file => saved : '%s'" % (thisfile(), linenum(), file_path)
		
		
	# clear the figure
	#ref https://stackoverflow.com/questions/8213522/when-to-use-cla-clf-or-close-for-clearing-a-plot-in-matplotlib "answered Nov 22 '11 at 14:54"
	pyplot.clf()
 	
	pyplot.close()
		
#]]def psysData_SaveImage(psys, fs, E, width, output = false):


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

def exec_shooting(E, width_, tick_, dpath, flag_Plot = False, flag_SaveImage = False, suffix_=None):
# def exec_shooting(E, width_, tick_, flag_Plot = False, flag_SaveImage = False):
	
	psys, fs = calculate(E, tick=tick_, width=width_)
	
	#ref multiline comment https://stackoverflow.com/questions/7696924/way-to-create-multiline-comments-in-python ""answered Oct 8 '11 at 12:58
	'''
	report ==> last index value
	'''
	print "[%s:%d] psys[%d] = %f" %\
		 (thisfile(), linenum(), len(psys) - 1, psys[len(psys) - 1])

	'''
	Save image
	'''
	if flag_SaveImage == True :
		
		psysData_SaveImage(psys, fs, E, width_, dpath, output=True, tick=tick_, suffix=suffix_)
# 		psysData_SaveImage(psys, fs, E, width_, dpath, output=True, tick=tick_)
# 		psysData_SaveImage(psys, fs, E, width_, dpath, output=True, tick=tick_)
# 		psysData_SaveImage(psys, fs, E, width, dpath, output=True, tick=tick_)
		
	'''
	Plot
	'''
	if flag_Plot == True :
		#plot_PsysData(psys, fs, E, width, output = False)
		output_ = False
# 		
# 		if flag_SaveImage == True : output_ = True
		
		psysData_Plot(psys, fs, E, width_, dpath, output = output_, tick=tick_)
# 		plot_PsysData(psys, fs, E, width_, output = output_, tick=tick_)
	
	
#]]def exec_shooting():
	
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
		
		psysData_Plot(psys, fs, E, width_, output = output_, tick=tick_)
# 		plot_PsysData(psys, fs, E, width_, output = True, tick=tick_)
	# 	plot_PsysData(psys, fs, E, width_, output = False, tick=tick_)

#]]def shooting():
	
def shooting_2():

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

	# dir path
	dpath = "images/images_%s" % get_TimeLabel_Now()

	print "[%s:%d] dpath => %s" % (thisfile(), linenum(), dpath)
	
	

	'''
	Exec : shooting
	'''
# 	exec_shooting(E, width_, tick_, flag_Plot, flag_SaveImage)
	exec_shooting(E, width_, tick_, dpath, flag_Plot, flag_SaveImage)


# 	psys, fs = calculate(E, tick=tick_, width=width_)
# # 	psys, fs = calculate(E, tick=0.1, width=width_)
# # 	psys, fs = calculate(E, tick=0.1)
# # 	psys, fs = calculate(E, tick=0.2)
# # 	psys, fs = calculate(tick=0.2, E = 2.676)
# # 	psys, fs = calculate(tick=0.2)
# # 	psys, fs = calculate()
# 	
# # 	#debug
# # 	a = 10
# # 	max_num = len(psys)
# #  	
# # 	for i in range(max_num - a, max_num) :
# # # 	for i in range(max_num - 1 - a, max_num - 1) :
# # # 	for i in range(max_num / 2, max_num / 2 + 10) :
# #  		
# # 		#ref multiline https://stackoverflow.com/questions/53162/how-can-i-do-a-line-break-line-continuation-in-python "answered Sep 9 '08 at 23:52"
# # 		print "[%s:%d] psys[%d] = %f / fs[%d] = %f" \
# # 				% (thisfile(), linenum(), i, psys[i], i, fs[i])
# 
# 	#ref multiline comment https://stackoverflow.com/questions/7696924/way-to-create-multiline-comments-in-python ""answered Oct 8 '11 at 12:58
# 	'''
# 	report ==> last index value
# 	'''
# 	print "[%s:%d] psys[%d] = %f" %\
# 		 (thisfile(), linenum(), len(psys) - 1, psys[len(psys) - 1])
# 
# 	'''
# 	Plot
# 	'''
# 	if flag_Plot == True :
# 		#plot_PsysData(psys, fs, E, width, output = False)
# 		output_ = False
# 		
# 		if flag_SaveImage == True : output_ = True
# 		
# 		plot_PsysData(psys, fs, E, width_, output = output_, tick=tick_)
# 		plot_PsysData(psys, fs, E, width_, output = True, tick=tick_)
	# 	plot_PsysData(psys, fs, E, width_, output = False, tick=tick_)

#]]def shooting_2():
	
def shooting_3():

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

	if len(opts) > 0 :
		
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

	# dir path
	dpath = "images/images_%s" % get_TimeLabel_Now()

	print "[%s:%d] dpath => %s" % (thisfile(), linenum(), dpath)
	
	

	'''
	Exec : shooting
	'''
	offsets = np.arange(0, 9, 0.1)
# 	offsets = np.arange(0, 2, 0.1)

	count = 1
	
	for n in offsets :
		
		exec_shooting(\
				E + n, width_, tick_, dpath, \
				flag_Plot, flag_SaveImage, suffix_=count)
# 		exec_shooting(E + n, width_, tick_, dpath, flag_Plot, flag_SaveImage)
		
		count += 1

#]]def shooting_3():
	
def shooting_4():

	#ref https://www.tutorialspoint.com/python/python_command_line_arguments.htm
# 	print sys.argv
# 	print sys.argv[1:]

	# variables
	E = None
	
	start = None
	end = None
	tick_ = None
	
	flag_Plot = False
	flag_SaveImage = False

	#test
	opts = get_opt(sys.argv[1:])
	
	print "[%s:%d] opts => " % (thisfile(), linenum()), opts

	if len(opts) > 0 :
		
		for elem in opts :
			
			if elem[0] == '-E' :
				
				#ref https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points "answered Jun 30 '11 at 18:53"
				E = round(float(elem[1]), 9)
# 				E = float(elem[1])
				
				print "[%s:%d] E is now => %.9f" % (thisfile(), linenum(), E)
# 				print "[%s:%d] E is now => %f" % (thisfile(), linenum(), E)

			elif elem[0] == '-s' :
				
				start = round(float(elem[1]), 9)
				
			elif elem[0] == '-e' :
				
				end = round(float(elem[1]), 9)
				
			elif elem[0] == '-t' :
				
				tick_ = round(float(elem[1]), 3)
# 				tick_ = round(float(elem[1]), 2)
				
			elif elem[0] == 'PLOT_GO' :
				
				flag_Plot = True
	
			elif elem[0] == 'SAVE_IMAGE_GO' :
				
				flag_SaveImage = True
	
			
	
	# put value to E
# 	if E == None : E = 2.676
# 	if E == None : E = 10.62

	'''
	Defaults
	'''	
	if start == None : start = 10.62
	if end == None : end = 10.92
	if tick_ == None : tick_ = 0.001

	'''
	E ---> set to 'start'
	'''
	E = start

	'''
	width, directory path
	'''
	width_ = 20
	
# 	tick_ = 0.1

	# dir path
	dpath = "images/images_%s" % get_TimeLabel_Now()

	print "[%s:%d] dpath => %s" % (thisfile(), linenum(), dpath)
	
	'''
	Exec : shooting
	'''
	
# 	#debug
# 	print "[%s:%d] start = %2.9f / end = %2.9f / tick = %1.2f" \
# 			% (thisfile(), linenum(), \
# 			start, end, tick_)

	
	offsets = np.arange(0, end - start, tick_)
# 	offsets = np.arange(0, 2, 0.1)

# 	#debug
# 	print offsets

	count = 1
	
	#debug
	print "[%s:%d] start = %2.9f / end = %2.9f / tick = %1.2f / offsets = %d" \
			% (thisfile(), linenum(), \
			start, end, tick_, len(offsets))

	
	for n in offsets :
 		
		exec_shooting(\
				E + n, width_, tick_, dpath, \
				flag_Plot, flag_SaveImage, suffix_=count)
# 		exec_shooting(E + n, width_, tick_, dpath, flag_Plot, flag_SaveImage)
 		
		count += 1

#]]def shooting_3():
	
if __name__ == '__main__':
	
	shooting_4()
# 	shooting_3()
# 	shooting_2()
# 	shooting()
	
# 	#debug
# 	print "[%s:%d] time label => %s" % (thisfile(), linenum(), get_TimeLabel_Now(string_type="serial", mili=True))
		

else:
	print "no"

#test_4()
