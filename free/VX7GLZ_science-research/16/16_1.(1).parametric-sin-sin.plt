#	load "C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\16\16_1.(1).parametric-sin-sin.plt
#	
#       2017/05/12 11:36:05
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

############################
#
# animation: setup
#
############################
if (exist("count") == 0 || count < 0) count = count_init #変数の初期化

if (exist("sequence") == 0 || sequence < 0) sequence = 0 #変数の初期化

if (exist("n")==0 || n<0) n=0 #変数の初期化

############################
#
# params setup
#
############################
#set size ratio 0.2
set size ratio 1

set samples 256

xrange_start = -2
xrange_end = 2

set xrange [xrange_start : xrange_end]


yrange_start = -2
yrange_end = 2

set yrange [yrange_start : yrange_end]

trange_end = 60
trange_start = 0

set trange [trange_start : trange_end * pi]
#set trange [0 : trange_end * pi]
#set trange [0 : 60 * pi]
#set trange [0 : 30 * pi]
#set trange [0 : 10 * pi]
#set trange [0 : pi * 5]

set xtics 0, 2, 15
set ytics 0, 1, 3
set nokey

########## parametric ##########
set parametric

########## grid ##########
xtic_value = 1
set xtics xrange_start, xtic_value, xrange_end

ytic_value = 0.5
set ytics yrange_start, ytic_value, yrange_end

set grid lw 1

set terminal jpeg  enhanced font "Times" 10 size 600, 600

set tics font 'Times,10'

set ylabel font "Arial,10"



dname_images = "images_20170512_125250"

#outfile(n) = sprintf("%s/%d.jpg", dname_images, n+1000)  #出力ファイル名
outfile(n) = sprintf("%s/%d.jpg", dname_images, n*10 + 1000)  #出力ファイル名

unset label 

set output outfile(n)

theta = pi/20 * n

#title(n) = sprintf("t = %d / theta = %3.4f (x = a*t - b*sin(t), y = a - b*cos(t))",n, theta)  #タイトル名
#title(n) = sprintf("count = %2.2f / sin(t * n), cos(t * n)",n)  #タイトル名
title(n) = sprintf("count = %2.2f",n)  #タイトル名


########## title ##########

#set label title(n)  font 'Times,10'  at 0 , 7
set label title(n)  font 'Times,10'  at 0.5 , 1.5

str_session = "16_1.(1)"
str_time = time("%Y%m%d_%H%M%S")
str_date = time("%Y%m%d")
str_title = "sin(ax), cos(ax)"

########## plot ##########
### plot: cycloid, circle, point on the circumference

n_denomi = 10.0
n_max = 50

#set title sprintf("%s @%s / %s", str_session, str_time, str_title)
#set title sprintf("%s @%s / %s / trange = %d * pi - %d * pi", str_session, str_time, str_title, trange_start, trange_end)
set title sprintf("%s @%s / %s \ntrange = %d * pi - %d * pi / n_denomi = %2.1f / n_max = %d", \
     str_session, str_date, str_title, trange_start, trange_end, n_denomi, n_max)

#set title sprintf("<%s %s / @%s / (a = %d, b = %d) / n = %d>", str_session, str_title, str_time, a, b, n)

set xlabel "sin(x * n)"
set ylabel "cos(x * n)"


#plot sin(x), cos(x)
#plot sin(t), cos(t)

#n = 3
#plot sin(t * 3), cos(t * 3)   #=> plot shown
#plot sin(t * n), cos(t * n) lw (floor(n*10) % 4)   #=> w.
#plot sin(t * n), cos(t * n) lt (floor(n*10) % 4)   #=> w.
plot sin(t * n), cos(t * n) lc "blue"

#plot sin(t + count / 10), cos(t + count / 10)   #=> works; no change?
#plot sin(t + count), cos(t + count)   #=> works; no change?
#plot sin(t * count / 10), cos(t * count / 10)   #=> 



#wait = 0.1
#wait = 0.3
wait = 0.0


if (n < n_max)  pause wait; n = n + 1/n_denomi; reread

#if (n < 50)  pause wait; n = n + 0.5; reread
#if (n < 50)  pause wait; n=n+1; reread
#if (n < 30)  pause wait; n=n+1; reread
#if (n < 200)  n=n+1; reread
#

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

#if (n < 200)  pause wait; n=n+1; reread

#count = count_init
#sequence = sequence_init


+