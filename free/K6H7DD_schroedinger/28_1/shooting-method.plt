# cd "C:/WORKS_2/WS/WS_Others/free/K6H7DD_schroedinger/28_1"

set yrange[-15:40]
set grid lw 2

#e = 2.67
e = 2.6760079

fname = sprintf("level-1.E-%1.7f.dat", e)

set title fname

#plot "level-1.dat" u 1 with lines lw 3, "level-1.dat" u 2 with lines lw 3
plot fname u 1 with lines lw 3, fname u 2 with lines lw 3
