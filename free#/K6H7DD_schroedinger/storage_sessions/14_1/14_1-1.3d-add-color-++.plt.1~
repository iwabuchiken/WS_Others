#	load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/13_1/13_1-2.3d-add-color.animation.plt"
#	
#	2017/04/20 12:04:19
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

set isosamples samples_value

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
#name = sprintf("13-2 : 3d surface color (%02d)", count)
#name = sprintf("13-2 (%02d)", count)
name = sprintf("13-1-2 (%02d)", sequence)

set title title_session(name)
#set title title_session("13-1 3d surface color")
#set title title_session("sin(x)*sin(y)")

set xlabel "x"
set ylabel "y"

a = 3

set xrange [-a*pi:a*pi]
set yrange [-a*pi:a*pi]

#rerf z axis https://www.google.co.jp/url?sa=t&rct=j&q=&esrc=s&source=web&cd=3&cad=rja&uact=8&ved=0ahUKEwiHqqmmnLLTAhXLfbwKHc3KDewQFgg1MAI&url=http%3A%2F%2Fwww.gnuplot-cmd.com%2Faxis%2Frange.html&usg=AFQjCNEcZM3rkh_Kr2hYqmoQuMHNxpaJqg&sig2=bcrPpV2_RHo7-K6nSQXevQ
#set zrange [-1.5:1.5]

set grid lw 1

#splot sin(x + count * 5)*sin(y + count * 5) with pm3d
#splot sin(x)*sin(y) with pm3d

#splot (sin(x + count * 5)) * sin(y + count * 5), (sin(x + count * 5)) * cos(y + count * 5) with pm3d
splot (sin(x + count * 5)) * cos(y + count * 5) with pm3d
#splot (sin(x + count * 5))**2*sin(y + count * 5) with pm3d
#splot (sin(x + count * 5))**2*sin(y + count * 5), sin(x + count * 5)*sin(y + count * 5) with pm3d


############################
#
# save image
#
############################
#ref http://xmodulo.com/how-to-export-gnuplot-output-to-png-jpg-and-pdf.html
#set terminal gif color enhanced

#ref http://www.math.utk.edu/~vasili/refs/How-to/gnuplot.print.html
#set terminal gif

#time_label = "20170420_134828"
time_label = "20170420_140349"

#set output sprintf("image_%s/13_1-2.%s.%002d.gif", time_label, time_label, sequence)

#set output "output.gif"
#set output sprintf("13_1-2.%s.%002d.gif", "20170420_131701", sequence)   #=> working
#set output sprintf("image_%s/13_1-2.%s.%002d.gif", "20170420_131824", "20170420_131824", sequence)


#image_20170420_131824

############################
#
# graph: 2
#
############################

#set title title_session("sin(x)^2*sin(y)")

#replot (sin(x))**2*sin(y) with pm3d
#splot (sin(x))**2*sin(y) with pm3d

############################
#
# animation: loop
#
############################
#if (count < count_max) pause wait;  count = count + count_tick; reread
if (count < count_max) pause wait;  count = count + count_tick; sequence = sequence + 1; reread
#if (count < count_max) pause wait;  count = count + count_tick, sequence = sequence + 1; reread   #=> animation doesn't start

count = count_init


