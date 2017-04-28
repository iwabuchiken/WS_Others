#	load "C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\5_1\5_1-2.contour.A.plt"
#	
#       2017/04/25 12:13:53
#
#      ref: http://lowrank.net/gnuplot/plot3d.html
#

################## animation setup ##############
if (exist("count") == 0 || count < 0) count = 0 #•Ï”‚Ì‰Šú‰»

#max_count = 20
max_count = 30

if (exist("count_max") == 0 || count_max < 0) count_max = max_count #•Ï”‚Ì‰Šú‰»
#if (exist("count_max") == 0 || count_max < 0) count_max = 12 #•Ï”‚Ì‰Šú‰»

if (exist("sequence") == 0 || sequence < 0) sequence = 0 #•Ï”‚Ì‰Šú‰»
#if (exist("level") == 0 || level < -0.5) level = -0.5 #•Ï”‚Ì‰Šú‰»
if (exist("level") == 0 || level < 0) level = 0 #•Ï”‚Ì‰Šú‰»


a = 1
set xrange [-a*pi : a*pi]
set yrange [-a*pi : a*pi]


tics_level = 0.3
set ticslevel tics_level

sample_level = 80
set isosample sample_level

#view_X = 40 + count * 10
#view_X = 30 + count * 10
span_X = 10
#steps_X = 12
steps_X = 360 / span_X
view_X = 30 + (count % steps_X) * span_X
#if (view_X > 70) view_X = 30

view_Y = 50
set view view_X, view_Y

set contour
set cntrparam levels 5

set title sprintf(" ticslevel = %f / sample = %d / view = (%d %d)", \
     tics_level, sample_level, view_X, view_Y)


############### setup: animation #######################
#ref http://www.math.utk.edu/~vasili/refs/How-to/gnuplot.print.html
set terminal gif

time_label = "20170428_144317"

set output sprintf("images_%s/15_1-2.%s.%002d.gif", time_label, time_label, sequence)


############### plot #######################
#splot (x**2)*(y**2)
#splot sin(x) * cos(y)
splot sin(x) * cos(y) with pm3d


############## animation ####################
#if(count < 10) count = count + 1;  level = level + 0.1; sequence = sequence + 1; reread
#count_max = 12
if(count < count_max) pause 1; count = count + 1;  level = level + 0.1; sequence = sequence + 1; reread

count=0


