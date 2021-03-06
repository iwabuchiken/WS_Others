#	load "C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\15\15_1.(1).gamma.plt"
#	
#       2017/05/11 11:52:30
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

if (exist("n")==0 || n<0) n=0 #変数の初期化

############################
#
# params setup
#
############################
#f(x)=exp(-x**2)  # 被積分関数
#f(x) = x^3 * (1-x)^2

set trange [-5 : 5]

#f(x) = t**(x-1) * (1 - t) ** 2   #=> 'undefined variable: t'
f(x) = x**3 * (1-x)**2   #=> works


#x0=-30   # 積分区間の下限
x0=0   # 積分区間の下限

x1= 300   # 積分区間の上限
#x1= 30   # 積分区間の上限
#N=1000   # 積分区間の分割数
N=900   # 積分区間の分割数

set xrange [x0:x1]
set samples N+1

#ref http://www.ss.scphys.kyoto-u.ac.jp/person/yonezawa/contents/program/gnuplot/integ_func.html
plot lastx=0.0,lasty=0.0,integ = 0.0,\
     "+" using 1:(f($1)) w l lw 3 title "gauss function exp(-x^2)", \
     "+" using 1:(dx=$1-lastx, \
     integ = ($0==0 ? 0.0 : integ+dx*(f($1)+lasty)*0.5), \
     lastx=$1, \
     lasty=f($1), \
     integ) w l lw 3 title "integral"

############################
#
# animation
#
############################
wait = 0

#if (n < 200)  pause wait; n=n+1; reread

n = 0


