#	load "C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\7_1\7_1.TINK-2-.plt"
#	
#       2017/04/25 12:13:53
#
#      ref: http://maxima.sourceforge.net/contrib/maxiplot/maxiplot_en.pdf
#
############################
#
# includes
#
############################
load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/lib_gnuplot/lib.plt"
load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/lib_gnuplot/cons.plt"


############################
# setup ---> animation
############################
if (exist("count") == 0 || count < 0) count = count_init #•Ï”‚Ì‰Šú‰»

if (exist("sequence") == 0 || sequence < 0) sequence = 0 #•Ï”‚Ì‰Šú‰»




set parametric

urange_start = -2 * pi
#urange_end = count * 0.1 * pi
urange_end = urange_start + count * 0.1

set urange [urange_start : urange_end]
#set urange [-2 * pi : count * pi]
#set urange [-2 * pi : 2 * pi]
#set urange [0:2*pi]

#set vrange [-pi:pi]
set vrange [-pi * 2 : pi * 2]
vrange_start = -2 * pi
vrange_end = vrange_start + count * 0.1
#set vrange [vrange_start : vrange_end]


#set isosamples 36,24
set isosamples 40

set hidden3d

#view_X = 75 + count
view_X = 50 + count
view_Y = 15 + count

#set view view_X, view_Y, 1, 1
#set view 75 + count,15 + count, 1, 1
#set view 75,15,1,1
#set view 50, 15, 1,1
#set view 0, 0, 1,1
#set view 5, 5, 1,1
set view 25, 35, 1.5,1

#ref contour http://lowrank.net/gnuplot/plot3d.html
#set contour
#set cntrparam levels 10
set cntrparam levels incremental -1.5, 0.2, 1.5

A_value = 0.5

session_num = "7_1"
title_num = "2-2"
set title sprintf("%s TINK-%s (count = %d / urange = %f, %f / A = %f)", \
          session_num, title_num, count, urange_start, urange_end, A_value)   #=> TINK-3-3

#unset key

#set ticslevel 0
set ticslevel 0.5

#a = 1.0
#a = 0.3 + count * 0.1
#a = 0.1 + count * 0.1
#a = 0.4 + count * 0.01
a = 0.1 + count * 0.01
#a = 0.5

#set title sprintf("6_1-2 TINK-3-3 (count = %d / a = %f)", count, a)   #=> TINK-3-3

x1(u,v)=cos(u)+.5*cos(u)*cos(v)
x1_1(u,v)=cos(u)+ a * cos(u)*cos(v)
#x1_2(u,v)= .5*cos(u)*cos(v)
x1_2(u,v)= A_value + .5*cos(u)*cos(v)


y1(u,v)=sin(u)+.5*sin(u)*cos(v)
y1_1(u,v)=sin(u)+ a *sin(u)*cos(v)
#y1_2(u,v)= .5*sin(u)*cos(v)
y1_2(u,v)= A_value + .5*sin(u)*cos(v)

z1(u,v)=.5*sin(v)

x2(u,v)=1+cos(u)+.5*cos(u)*cos(v)
y2(u,v)=.5*sin(v)
z2(u,v)=sin(u)+.5*sin(u)*cos(v)

#set multiplot

############################
# save image
############################
#ref http://www.math.utk.edu/~vasili/refs/How-to/gnuplot.print.html
set terminal gif

time_label = "20170501_151940"
#time_label = "20170501_142352"
#time_label = "20170501_131530"
#time_label = "20170501_130628"
#time_label = "20170501_125637"
#time_label = "20170501_111009"
#time_label = "20170430_175030"
#time_label = "20170430_174244"
#time_label = "20170430_173728"

serial_string = "2-2"
session_string = "7-1"
set output sprintf("f_TINK-%s_%s/%s.TINK-%s.%s.%02d.gif", \
     serial_string, time_label, session_string, time_label, serial_string, sequence)

set xlabel "x1(u,v)"
set ylabel "y1(u,v)"

set grid lw 1

set xrange [-2:2]
set yrange[-2:2]

#set multiplot

splot x1(u,v), y1(u,v), 0 lt 2, x1_2(u,v), y1_2(u,v), 1 lt 3
#splot x1(u,v), y1(u,v), 0 lt 2, x1_1(u,v), y1_1(u,v), 0 lt 3
#splot x1(u,v), y1(u,v), 0 lt 2
#splot x1_1(u,v), y1_1(u,v), 0 lt 3
#splot x1_1(u,v), y1_1(u,v), 0 lt 2
#splot x1_2(u,v), y1_2(u,v), 0 lt 2

#splot u, v, x1(u,v) lt 1, u, v, y1(u,v) lt 2
#splot u, v, x1(u,v) w pm3d, u, v, y1(u,v) w pm3d
#splot u, v, x1(u,v) w pm3d

#splot u, v, y1(u,v) w pm3d

#splot x1(u,v), y1(u,v), z1(u,v) w pm3d, x2(u,v), y2(u,v), z2(u,v) w pm3d
#splot x1(u,v), y1(u,v), z1(u,v) lt 3, x2(u,v), y2(u,v), z2(u,v) lt 5

############################
#
# animation: loop
#
############################
#wait = 0.1
#count_max = 200
#count_max = 300
count_max = 60

if (count < count_max) pause wait;  count = count + 1; sequence = sequence + 1; reread
