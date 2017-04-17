#	load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/10_1/10_2-2.splot-two-graphs.plt"
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

#count = 20

if (exist("count") == 0 || count < 0) count = count_init #•Ï”‚Ì‰Šú‰»

set isosamples count

name = sprintf("isosamples = %d", count)

set title name

#splot x*y
#splot x*y, x + y
splot x + y, x * y

#ref http://www.ss.scphys.kyoto-u.ac.jp/person/yonezawa/contents/program/gnuplot/loop.html
#if (count < 50) pause wait;  count = count + 1; reread
if (count < count_max) pause wait;  count = count + 1; reread

count = 20

#name = "isosamples = 50"
#name = "isosamples = " + count
#ref http://stackoverflow.com/questions/36138334/concatenate-2-strings-in-gnuplot
#name = sprintf("isosamples = %d", count)

#set title name

#splot x*y



