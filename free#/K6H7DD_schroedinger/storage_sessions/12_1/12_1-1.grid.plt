#	load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/12_1/12_1-1.grid.plt"
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
load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/lib_gnuplot/cons.plt"


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
#name(x)=sprintf("session %s", x)

#set title name("11-1")
#set title msg("11-1")
set title title_session("12_1 grid")

#set xrange[0:2*pi]
set xrange[-2 * pi : 2 * pi]
set yrange[-2.5 : 2.5]

# grid
#set grid lw 1 mytics   #=> grid not shown
#set grid mytics lw 1   #=> grid not shown
set grid xtics ytics mytics lw 1
 
plot tan(x) \
    , sin(x) \
     , sin(x) + tan(x)
#     , sin(x) + tan(x) \
#     , 0 lc rgb "#000000" \
#     , 0.5 lt 1 lc rgb gray dt (10,5) \
#     , 1.0 lt 1 lc rgb gray dt (10,5) \
#     , -1.0 lt 1 lc rgb gray dt (10,5) \
#   , -0.5 lt 1 lc rgb gray dt (10,5)

