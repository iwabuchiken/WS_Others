#	load "C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\4_1\Lorenz_Attractor.plt"
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
if (exist("count") == 0 || count < 0) count = count_init #•Ï”‚Ì‰Šú‰»

if (exist("sequence") == 0 || sequence < 0) sequence = 0 #•Ï”‚Ì‰Šú‰»

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
set terminal jpeg  enhanced font "Times" 20 size 600, 480
set tics font 'Times,12'
set nokey
set ticslevel 0

set xr[-50:50]
set yr[-50:50]
set zr[0:50]

DATA = "Lorenz_Attractor.data"
set print DATA
f1(x, y, z) = -p*x + p*y
f2(x, y, z) = -x*z + r*x - y
f3(x, y, z) = x*y - b*z

p = 10.0
#p = 5.0

r = 28.0
b = 8.0/3.0

#x = 1
x = 2

y = 1
z = 1

dt = 0.01    #ŽžŠÔ‚Ý

n_max = 1000 #ÃŽ~‰æ”
#n_max = 250 #ÃŽ~‰æ”
m_max = 10   #ŠÔˆø‚«”

n=0;
m=0
call "rk.plt"

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


