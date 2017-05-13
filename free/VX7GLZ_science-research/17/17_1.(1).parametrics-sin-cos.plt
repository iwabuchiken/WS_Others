#	load "C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\17\17_1.(1).parametrics-sin-cos.plt"
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
set size ratio 1
set samples 256

set xrange [-2 : 2]
set yrange [-2 : 2]

set trange [0:5*pi]
#set trange [-5*pi:5*pi]

set xtics -1, 0.5, 1
set ytics -1, 0.5, 1

set nokey
set parametric

#n_denomi = 10.0
n_denomi = 30.0
n_max = 50
wait = 0.1

########## grid ##########

set grid lw 1

#set terminal jpeg  enhanced font "Times" 20 size 600, 240
set tics font 'Times,18'

if (exist("n")==0 || n<0) n=0 #変数の初期化

outfile(n) = sprintf("f-2/%d.jpg",n+1000)  #出力ファイル名

unset label 

#set output outfile(n)

theta = pi/20 * n

title_label(n) = sprintf("t = %2.1f / theta = %f",n, theta)  #タイトル名


#fx(t) = t<=theta ? t-sin(t) : 1/0
#fy(t) = t<=theta ? 1-cos(t) : 1/0
f(t) = t<=theta ? sin(t) : 1/0
g(t) = t<=theta ? cos(t) : 1/0

f2(t) = t<=theta ? sin(t * n) : 1/0
g2(t) = t<=theta ? cos(t * n) : 1/0

########## title ##########
#title(n) = sprintf("t = %d (t = %f / theta = %f)",n, t, theta)  #タイトル名
#title(n) = sprintf("t = %d (t = %f / theta = %f / fx(t) = %f)",n, t, theta, fx(t))  #タイトル名   #=> 't' --> 'undefined value'
set label title_label(n)  font 'Times,10'  at 0.5, 1.5 

#title(n) = sprintf("t = %d",n)  #タイトル名
str_title(n) = sprintf("t = %2.1f / n_denomi = %2.1f / n_max = %d / wait = %2.1f",\
                    n, n_denomi, n_max, wait)  #タイトル名

set title str_title(n)

########## plot ##########
### plot: cycloid, circle, point on the circumference
plot\
     f(t), g(t) w l lc rgb "#44ff44",\
     f2(t), g2(t) w l lc rgb "#555555", \
     f2(theta), g2(theta) with points pt 7 lc rgb "red", \
     f(theta), g(theta) with points pt 7 lc rgb "blue"

#replot 0.5, 0.5 with points pt 10 lc rgb "red"

if (n < n_max)  pause wait; n = n + 1/n_denomi; reread

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


