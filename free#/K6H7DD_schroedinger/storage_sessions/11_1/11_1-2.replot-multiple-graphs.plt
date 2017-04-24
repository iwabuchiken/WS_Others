#	load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/10_1/11_1-2.replot-multiple-graphs.plt"
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
set title title_session("11-2 multiple graphs")

#set xrange[0:2*pi]
set xrange[-4 * pi : 4 * pi]
set yrange[-2.5 : 2.5]

#ref http://www.ss.scphys.kyoto-u.ac.jp/person/yonezawa/contents/program/gnuplot/script.html
set multiplot layout 2,1

plot tan(x) \
     , sin(x) \
     , sin(x) + tan(x) \
     , 0 lc rgb "#000000" \
     , 0.5 lt 1 lc rgb gray dt (10,5) \
     , 1.0 lt 1 lc rgb gray dt (10,5) \
     , -1.0 lt 1 lc rgb gray dt (10,5) \
   , -0.5 lt 1 lc rgb gray dt (10,5)

#replot sin(x)

#replot sin(x) + tan(x) \
#     , 0 lc rgb "#000000" \
#     , 0.5 lt 1 lc rgb gray dt (10,5) \
#     , 1.0 lt 1 lc rgb gray dt (10,5) \
#     , -1.0 lt 1 lc rgb gray dt (10,5) \
#   , -0.5 lt 1 lc rgb gray dt (10,5)

set title title_session("cos + tan")

plot  tan(x) \
     , cos(x) \
     , tan(x) + cos(x) \
     , 0 lc rgb "#000000" \
     , 0.5 lt 1 lc rgb gray dt (10,5) \
     , 1.0 lt 1 lc rgb gray dt (10,5) \
     , -1.0 lt 1 lc rgb gray dt (10,5) \
   , -0.5 lt 1 lc rgb gray dt (10,5)

#plot sin(x)+tan(x) with lines dt (2,6) lc rgb "cyan" lw 3 \
#replot sin(x)+tan(x) with lines dt (2,6) lc rgb "cyan" lw 3 \
#     , 0 lc rgb "#000000" \
#     , 0.5 lt 1 lc rgb gray dt (10,5) \
#     , 1.0 lt 1 lc rgb gray dt (10,5) \
#     , -1.0 lt 1 lc rgb gray dt (10,5) \
#   , -0.5 lt 1 lc rgb gray dt (10,5)


#plot sin(x)+cos(x) with lines dt "_-" lc rgb "green"
#plot sin(x)


#plot sin(x), 0 lc rgb "red"   #=> working
#ref http://d.hatena.ne.jp/yrgnah_yats/20090802/1249188972
#ref http://www.ss.scphys.kyoto-u.ac.jp/person/yonezawa/contents/program/gnuplot/dashtype.html
#plot sin(x), \
#plot sin(x)
#plot tan(x) with lines dt ".-" lc rgb "blue" \
#plot tan(x) with lines dt ".-" lc rgb "blue"   #=> plot window not shown
#     , 0 lc rgb "#000000" \
#     , 0.5 lt 1 lc rgb gray dt (10,5) \
#     , 1.0 lt 1 lc rgb gray dt (10,5) \
#     , -1.0 lt 1 lc rgb gray dt (10,5) \
#    , -0.5 lt 1 lc rgb gray dt (10,5)

#replot cos(x) with lines dt "._"
#replot tan(x) with lines dt ".-" lc rgb "blue"

#replot sin(x)+cos(x) with lines dt "_-" lc rgb "green"
#replot sin(x)+tan(x) with lines dt (2,6) lc rgb "cyan"
#replot cos(x)+tan(x) with lines dt (2,3,2,10) lc rgb "magenta"

#plot sin(x) lw 3 lt 2
#plot sin(x) linetype 2 linecolor rgbcolor "red" linewidth 1

#p(w)=(plot sin(x) linetype 2 linecolor rgbcolor "red" linewidth )

#plt(w)=(plot sin(x) linetype 2 linecolor rgbcolor "red" linewidth w)

#plt(2)

#p(x)=sin(x)
#p(2)

#replot


