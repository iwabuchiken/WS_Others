#	load "C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\18\18_1.(1).sin-costn.plt
#	
#       20170514_163807
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
#set samples 256

set xrange [-2 : 2]
set yrange [-2 : 2]

set trange [-2*pi:2*pi]
#set trange [0:5*pi]
#set trange [-5*pi:5*pi]

set xtics -1, 0.5, 1
set ytics -1, 0.5, 1

set nokey
set parametric

n_denomi = 100.0
#n_denomi = 10.0
#n_denomi = 30.0
#n_max = 100
#n_max = 50
n_max = 5
#wait = 0.5
wait = 0.1
#wait = 0.0

########## grid ##########

set grid lw 1

set terminal jpeg  enhanced font "Times" 20 size 600, 600

set tics font 'Times,18'

if (exist("n")==0 || n<0) n=0 #�ϐ��̏�����

#outfile(n) = sprintf("f-2/%d.jpg",n+1000)  #�o�̓t�@�C����
dname_images = "images_20170514_163847"

#outfile(n) = sprintf("%s/%d.jpg", dname_images, n+1000)  #�o�̓t�@�C����
outfile(n) = sprintf("%s/%d.jpg", dname_images, n*10 + 1000)  #�o�̓t�@�C����

unset label 

set output outfile(n)

theta = pi/20 * n

title_label(n) = sprintf("t = %2.2f / theta = %2.5f",n, theta)  #�^�C�g����

########## title ##########
#title(n) = sprintf("t = %d (t = %f / theta = %f)",n, t, theta)  #�^�C�g����
#title(n) = sprintf("t = %d (t = %f / theta = %f / fx(t) = %f)",n, t, theta, fx(t))  #�^�C�g����   #=> 't' --> 'undefined value'
set label title_label(n)  font 'Times,10'  at 0.5, 1.5 

#title(n) = sprintf("t = %d",n)  #�^�C�g����
#formula = "sin(t * n), cos(t * n)"
formula = "sin(t), cos(t * n) #"

str_title(n) = sprintf("%s\nt = %2.2f / n_denomi = %2.2f / n_max = %d /wait = %2.2f",\
                    formula, n, n_denomi, n_max, wait)  #�^�C�g����

set title str_title(n)

########## plot ##########
### plot: cycloid, circle, point on the circumference
#plot sin(t), cos(t*2)
#plot sin(t), cos(t*3)
#plot sin(t * n), cos(t * n)
plot sin(t), cos(t * n)
#plot sin(t), cos(t * n), \
#     sin(theta), cos(theta) with points pt 7 lc "blue"
#plot sin(t), sin(t * n) lc "green", \
#     sin(theta), cos(theta) with points pt 7 lc "blue", \
#     sin(t), cos(t * n) lc "red"
#plot sin(t)**2, cos(t)**2 lc "green"
#plot sin(t)**3, cos(t)**3 lc "green"
#plot sin(t)**n, cos(t)**n lc "green"
#plot sin(t)**n/floor(n)!, cos(t)**n/floor(n)! lc "green"

#replot 0.5, 0.5 with points pt 10 lc rgb "red"

if (n < n_max)  pause wait; n = n + 1/n_denomi; reread

n = 0

