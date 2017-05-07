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
#set size ratio 1
set samples 256

##### xrange, yrage ##### 
xrange_start = -10
xrange_end = 10

set xrange [xrange_start : xrange_end]

yrange_start = 0
yrange_end = 10
#yrange_end = 15

set yrange [yrange_start : yrange_end]

##### xtics, ytics  ##### 
xtic_value = 1

set xtics xrange_start, xtic_value, xrange_end

ytic_value = 0.5

set ytics yrange_start, ytic_value, yrange_end

##### key, parametric  ##### 
#set nokey
#set parametric

########## grid ##########
set grid lw 1

########## set terminal : image ##########
set terminal jpeg  enhanced font "Times" 10 size 600, 600
#set terminal wxt font "Times" 10

########## fonts ##########
set tics font 'Times,10'

########## variables ##########
#a = 1.0   #=> A(0, a)
a = 1.0 + n * 0.1   #=> A(0, a)

########## labels ##########
set ylabel font "Arial,10"

dname_images = "images_20170507_134739"
str_session = "12_1.1-2"
str_time = time("%Y%m%d_%H%M%S")
str_title = "Catenary"

title(n) = sprintf("[%s] %s @%s \n(a = %1.2f)", str_session, str_title, str_time, a)

#outfile(n) = sprintf("%s/%d.jpg", dname_images, n+1000)  #出力ファイル名
image_file_name = "catenaries"
outfile(n) = sprintf("%s.jpg", image_file_name)  #=> single image output

set label title(n)  font 'Times,10'  at -9 , 8

set xlabel "theta"
set ylabel "y"

########## set output ##########
set output outfile(n)

########## plot ##########
#plot (a / 2) * ((exp((x / a)) - exp(-(x / a))) / 2)

#plot for [i = 0: 5] sin(x + i)

#plot for [i = 1 : 3] exp(i)   #=> not working
#plot for [i = 1 : 3] exp(i)
#plot for [i = 1 : 10] exp(x / (a + i * 0.1)), exp(x / (a + i * 0.1)) + exp(- x / (a + i * 0.1))   #=> Only first formula gets iterated
#plot for [i = 1 : 10]  exp(x / (a + i * 0.1)) + exp(- x / (a + i * 0.1))
i_magnify = 0.3
plot for [i = 1 : 10]  (exp(x / (a + i * i_magnify)) + exp(- x / (a + i * i_magnify))) / 2 * (a + i * i_magnify)

#plot \
#     for [i=1:10] \
#     exp(x), exp(x / (a + i * 0.1)), exp(-x / (a + i * 0.1)), \
#     (exp(x / (a + i * 0.1)) + exp(-x / (a + i * 0.1))), \
#    (exp(x / (a + i * 0.1)) + exp(-x / (a + i * 0.1))) / 2, \
#     (exp(x / (a + i * 0.1)) + exp(-x / (a + i * 0.1))) / 2 * (a + i * 0.1)

#      exp(x), exp(x / a), exp(-x / a), \
#     (exp(x / a) + exp(-x / a)), \
#     (exp(x / a) + exp(-x / a)) / 2, \
#     (exp(x / a) + exp(-x / a)) / 2 * a

#plot sin(x)

############################
#
# animation
#
############################
#wait = 0.5
wait = 0.0   #=> for image files output

n_max = 50

#if (n < n_max)  pause wait; n=n+1; reread

n = 0

