#	load "C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\3_2\rk.plt"
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
k1x = dt*f1(x, y, z)
k1y = dt*f2(x, y, z)
k1z = dt*f3(x, y, z)
k2x = dt*f1(x+k1x/2,y+k1y/2, z+k1z/2)
k2y = dt*f2(x+k1x/2,y+k1y/2, z+k1z/2)
k2z = dt*f3(x+k1x/2,y+k1y/2, z+k1z/2)
k3x = dt*f1(x+k2x/2,y+k2y/2, z+k2z/2)
k3y = dt*f2(x+k2x/2,y+k2y/2, z+k2z/2)
k3z = dt*f3(x+k2x/2,y+k2y/2, z+k2z/2)
k4x = dt*f1(x+k3x,  y+k3y,   z+k3z)
k4y = dt*f2(x+k3x,  y+k3y,   z+k3z)
k4z = dt*f3(x+k3x,  y+k3y,   z+k3z)
x=x+(k1x + 2*k2x + 2*k3x + k4x)/6
y=y+(k1y + 2*k2y + 2*k3y + k4y)/6
z=z+(k1z + 2*k2z + 2*k3z + k4z)/6
print x, y, z
m=m+1
if(m < m_max) reread
m=0

outfile(n) = sprintf("f/%d.jpg",n+10000)  #出力ファイル名
title(n) = sprintf("t = %4.2f",n*dt )  #タイトル名
unset label 
set label title(n)  font 'Times,12'  at -50 , -50 , 55 
set output outfile(n)
splot DATA with line linecolor rgb "blue"

n = n+1
if(n < n_max) reread
n=0

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


