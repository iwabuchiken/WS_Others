set term png size 900, 900

val_cbtics = 0.5
set cbtics val_cbtics
set mcbtics 4

str_time = time("%Y%m%d_%H%M%S")

#set output "mandelbrot.png"
#set output sprintf("mandelbrot.%s.png",  time("%Y%m%d_%H%M%S"))
set output sprintf("mandelbrot.%s.png",  str_time)

set title sprintf("mandelbrot @%s cbtics = %f", str_time, val_cbtics)



set grid
set pm3d map
set size square

#set palette defined (0 "#000000", 2 "#c00000", 7 "#ffff00", 9 "#ffffff")
set palette defined (0 "#000000", 2 "#c00000", 7 "blue", 9 "#ffffff")

splot "data.txt" u 1:2:3
#splot "data.txt"


#set terminal wxt; set output