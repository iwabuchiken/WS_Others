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
if (exist("count") == 0 || count < 0) count = count_init #�ϐ��̏�����

if (exist("sequence") == 0 || sequence < 0) sequence = 0 #�ϐ��̏�����

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
set size ratio 1/2
set samples 1024

set xrange [-4*pi : 4*pi]
set yrange [-30 : 40]

set trange [-4*pi : 4*pi]

set xtics -4*pi, pi/4, 4*pi
#set ytics 0, 1, 3

#set nokey
#set parametric

########## grid ##########

set grid lw 1

set terminal jpeg  enhanced font "Times" 20 size 600, 600
set tics font 'Times,18'

if (exist("n")==0 || n<0) n=0 #�ϐ��̏�����

outfile(n) = sprintf("f-2/%d.jpg",n+1000)  #�o�̓t�@�C����

title(n) = sprintf("t = %d",n)  #�^�C�g����


unset label 

########## title ##########
set label title(n)  font 'Times,20'  at 0 , 3.3 


########## output ##########
time_label = "images_20170513_000508"

set output sprintf("%s/16_1-1.%002d.gif", time_label, n)


########## plot ##########
### plot: cycloid, circle, point on the circumference

#ref sum http://www.ss.scphys.kyoto-u.ac.jp/person/yonezawa/contents/program/gnuplot/sum.html
#plot sum [i=1:n] sin(x * n)
plot sum [i=1:n] cos(x * i)

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

#wait = 0.5
wait = 0.0

n_max = 40

if (n < n_max)  pause wait; n=n+1; reread
n = 0

############################
#
# save image
#
############################


#ref http://www.math.utk.edu/~vasili/refs/How-to/gnuplot.print.html
#set terminal gif



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


