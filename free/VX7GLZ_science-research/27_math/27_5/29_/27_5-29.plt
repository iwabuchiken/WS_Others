#	original file : load "C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\16\16_1.(1).parametric-sin-sin.plt
#	
#       2017/05/12 11:36:05
#
#   2017/12/31 08:11:29
#   C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\27_math\27_5\13_
#   27_5-13.plt
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
# animation: setup
#
############################
if (exist("count") == 0 || count < 0) count = count_init #変数の初期化

if (exist("sequence") == 0 || sequence < 0) sequence = 0 #変数の初期化

if (exist("n")==0 || n<0) n=0 #変数の初期化

############################
#
# Variables
#
############################
xrange_start = -3
xrange_end = 3

yrange_start = -3
yrange_end = 3

trange_end = pi * 2
trange_start = 0

xtic_value = 0.5
ytic_value = 0.5

time_str = strftime("%y%m%d-%H%M%S", time(0)+9*3600)
dname_images = sprintf("images/images_20180117_094030")


str_session = "27_5.29"
str_time = time("%Y%m%d_%H%M%S")
str_date = time("%Y%m%d")
str_title = "rotation-matrix"

n_denomi = 2.0
n_max = 200

wait = 0.0


a = n / 50.0
b = 1

#x_init = 1 + a
#x_init = a
x_init = -a
y_init = 1

########## parametric ##########
set parametric

############################
#
# Set values
#
############################

set size ratio 1

set samples 256

set xrange [xrange_start : xrange_end]

set yrange [yrange_start : yrange_end]

set trange [trange_start : trange_end]


########## grid ##########
set xtics xrange_start, xtic_value, xrange_end
set ytics yrange_start, ytic_value, yrange_end

set grid lw 1

set terminal jpeg  enhanced font "Times" 10 size 600, 600

set tics font 'Times,10'

set ylabel font "Arial,10"


outfile(n) = sprintf("%s/out_%03d.jpg", dname_images, n)  #出力ファイル名
#outfile(n) = sprintf("%s/test_%s.(%03d).jpg", dname_images, time_str, n)  #出力ファイル名

unset label 

set output outfile(n)

title_label(n) = sprintf("count = %03d",n)  #タイトル名

########## title ##########

set label title_label(n)  font 'Times,10'  at 0.5 , 1.5

########## plot ##########

set title title_label(n)

#set title sprintf("<%s %s / @%s / (a = %d, b = %d) / n = %d>", str_session, str_title, str_time, a, b, n)

set xlabel "x'"
set ylabel "y'"

pow = n / 3
#pow = n / 2

f1(x) = 1 * cos(x) * x_init + 2 * (- sin(x)) * y_init
f2(x) = 1 * sin(x) * x_init + -1 * cos(x) * y_init


plot f1(t), f2(t) lc "blue" lw 1
#plot sin(t), cos(t) lc rgb "#ff5555" lw 1


#if (n < n_max)  pause wait; n = n + 1/n_denomi; reread
if (n < n_max)  pause wait; n = n + 1; reread

n = 0

