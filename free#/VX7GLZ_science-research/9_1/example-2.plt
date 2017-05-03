set term png size 900, 900

#set output "mandelbrot.png"
set output sprintf("mandelbrot.%s.png",  time("%Y%m%d_%H%M%S"))

set grid
set pm3d map
set size square
set palette defined (0 "#000000", 2 "#c00000", 7 "#ffff00", 9 "#ffffff")
#splot "data.txt" u 1:2:3
splot "data.txt"
