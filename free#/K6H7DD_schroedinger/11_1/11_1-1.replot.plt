#	load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/10_1/11_1-1.replot.plt"
#	
#	20170417_163651
#	ref: http://www.ss.scphys.kyoto-u.ac.jp/person/yonezawa/contents/program/gnuplot/script.html
#

#set isosamples 50

############################
#
# includes
#
############################
load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/lib_gnuplot/lib.plt"


############################
#
# variables
#
############################
#wait = 0.001
#count_max = 40
#count_init = 0.1
#count_tick = 0.1
#samples_value = 10

############################
#
# for loop
#
############################
#ref http://www.gnuplot-cmd.com/plot/replot.html

set isosamples samples_value

#ref http://stackoverflow.com/questions/12144714/procedures-in-gnuplot  answered Aug 27 '12 at 15:28
name(x)=sprintf("session %s", x)

#set title name("11-1")
#set title msg("11-1")
set title title_session("11-1")

plot sin(x)

#plot sin(x) lw 3 lt 2
#plot sin(x) linetype 2 linecolor rgbcolor "red" linewidth 1

#p(w)=(plot sin(x) linetype 2 linecolor rgbcolor "red" linewidth )

#plt(w)=(plot sin(x) linetype 2 linecolor rgbcolor "red" linewidth w)

#plt(2)

#p(x)=sin(x)
#p(2)

#replot


