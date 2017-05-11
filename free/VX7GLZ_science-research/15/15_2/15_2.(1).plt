#	load "C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\15\15_1-2\15_1-2.(1).plt"
#	
#       2017/05/11 22:47:31
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

if (exist("n")==0 || n<0) n=0 #•Ï”‚Ì‰Šú‰»

############################
#
# params setup
#
############################



#set xrange [-0.5:3.5]
#plot "data.dat" u 1:2 title "raw data", \
#     "" u 1:2 smooth unique title "averaged data"

#set xrange [1 : 3]   #=> range for 'p'
#set yrange [1 : 3]   #=> range for 'q'
#set zrange [0 : 1]   #=> range for 't'

#set samples 100
#set isosamples 100
#set pm3d depthorder

#set print "table2-2.dat"
#set table "table2.dat"
#splot 0
#unset table


#set xrange [1 : 3]   #=> range for 'p'
#set yrange [1 : 3]   #=> range for 'q'
#set zrange [0 : 1]   #=> range for 't'

#set samples 100
#set isosamples 100
#set pm3d depthorder

#set table "table2.dat"
#splot 0
#unset table

#plot "table2.dat" using 1:2   #=> works
#splot "table2.dat" using ($1) : ($2) : ($1*$2)   #=> works

#set trange [0 : 1]
set urange [0 : 1]

#splot "table2.dat" using ($1) : ($2) : ($1*$2)   #=> works
#splot "table2.dat" using ($1) : ($2) : (t**$1 * (1-t)**($2-1))

splot "table2.dat" using ($1) : ($2) : (u ** $1 * (1-u)**($2-1))



############################
#
# animation
#
############################
#wait = 0

#if (n < 200)  pause wait; n=n+1; reread

#n = 0


