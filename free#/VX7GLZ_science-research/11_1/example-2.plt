############################
# file: C:\WORKS_2\WS\WS_Others\free#\VX7GLZ_science-research\11_1\example-2.plt
# at: 2017/05/05 12:43:38
############################


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


#input_file = "data.20170505_122426.nmax-2000.txt"

set output sprintf("%s.%s.png", input_file, str_time)

#NMAX = 50
#nmax = 2000

set title sprintf("mandelbrot @%s / NMAX = %d", str_time, nmax)   #=> 'nmax' ---> defined in test_popen.rb
#set title sprintf("mandelbrot @%s / NMAX = %d", str_time, NMAX)
#set title sprintf("mandelbrot @%s cbtics = %f", str_time, val_cbtics)
#set title sprintf("mandelbrot / count = %02d / time = %s / view = %d, %d", \
#     count, str_time, view_X, view_Y)



set grid

set pm3d map

set size square

set palette defined (0 "#000000", 2 "#c00000", 7 "#ffff00", 9 "#ffffff")
#set palette defined (0 "#000000", 2 "#c00000", 7 "blue", 9 "#ffffff")

#str_fdst = sprintf("%s.txt", "data.20170504_133655.nmax-1000")


splot input_file u 1:2:3
#splot str_fdst u 1:2:3
#splot str_fdst_trunk ".txt" u 1:2:3
#splot str_fdst_trunk + ".txt" u 1:2:3
#splot "data.txt" u 1:2:3
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
