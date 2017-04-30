#	load "C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\6_1\6_1-1.TINK-1.torus-data_x1,y1.plt"
#	
#       2017/04/30 15:29:00
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
#set parametric
set xrange [0:2*pi]
set yrange [-pi:pi]
set zrange [-1:1]

set isosamples 36,24

#set table "6_1-1.TINK-1.table"
#splot 0
#unset table

#exit

set parametric

set hidden3d
#ref " ‰ñ“]1, ‰ñ“]2, ƒOƒ‰ƒt‚ÌŠg‘å—¦, zŽ²‚ÌŠg‘å—¦" http://dsl4.eee.u-ryukyu.ac.jp/DOCS/gnuplot/node128.html
set view 75,15,1,1   #=> original

#unset key
set ticslevel 0

set xrange [-1 : 1]
set yrange [-1 : 1]
set zrange [-1 : 1]

x1(u,v)=cos(u)+.5*cos(u)*cos(v)
y1(u,v)=sin(u)+.5*sin(u)*cos(v)

splot "6_1-1.TINK-1.table" using 1 : 2 : 

#set multiplot

#ref http://www.ss.scphys.kyoto-u.ac.jp/person/yonezawa/contents/program/gnuplot/3D_surface.html
#palette_0 = "dark-blue"
#palette_1 = "cyan"
#set palette defined ( 0 palette_0 , 1 palette_1)
#set palette defined ( 0 "dark-blue" , 1 "cyan")

#ref http://stackoverflow.com/questions/7208665/how-to-export-from-gnuplot-to-extern-datafile-the-frecuency-counts-used-to-gener answered Aug 26 '11 at 19:15
#search https://www.google.co.jp/search?q=gnuplot+splot+write+data&oq=gnuplot+splot+write+data&aqs=chrome..69i64j5l2.6678j0j4&sourceid=chrome&ie=UTF-8#q=gnuplot+write+plot+data

#splot x1(u,v), y1(u,v), z1(u,v) lt 3

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


