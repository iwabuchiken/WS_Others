#	load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/10_1/10_2-3.splot-with-range.plt"
#	
#	2017/04/16 15:30:40
#	ref: http://www.ss.scphys.kyoto-u.ac.jp/person/yonezawa/contents/program/gnuplot/script.html
#

#set isosamples 50

############################
#
# variables
#
############################
wait = 0.3
count_max = 70
count_init = 20

############################
#
# for loop
#
############################
#ref http://gnuplot.sourceforge.net/docs_4.2/node60.html

set isosamples 50

f(x,y) = exp(-(x*x + y*y) / 2)
#f2(x,y) = exp((x*x + y*y) / 3)   #=> same as "/ 2"
f2(x,y) = exp(-(x*x + y*y) / 5)
#f2(x,y) = exp(-(x*x + y*y) / 3)
#f2(x,y) = -1 * exp(-(x*x + y*y) / 3)
#f2(x,y) = exp(-(x*x + y*y) / -3)

#splot [-5:5][-5:5][0:1] f(x,y)
splot [-5:5][-5:5][0:1] f(x,y), f2(x,y)
#splot [-5:5][-5:5][0:0.5] f(x,y), f2(x,y)


