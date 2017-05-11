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
if (exist("count") == 0 || count < 0) count = count_init #•Ï”‚Ì‰Šú‰»

if (exist("sequence") == 0 || sequence < 0) sequence = 0 #•Ï”‚Ì‰Šú‰»

if (exist("n")==0 || n<0) n=0 #•Ï”‚Ì‰Šú‰»

############################
#
# params setup
#
############################
#f(x)=exp(-x**2)  # ”íÏ•ªŠÖ”
#f(x) = x^3 * (1-x)^2

set trange [-5 : 5]

#f(x) = t**(x-1) * (1 - t) ** 2   #=> 'undefined variable: t'
f(x) = x**3 * (1-x)**2   #=> works


#x0=-30   # Ï•ª‹æŠÔ‚Ì‰ºŒÀ
x0=0   # Ï•ª‹æŠÔ‚Ì‰ºŒÀ

x1= 300   # Ï•ª‹æŠÔ‚ÌãŒÀ
#x1= 30   # Ï•ª‹æŠÔ‚ÌãŒÀ
#N=1000   # Ï•ª‹æŠÔ‚Ì•ªŠ„”
N=900   # Ï•ª‹æŠÔ‚Ì•ªŠ„”

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


