#	load "C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\3_1\3_1-2.multi-plot.sin-cos.plt"
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


########## grid ##########


########## plot ##########
########## range ##########
a = 3
#set xrange [-a * pi : a * pi]
set xrange [0:5 * pi]
#set yrange [-2 : 2]
set yrange [-2 : 2]
set trange [0:5 * pi]
#set xrange [0:5]
#set yrange [-1:1]

########## grid ##########
set grid lw 1

########## multi plot ##########
#set multiplot layout 3,1  #multiplotの開始、縦3横1自動配置
#set multiplot layout 2,1  #multiplotの開始、縦3横1自動配置
set multiplot layout 4,1  #multiplotの開始、縦3横1自動配置

########## plot ##############################
########## plot-1 : sin, cos  ##########
set xlabel "x"
set ylabel "sin(x)/(1-cos(x))"

plot sin(x)/(1-cos(x))

#set xlabel "x"


#plot cos(x) title "plot 1"
#plot cos(x)  lc "red"

#plot cos(x), (1-cos(x))  lc "red", sin(x) lc "blue"

#plot cos(x), (1-cos(x))  lc "red"
#plot cos(t)  lc "red"   #=> 'undefined variable: t'
#plot sin(x)  lc "blue"
#plot sin(t)  lc "blue"

########## plot-2 : velocity (linear)  ##########
set yrange [-5 : 5]
set xlabel "x"
set ylabel "sin(x)/(1-cos(x))"

#velocity = sin(x)/(1-cos(x))   #=> 'undefined variable: x'

plot sin(x)/(1-cos(x)) lc "green"

########## plot-3 : cycloid (parametric)  ##########
set parametric
set yrange [0 : 3]

set xlabel "t-sin(t)"
set ylabel "1-cos(t)"


plot t - sin(t), 1-cos(t)

########## plot-4 : velocity (parametric)  ##########
set parametric

#set xlabel "t"
set xlabel "t - sin(t)"
set ylabel "sin(t)/(1-cos(t))"

set yrange [-3 : 3]
#plot t, velocity
#plot t, sin(t)/(1-cos(t))
plot t - sin(t), sin(t)/(1-cos(t)) lc "red"

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


