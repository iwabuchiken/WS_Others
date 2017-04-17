#	load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/9_1/test-2.plt"
#	
#	2017/04/16 15:30:40
#	ref: http://www.ss.scphys.kyoto-u.ac.jp/person/yonezawa/contents/program/gnuplot/script.html
#


set xrange [0:50]
set samples 500
set xlabel "time (sec)"
set ylabel "amplitude (V)"
set multiplot layout 2,1
theta=0.5*pi
tau=25
set title "test of gnuplot script - oscillation"
plot sin(x) title "input", sin(x-theta) title "output"
set title "test of gnuplot script - dumping oscillation"
plot sin(x) title "input", \
     sin(x-theta)*exp(-x/tau) title "output"
unset multiplot
