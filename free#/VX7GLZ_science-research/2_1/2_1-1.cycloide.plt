#	load "C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\2_1\2_1-1.cycloide.plt"
#	
#       2017/04/25 12:13:53
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
if (exist("count") == 0 || count < 0) count = count_init #変数の初期化

if (exist("sequence") == 0 || sequence < 0) sequence = 0 #変数の初期化

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
set size ratio 0.2
set samples 256
set xrange [0:15]
set yrange [0:3]
set trange [0:5*pi]
set xtics 0, 2, 15
set ytics 0, 1, 3
set nokey
set parametric

set terminal jpeg  enhanced font "Times" 20 size 600, 240
set tics font 'Times,18'

if (exist("n")==0 || n<0) n=0 #変数の初期化
outfile(n) = sprintf("f/%d.jpg",n+1000)  #出力ファイル名
title(n) = sprintf("t = %d",n)  #タイトル名
unset label 
set label title(n)  font 'Times,20'  at 0 , 3.3 
set output outfile(n)

theta = pi/20 * n
fx(t) = t<=theta ? t-sin(t) : 1/0
fy(t) = t<=theta ? 1-cos(t) : 1/0
plot fx(t),fy(t) w l,\
     cos(t)+theta,sin(t)+1 w l ,\
     fx(theta), fy(theta) with points pt 7 lc rgb "blue"

if (n<100)  n=n+1; reread
n = 0

############################
#
# save image
#
############################


#ref http://www.math.utk.edu/~vasili/refs/How-to/gnuplot.print.html
#set terminal gif

time_label = "20170424_132124"

#set output sprintf("image_%s/17_1-1.%s.%002d.gif", time_label, time_label, sequence)


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


