set xrange[-pi*3:pi*3]
set grid lw 2

#tick = 50

#plot sin(x), sin(x*510/500.0), sin(x*520/500.0)
#plot sin(x), sin(x * (500 + tick) / 500.0), sin(x * (500 + tick * 2) / 500.0)

set sample 1000

plot sum [i=-10:10] sin(x * (500 + 50 * i) / 500.0)   

set xrange[-pi*10:pi*10];replot

