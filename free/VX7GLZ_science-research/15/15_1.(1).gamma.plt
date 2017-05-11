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
if (exist("count") == 0 || count < 0) count = count_init #�ϐ��̏�����

if (exist("sequence") == 0 || sequence < 0) sequence = 0 #�ϐ��̏�����

if (exist("n")==0 || n<0) n=0 #�ϐ��̏�����

############################
#
# params setup
#
############################
#f(x)=exp(-x**2)  # ��ϕ��֐�
#f(x) = x^3 * (1-x)^2

set trange [-5 : 5]

#f(x) = t**(x-1) * (1 - t) ** 2   #=> 'undefined variable: t'
f(x) = x**3 * (1-x)**2   #=> works


#x0=-30   # �ϕ���Ԃ̉���
x0=0   # �ϕ���Ԃ̉���

x1= 300   # �ϕ���Ԃ̏��
#x1= 30   # �ϕ���Ԃ̏��
#N=1000   # �ϕ���Ԃ̕�����
N=900   # �ϕ���Ԃ̕�����

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


