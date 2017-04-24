#	load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/10_1/10_2-5.splot-with-data-file.plt"
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
wait = 0.001
count_max = 40
count_init = 0.1
count_tick = 0.1
samples_value = 30
############################
#
# for loop
#
############################
#ref http://gnuplot.sourceforge.net/docs_4.2/node60.html

set isosamples samples_value

############################
#
# plot
#
############################
#splot '10_2-5.input.dat'
splot '10_2-5.input.dat' using 2:3:4



