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
xrange_start = 0
xrange_end = pi * 10

yrange_start = -2
yrange_end = 2

trange_end = 60
trange_start = 0

xtic_value = 1
ytic_value = 0.5

time_str = strftime("%y%m%d-%H%M%S", time(0)+9*3600)
dname_images = sprintf("images/images_20171231_074738")


str_session = "16_1.(1)"
str_time = time("%Y%m%d_%H%M%S")
str_date = time("%Y%m%d")
str_title = "sin(ax), cos(ax)"

n_denomi = 2.0
n_max = 40

wait = 0.0


a = 1 + n / 10.0
b = 1

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

set trange [0 : pi * 4]

set xtics 0, 2, 15
set ytics 0, 1, 3

set nokey


########## grid ##########
set xtics xrange_start, xtic_value, xrange_end
set ytics yrange_start, ytic_value, yrange_end

set grid lw 1

set terminal jpeg  enhanced font "Times" 10 size 600, 600

set tics font 'Times,10'

set ylabel font "Arial,10"


#outfile(n) = sprintf("%s/%d.jpg", dname_images, n+1000)  #出力ファイル名
outfile(n) = sprintf("%s/test_%s.(%03d).jpg", dname_images, time_str, n)  #出力ファイル名

unset label 

set output outfile(n)

title(n) = sprintf("count = %02d",n)  #タイトル名

########## title ##########

set label title(n)  font 'Times,10'  at 0.5 , 1.5

########## plot ##########

set title sprintf("[cycloide] n = %d / x = t * %f - sin(t) / y = %d - cos(t)", n, a, b)

#set title sprintf("<%s %s / @%s / (a = %d, b = %d) / n = %d>", str_session, str_title, str_time, a, b, n)

set xlabel "sin(x)"
set ylabel "cos(x)"

pow = n / 3
#pow = n / 2


xval(t) = t * a - sin(t)
#yval(t) = 1 - sin(t)
yval(t) = 1 - cos(t)

plot xval(t), yval(t) lc "blue" lw 1
#plot t - sin(t), 1 - cos(t) lc "blue" lw 1
#plot sin(t) ** pow, cos(t) ** pow lc "blue" lw 1
#plot sin(t), cos(t) lc rgb "#ff5555" lw 1


#if (n < n_max)  pause wait; n = n + 1/n_denomi; reread
if (n < n_max)  pause wait; n = n + 1; reread

n = 0

