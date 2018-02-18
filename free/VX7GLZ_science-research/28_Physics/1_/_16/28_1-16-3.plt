#	original file : load "C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\16\16_1.(1).parametric-sin-sin.plt
#	
#   created at : 2018/02/18 14:38:06
#
#   dir : C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\28_Physics\1_\_16
#   file : 28_1-16.plt
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
#xrange_start = 0
xrange_start = -1
xrange_end = 1
#xrange_start = -2
#xrange_end = 2

yrange_start = -5
yrange_end = 5

trange_end = 60

trange_start = 0

xtic_value = 1
ytic_value = 0.5

time_str = strftime("%y%m%d-%H%M%S", time(0)+9*3600)
dname = "images_20180218_143342"
dpath_Images = sprintf("images/%s", dname)
#dpath_Images = sprintf("images/images_20171231_074738")


str_session = "28 1-16-2"
str_time = time("%Y%m%d_%H%M%S")
str_date = time("%Y%m%d")
str_title = "rotation of circle"

n_denomi = 2.0
#n_max = 10
n_max = 20

wait = 0.5

m = 2 + 0.1 * n

### rotate
rotate = pi / 2

########## parametric ##########
#set parametric

############################
#
# Set values
#
############################

set size ratio 2

set samples 256

set xrange [xrange_start : xrange_end]

set yrange [yrange_start : yrange_end]

set trange [0 : pi]
#set trange [0 : pi * 4]

set xtics -2, 0.5, 2
set ytics -2, 0.5, 2

#set nokey


########## grid ##########
#set xtics xrange_start, xtic_value, xrange_end
#set ytics yrange_start, ytic_value, yrange_end

set grid lw 1

#set terminal jpeg  enhanced font "Times" 10 size 600, 600

set tics font 'Times,10'

set ylabel font "Arial,10"


#outfile(n) = sprintf("%s/%d.jpg", dpath_Images, n+1000)  #出力ファイル名
outfile(n) = sprintf("%s/test_%s.(%03d).jpg", dpath_Images, time_str, n)  #出力ファイル名

unset label 

set output outfile(n)

title(n) = sprintf("count = %02d",n)  #タイトル名

########## title ##########

set label title(n)  font 'Times,10'  at 0.5 , 1.5

########## plot ##########

set title sprintf("[Lorenz conv] n = %d", n)

#set title sprintf("<%s %s / @%s / (a = %d, b = %d) / n = %d>", str_session, str_title, str_time, a, b, n)

set xlabel "x"
set ylabel "y"

########## funcs ##########
#x = 1; y = 1

y(a) = abs(a) <= (1.0 * n/n_max) ? sqrt(1 - a**2) : 1/0
y_(a) = abs(a) <= (1.0 * n/n_max) ? cos(rotate) * a + sin(rotate) * y(a) : 1.0
y_2(a) = abs(a) <= (1.0 * n/n_max) ? cos(rotate) * a + sin(rotate) * y(a) * 3 : 1.0
#y(a) = abs(a) <= (1.0 * n/n_max) ? sqrt(1 - a**2) : 1/0
#y_(a) = abs(a) <= (1.0 * n/n_max) ? cos(pi) * a + sin(pi) * y(a) : 1.0
#y(a) = sqrt(1 - a**2)
#y_(a) = cos(pi) * a + sin(pi) * y(a)
#y_(a) = cos(pi) * y(a)
#y_(a) = cos(pi) * a

#x_(a) = cos(n) * x + sin(n) * y * 1
#y_(a) = -sin(n) * x * 1 + cos(n) * y
#x_(a) = cos(pi) * x + sin(pi) * y * 1
#y_(a) = -sin(pi) * x * 1 + cos(pi) * y
#x_(a) = cos(pi) * sin(a) + sin(pi) * cos(a) * m
#y_(a) = -sin(pi) * sin(a) * m + cos(pi) * cos(a)

########## plot ##########

plot y(x), y_(x), y_2(x)

#plot y(t), y_(t)
#plot y(x), y_(x)
#plot y(x)
#plot x_(t)
#plot sin(t),cos(t)
#plot x_(x), sqrt(1 - x**2)
#plot sqrt(1 - x**2)
#plot sin(x + n)
#plot xval(t), yval(t) lc "blue" lw 1
#plot t - sin(t), 1 - cos(t) lc "blue" lw 1
#plot sin(t) ** pow, cos(t) ** pow lc "blue" lw 1
#plot sin(t), cos(t) lc rgb "#ff5555" lw 1


#if (n < n_max)  pause wait; n = n + 1/n_denomi; reread
if (n < n_max)  pause wait; n = n + 1; reread

n = 0

