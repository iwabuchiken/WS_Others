#	load "C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\22\22_1.().taylor-expansion-ex.plt"
#	
#       2017/05/15 21:18:21
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
set yrange [-2 : 20]
#set trange [-2*pi:2*pi]
set trange [-3*pi:3*pi]
set grid lw 1
#set parametric

############################
#
# varibles
#
############################
#n_max = 50
n_max = 7
n_denomi = 100.0
wait_window_output = 0.5
wait_file_output = 0.01
wait = wait_window_output
#wait = wait_file_output

if (exist("n")==0 || n<0) n=0 #�ϐ��̏�����

############################
#
# labels
#
############################
#set label sprintf("n = %2.3f", n / 10.0) font 'Times,15'  at 0.5, 1.5   #=> for file output
set label sprintf("n = %2.3f", n) font 'Times,15'  at 0.5, 15   #=> for window output

dname_images = "images_20170515_212756"
outfile(n) = sprintf("%s/%d.jpg", dname_images, n*10 + 1000)  #�o�̓t�@�C����

#set xlabel 

set terminal jpeg  enhanced font "Times" 20 size 600, 600
set output outfile(n)

############################
#
# plot
#
############################
f(n, a) = sum [i=0:a] n**i / i!

plot [0 : 4] f(x, (n+1)), exp(x)
#plot [0 : 4] f(x, 2), exp(x)
#plot sin(x + n / 10.0)   #=> for file output, divide n with 10.0

#plot sin(t + n / 10.0), cos(t)   #=> for file output

#plot sin(t + n), sin(t+n) * cos(t), cos(t + n), sin(t+n) * cos(t)  #=> for window output
#plot sin(t + n), sin(t+n) * cos(t + n), cos(t + n), sin(t+n) * cos(t + n)  #=> for window output



if (n < n_max)  pause wait; n = n + 1; unset label; reread
#if (n < 5)  pause wait; n = n + 0.01; unset label; reread
#if (n < n_max)  pause wait; n = n + 0.01; unset label; reread
#if (n < n_max)  pause wait; n = n + (1 / n_denomi); unset label; reread

n = 0

