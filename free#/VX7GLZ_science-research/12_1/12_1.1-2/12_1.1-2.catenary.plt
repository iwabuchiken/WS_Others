#	load "C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\12_1\12_1.1-2\12_1.1-2.catenary.plt"
#	
#       2017/05/07 13:02:30
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

if (exist("n")==0 || n<0) n=0 #変数の初期化

############################
#
# params setup
#
############################
set size ratio 0.2
set samples 256

##### xrange, yrage ##### 
xrange_start = 0
xrange_end = 30

#set xrange [xrange_start : xrange_end]

yrange_start = -2
yrange_end = 4

set yrange [yrange_start : yrange_end]

##### xtics, ytics  ##### 
xtic_value = 1

set xtics xrange_start, xtic_value, xrange_end

ytic_value = 0.5

set ytics yrange_start, ytic_value, yrange_end

##### key, parametric  ##### 
set nokey
set parametric

########## grid ##########
set grid lw 1


########## set terminal : image ##########
#set terminal jpeg  enhanced font "Times" 10 size 600, 240

########## fonts ##########
set tics font 'Times,10'

########## variables ##########
a = 1.0   #=> A(0, a)

########## labels ##########
set ylabel font "Arial,10"

dname_images = "images_20170507_111637"
str_session = "12_1.1-2"
str_time = time("%Y%m%d_%H%M%S")
str_title = "Catenary"

title(n) = sprintf("[%s] %s @%s (a = %1.2f)", str_session, str_title, str_time, a)

outfile(n) = sprintf("%s/%d.jpg", dname_images, n+1000)  #出力ファイル名

set label title(n)  font 'Times,10'  at 0 , 7

set xlabel "theta"
set ylabel "y"

#unset label 
########## set output ##########
#set output outfile(n)

########## formulae ##########
#ex = (x / a)

#f(x) = (a / 2) * ((exp((x / a)) - exp(-(x / a))) / 2)
#f(n) = (a / 2) * ((exp((n / a)) - exp(-(n / a))) / 2)

########## plot ##########
plot\
     (a / 2) * ((exp((x / a)) - exp(-(x / a))) / 2)
#     (a / 2) * ((exp((t / a)) - exp(-(t / a))) / 2)
#     x, f(x) lc rgb "blue"
#     f(x) lc rgb "blue"

############################
#
# animation
#
############################
wait = 0

if (n < 200)  pause wait; n=n+1; reread

n = 0


