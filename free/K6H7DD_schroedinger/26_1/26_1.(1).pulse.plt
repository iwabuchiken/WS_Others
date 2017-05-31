if (exist("count") == 0 || count < 0) count = 0

##### setup : plot
set xrange[-pi*3:pi*3]
set grid lw 2

#tick = 50


#plot sin(x), sin(x*510/500.0), sin(x*520/500.0)
#plot sin(x), sin(x * (500 + tick) / 500.0), sin(x * (500 + tick * 2) / 500.0)

set sample 1000

### title
set title sprintf("count = %d", count)

### range
set xrange[-pi*10 : pi*10]

yrange_variance = 800
set yrange[-yrange_variance : yrange_variance]
#set yrange[-30 : 30]

### output
dname_images = "images_20170531_161216"
outfile(n) = sprintf("%s/%d.jpg", dname_images, count * 10 + 1000)

#set terminal jpeg  enhanced font "Times" 20 size 600, 600
set terminal jpeg  enhanced font "Times" 15 size 600, 600
set output outfile(count)


#plot sum [i=-10:10] sin(x * (500 + 50 * i) / 500.0)   
#plot sum [i= - count : count] sin(x * (500 + 50 * i) / 500.0)   
#plot sum [i= - count : count] sin(x * (500 + 10 * i) / 500.0)   
plot sum [i= - count : count] sin(x * (500 + i) / 500.0)   

#set xrange[-pi*10:pi*10];replot


################## reread
#wait = 1.0
wait = 0.01
#n_max  = 10
n_max  = 500
#n_max  = 5

if (count < n_max)  pause wait; count = count + 1; unset label; reread

n = 0

