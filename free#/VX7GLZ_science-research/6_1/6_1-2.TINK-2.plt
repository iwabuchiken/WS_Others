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


set parametric

set urange [-2 * pi : 2 * pi]
#set urange [0:2*pi]

#set vrange [-pi:pi]
set vrange [-pi * 2 : pi * 2]

#set isosamples 36,24
set isosamples 40

set hidden3d
set view 75,15,1,1

#ref contour http://lowrank.net/gnuplot/plot3d.html
#set contour
#set cntrparam levels 10
set cntrparam levels incremental -1.5, 0.2, 1.5

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

splot x1(u,v), y1(u,v), 0 lt 2
#splot u, v, x1(u,v) lt 1, u, v, y1(u,v) lt 2
#splot u, v, x1(u,v) w pm3d, u, v, y1(u,v) w pm3d
#splot u, v, x1(u,v) w pm3d

#splot u, v, y1(u,v) w pm3d

#splot x1(u,v), y1(u,v), z1(u,v) w pm3d, x2(u,v), y2(u,v), z2(u,v) w pm3d
#splot x1(u,v), y1(u,v), z1(u,v) lt 3, x2(u,v), y2(u,v), z2(u,v) lt 5

