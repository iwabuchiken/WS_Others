#	load "C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\18\18_1.(7).sint^n+cost^n.plt"
#	
#       2017/05/14 18:24:32
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
set size ratio 1
set samples 1024
set xrange [-2 : 2]
set yrange [-2 : 2]
#set trange [-2*pi:2*pi]
set trange [-3*pi:3*pi]
set grid lw 1
set parametric

############################
#
# varibles
#
############################
#n_max = 50
n_max = 10
n_denomi = 100.0
wait_window_output = 0.5
wait_file_output = 0.01
#wait = wait_window_output
wait = wait_file_output

if (exist("n")==0 || n<0) n=0 #�ϐ��̏�����

############################
#
# labels
#
############################
#set label sprintf("n = %2.3f", n / 10.0) font 'Times,15'  at 0.5, 1.5   #=> for file output
set label sprintf("n = %2.3f", n) font 'Times,15'  at -1.5, 1.5   #=> for window output

dname_images = "images_20170514_182445"
outfile(n) = sprintf("%s/%d.jpg", dname_images, n*10 + 1000)  #�o�̓t�@�C����

#set xlabel 

#set terminal jpeg  enhanced font "Times" 20 size 600, 600
#set output outfile(n)

############################
#
# plot
#
############################
#plot sin(x + n / 10.0)   #=> for file output, divide n with 10.0

#plot sin(t + n / 10.0), cos(t)   #=> for file output

#plot sin(t)**n, cos(t)   #=> for window output
#plot sin(t)**n, cos(t), cos(t)**n, sin(t) lc "blue"   #=> for window output
#plot sin(t)**n, cos(t)**n   #=> for window output
#plot sin(t)**n, cos(t)*n   #=> for window output
#plot sin(t)*n, cos(t)*n   #=> for window output
#plot sin(t)*n*t, cos(t)*n*t   #=> for window output
#plot sin(t), cos(t)*n*t   #=> for window output
#plot sin(t), cos(t)*sin(t)   #=> for window output
#plot sin(n), cos(t)   #=> for window output
#plot sin(n), cos(t), sin(t), cos(n) lc "blue", cos(n), sin(t)   #=> for window output
#plot sin(t)**t, cos(t)   #=> for window output
#plot sin(t)**(t*n), cos(t)   #=> for window output
#plot sin(t)**(t*n), cos(t)**(t)   #=> for window output
#plot sin(t)**(t*n), cos(t)**(n)   #=> for window output
#plot sin(t), sin(t)**(n)   #=> for window output
#plot sin(t), sin(t*n)   #=> for window output
#plot sin(t), sin(t+n)   #=> for window output
#plot sin(t), sin(t)*sin(n)   #=> for window output
#plot sin(t), sin(t)*sin(n), cos(t), cos(t)*cos(n) lc "blue"   #=> for window output
#plot sin(n), sin(t)*sin(n), cos(n), cos(t)*cos(n) lc "blue"   #=> for window output
#plot sin(t), sin(t)+cos(t+n)   #=> for window output
#plot sin(t), sin(t+n)+cos(t)   #=> for window output
#plot sin(t), sin(t+n)+cos(t), sin(t), sin(t+n)*cos(t) lc "blue"   #=> for window output
#plot cos(t), sin(t)+cos(t + n)   #=> for window output
#plot cos(t) * 2, sin(t)+cos(t + n)   #=> for window output
#plot cos(t) * 2, sin(t)+cos(t + n), cos(t), sin(t)+cos(t + n) lc "blue"  #=> for window output
#plot sin(t), sin(t + n) + cos(t + n)  #=> for window output
#plot sin(t + n), sin(t) + cos(t)  #=> for window output
#plot sin(t + n), sin(t + n) + cos(t)  #=> for window output
#plot sin(t + n), sin(t + n) + cos(t + n)  #=> for window output
#plot cos(t + n), sin(t + n) + cos(t + n)  #=> for window output
#plot sin(t + n), sin(t) * cos(t), cos(t + n), sin(t) * cos(t)  #=> for window output
#plot sin(t)/(3*sin(n)), cos(t)/(3*sin(n)) lc rgb "#aaaaaa", sin(t + n), sin(t) * cos(t), cos(t + n), sin(t) * cos(t)  #=> for window output
#f(x) = (3*sin(x) > 0.5) ? 3*sin(x) : 0.5
#plot sin(t)/f(n), cos(t)/f(n) lc rgb "#aaaaaa", sin(t + n), sin(t) * cos(t), cos(t + n), sin(t) * cos(t)  #=> for window output
#plot sin(t + n), sin(t+n) * cos(t), cos(t + n), sin(t+n) * cos(t)  #=> for window output
plot sin(t + n), sin(t+n) * cos(t + n), cos(t + n), sin(t+n) * cos(t + n)  #=> for window output

#if (n < 5)  pause wait; n = n + 0.01; unset label; reread
#if (n < n_max)  pause wait; n = n + 0.01; unset label; reread
if (n < n_max)  pause wait; n = n + (1 / n_denomi); unset label; reread

n = 0

