#	load "C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\5_1\5_1-3.multiplot.plt.plt"
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

set urange [-2 * pi : 2 * pi]
#set urange [0:2*pi]

#set vrange [-pi:pi]
set vrange [-pi * 2 : pi * 2]

#set isosamples 36,24
set isosamples 40

set hidden3d

#view_X = 75 + count
view_X = 50 + count
view_Y = 15 + count

set view view_X, view_Y, 1, 1
#set view 75 + count,15 + count, 1, 1
#set view 75,15,1,1

#ref contour http://lowrank.net/gnuplot/plot3d.html
#set contour
#set cntrparam levels 10
set cntrparam levels incremental -1.5, 0.2, 1.5

set title sprintf("6_1-2 TINK-3-2 (count = %d / view = %d, %d)", count, view_X, view_Y)

#unset key

#set ticslevel 0
set ticslevel 0.5

x1(u,v)=cos(u)+.5*cos(u)*cos(v)
y1(u,v)=sin(u)+.5*sin(u)*cos(v)
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

time_label = "20170430_175030"
#time_label = "20170430_174244"
#time_label = "20170430_173728"

set output sprintf("f_TINK-3-2/6_1-2.TINK-2.%s.%02d.gif", time_label, sequence)
#set output sprintf("images_%s/6_1-2.TINK-2.%s.%02d.gif", time_label, time_label, sequence)

set xlabel "x1(u,v)"
set ylabel "y1(u,v)"

splot x1(u,v), y1(u,v), 0 lt 2
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
wait = 0
#count_max = 200
count_max = 300
if (count < count_max) pause wait;  count = count + 1; sequence = sequence + 1; reread
