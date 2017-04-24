#	load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/10_1/10_2-6.splot-with-style.animation.plt"
#	
#	20170417_163651
#	ref: http://www.ss.scphys.kyoto-u.ac.jp/person/yonezawa/contents/program/gnuplot/script.html
#

#set isosamples 50

############################
#
# variables
#
############################
wait = 0.001
count_max = 40
count_init = 0.1
count_tick = 0.1
samples_value = 10

############################
#
# for loop
#
############################
#ref http://gnuplot.sourceforge.net/docs_4.2/node60.html

set isosamples samples_value

if (exist("count") == 0 || count < 0) count = count_init #•Ï”‚Ì‰Šú‰»

name = sprintf("count = %f", count)
#name = sprintf("count = %d", count)

set title name

f(x,y) = exp(-(x*x + y*y) / 2)

f2(x,y) = exp(-(x*x + y*y) / count)

#splot [-5:5][-5:5][0:1] f(x,y), f2(x,y) with points   #=> working
splot [-5:5][-5:5][0:1] f(x,y), f2(x,y) with dots   #=> working
#splot [-5:5][-5:5][0:1] f(x,y), f2(x,y) with filledcurves x1   #=> graph not changing
#splot [-5:5][-5:5][0:1] f(x,y) with dots, f2(x,y) with dots   #=> plot window not shown
#splot [-5:5][-5:5][0:1] f(x,y), f2(x,y)
#splot [-5:5][-5:5][0:1] f(x,y)     #=> f and f2 plotted alternatingly (not simulataneious)
#splot [-5:5][-5:5][0:1] f2(x,y)

if (count < count_max) pause wait;  count = count + count_tick; reread

count = count_init


#f(x,y) = exp(-(x*x + y*y) / 2)
#f2(x,y) = exp((x*x + y*y) / 3)   #=> same as "/ 2"
#f2(x,y) = exp(-(x*x + y*y) / count)

#splot [-5:5][-5:5][0:1] f(x,y)
#splot [-5:5][-5:5][0:1] f(x,y), f2(x,y)
#splot [-5:5][-5:5][0:0.5] f(x,y), f2(x,y)



