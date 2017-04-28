#	load "C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\5_1\5_1-3.multiplot.plt.plt"
#	
#       2017/04/25 12:13:53
#
#      ref: 
#
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

############################
#
# operations
#
############################
#ref http://www.gnuplot-cmd.com/plot/replot.html

#set isosamples samples_value

############################
#
# animation: setup
#
############################
if (exist("count") == 0 || count < 0) count = count_init #•Ï”‚Ì‰Šú‰»

if (exist("sequence") == 0 || sequence < 0) sequence = 0 #•Ï”‚Ì‰Šú‰»
#if (exist("level") == 0 || level < -0.5) level = -0.5 #•Ï”‚Ì‰Šú‰»
if (exist("level") == 0 || level < 0) level = 0 #•Ï”‚Ì‰Šú‰»

############################
#
# graph: 1
#
###########################


############################
#
# params setup
#
############################


########## grid ##########


########## plot ##########
########## range ##########
########################################################
#set term png crop enhanced font "calibri, 10"
#set output "toros.png"
set parametric
set urange [0:2*pi]
set vrange [-pi:pi]
set isosamples 36,24

set hidden3d
set view 75,15,1,1
unset key
set ticslevel 0

x1(u,v)=cos(u)+.5*cos(u)*cos(v)
y1(u,v)=sin(u)+.5*sin(u)*cos(v)
z1(u,v)=.5*sin(v)
x2(u,v)=1+cos(u)+.5*cos(u)*cos(v)
y2(u,v)=.5*sin(v)
z2(u,v)=sin(u)+.5*sin(u)*cos(v)
set multiplot

#splot x1(u,v), y1(u,v), z1(u,v) w pm3d, x2(u,v), y2(u,v), z2(u,v) w pm3d
splot x1(u,v), y1(u,v), z1(u,v) lt 3, x2(u,v), y2(u,v), z2(u,v) lt 5


#count = count + 1

#if(count < 10) pause 1; level = level + 0.1; reread
#if(count < 10) pause 2; level = level + 0.1; sequence = sequence + 1; reread
#if(count < 10)  level = level + 0.1; sequence = sequence + 1; reread

#count=0


############################
#
# save image
#
############################


############################
#
# animation: loop
#
############################
#if (count < count_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread
#if (sequece < sequence_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread

#if (sequence < sequence_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread

#count = count_init
#sequence = sequence_init


