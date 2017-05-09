#	load "C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\12_1\12_1.1\12_1.1-1.trochoid"
#	
#       2017/05/07 09:36:54
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

#set xrange [0:15]
#set xrange [0:25]
xrange_start = 0
xrange_end = 30

set xrange [0:30]

#set yrange [0:3]
yrange_start = -2
yrange_end = 4

#set yrange [-3 : 3]
set yrange [yrange_start : yrange_end]

#set trange [0:5*pi]
set trange [0 : 10 * pi]

set xtics 0, 2, 15
set ytics 0, 1, 3
set nokey
set parametric

########## grid ##########
xtic_value = 1
#set xtics 0, xtic_value, 15
set xtics xrange_start, xtic_value, xrange_end

ytic_value = 0.5
#set ytics 0, ytic_value, 3
set ytics yrange_start, ytic_value, yrange_end

set grid lw 1

set terminal jpeg  enhanced font "Times" 10 size 600, 240
#set terminal jpeg  enhanced font "Times" 20 size 600, 240
#set tics font 'Times,18'
set tics font 'Times,10'

set ylabel font "Arial,10"


if (exist("n")==0 || n<0) n=0 #変数の初期化

dname_images = "images_20170507_111637"
#outfile(n) = sprintf("f/%d.jpg",n+1000)  #出力ファイル名
#outfile(n) = sprintf("f-2/%d.jpg",n+1000)  #出力ファイル名
outfile(n) = sprintf("%s/%d.jpg", dname_images, n+1000)  #出力ファイル名

#title(n) = sprintf("t = %d",n)  #タイトル名
#title(n) = sprintf("t = %d (t = %f)",n, t)  #タイトル名

unset label 
#set label title(n)  font 'Times,20'  at 0 , 3.3 
set output outfile(n)

theta = pi/20 * n

#title(n) = sprintf("t = %d / theta = %3.4f",n, theta)  #タイトル名
title(n) = sprintf("t = %d / theta = %3.4f (x = a*t - b*sin(t), y = a - b*cos(t))",n, theta)  #タイトル名

#title(n) = sprintf("t = %d / theta = %f",n, theta)  #タイトル名


fx(t) = t<=theta ? t-sin(t) : 1/0
fy(t) = t<=theta ? 1-cos(t) : 1/0

########## title ##########
#title(n) = sprintf("t = %d (t = %f / theta = %f)",n, t, theta)  #タイトル名
#title(n) = sprintf("t = %d (t = %f / theta = %f / fx(t) = %f)",n, t, theta, fx(t))  #タイトル名   #=> 't' --> 'undefined value'
#set label title(n)  font 'Times,20'  at 0 , 3.3 
#set label title(n)  font 'Times,10'  at 0 , 3.3 
set label title(n)  font 'Times,10'  at 0 , 7

str_session = "12_1.1"
str_time = time("%Y%m%d_%H%M%S")
str_title = "trochoid"
#set title sprintf("<%s / @%s / (a = %d, b = %d) / n = %d>", str_session, str_time, a, b, n)

#set ylabel font "Arial,10"

########## plot ##########
### plot: cycloid, circle, point on the circumference
a = 1; b = 2

set title sprintf("<%s %s / @%s / (a = %d, b = %d) / n = %d>", str_session, str_title, str_time, a, b, n)

set xlabel "theta"
set ylabel "y"

gx(t) = cos(t) + theta
gy(t) = sin(t)+1

hx(t) = t<=theta ? a * t - b * sin(t) : 1/0
hy(t) = t<=theta ? a - b * cos(t) : 1/0

#ref set arrow http://gnuplot.sourceforge.net/demo/lines_arrows.html "set arrow from -500,-100 to 500,-100 as 1"
#set arrow from theta, a to hx(theta), hy(theta) no head lc rgb "red"   #=> 'wrong argument in set arrow'
#set arrow from theta, a to theta, 0 no head lc rgb "red"   #=> 'wrong argument in set arrow'
#set arrow from theta, a to theta, 0 lc rgb "red"   #=> works
set arrow from theta, a to hx(theta), hy(theta) lc rgb "red"   #=> works

plot\
     hx(t), hy(t) w l ,\
     gx(t), gy(t) w l ,\
     hx(theta), hy(theta) with points pt 7 lc rgb "blue"
#     theta, a with points pt 7 lc rgb "red"
#     fx(t),fy(t) w l,\
#     cos(t) + theta, sin(t)+1 w l ,\

#plot\
#     hx(t), hy(t) w l ,\
#     gx(t), gy(t) w l ,\
#     hx(theta), hy(theta) with points pt 7 lc rgb "blue"
##     fx(t),fy(t) w l,\
##     cos(t) + theta, sin(t)+1 w l ,\

### original
#plot fx(t),fy(t) w l,\
#     cos(t)+theta,sin(t)+1 w l ,\
#     fx(theta), fy(theta) with points pt 7 lc rgb "blue"

#plot fx(t),fy(t) w l,\
#     cos(t)+theta,sin(t)+1 w l ,\   #=> the circle : orig
#     fx(theta), fy(theta) with points pt 7 lc rgb "blue"   #=> point on the circumference
     
#     cos(t),sin(t)+1 w l\   #=> cycloid curve
#     cos(t)+theta,sin(t)+1 w l   #=> cycloid curve   #=> orig
#     cos(t)+theta w l   #=> cycloid curve   #=> nothing drawn in the box
#     cos(t)+theta,sin(t)+1 w l    #=> the circle : orig
#     cos(t)+theta,sin(t)+1 w l ,\   #=> the circle : orig
#     fx(theta), fy(theta) with points pt 7 lc rgb "blue"   #=> point on the circumference

#if (n<100)  n=n+1; pause 0.1; reread

#wait = 0.1
wait = 0

#if (n < 100)  n=n+1; reread
#if (n < 200)  n=n+1; reread
if (n < 200)  pause wait; n=n+1; reread

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


