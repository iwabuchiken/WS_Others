############################
# setup ---> animation
############################
if (exist("count") == 0 || count < 0) count = 0 #•Ï”‚Ì‰Šú‰»

if (exist("sequence") == 0 || sequence < 0) sequence = 0 #•Ï”‚Ì‰Šú‰»


set term png size 900, 900

val_cbtics = 0.5
set cbtics val_cbtics
set mcbtics 4

str_time = time("%Y%m%d_%H%M%S")

########## view ##########
#view_X = count * 10
#view_X = 80
#view_X = 80 + count * 10

#view_Y = 20
#view_Y = 0
#view_Y = 0 + count * 10
#set view view_X, view_Y, 1, 1

#set output "mandelbrot.png"

set output sprintf("mandelbrot.%s.png",  str_time)

#str_timelabel = "20170503_151857"
#str_timelabel = "20170503_155638"
str_timelabel = "20170503_164231"

str_dpath = sprintf("f_SEG-2_TINK-1_%s", str_timelabel)

#set output sprintf("%s/mandelbrot.%s.%02d.png",  str_dpath, str_timelabel, count)

NMAX = 500
set title sprintf("mandelbrot @%s / NMAX = %d", str_time, NMAX)
#set title sprintf("mandelbrot @%s cbtics = %f", str_time, val_cbtics)
#set title sprintf("mandelbrot / count = %02d / time = %s / view = %d, %d", \
#     count, str_time, view_X, view_Y)



set grid

set pm3d map

set size square

#set palette defined (0 "#000000", 2 "#c00000", 7 "#ffff00", 9 "#ffffff")
set palette defined (0 "#000000", 2 "#c00000", 7 "blue", 9 "#ffffff")

splot "data.txt" u 1:2:3
#splot "data.txt"


############################
#
# animation: loop
#
############################
#wait = 0
#count_max = 20
#count_max = 33
#count_max = 28

#if (count < count_max) pause wait;  count = count + 1; sequence = sequence + 1; reread

#count = 0; sequence = 0

#set terminal wxt; set output
#load "C:/WORKS_2/WS/WS_Others/free#/VX7GLZ_science-research/9_1/example-2.plt"
