time_str = strftime("%y%m%d-%H%M%S", time(0)+9*3600)

if (exist("n") == 0 || n < 0) n = 0
#plot sin(x)
#plot for [i=1:5] sin(x*i)*exp(-i)
#plot for [i=1:5] sin(x)*exp(-i)
i = 1

#n_max = 20
#n_max = 40
#n_max = 80
#n_max = 120
#n_max = 300
n_max = 4

set samples 500
#set xrange [-3 : 3]
set xrange [-6*pi : 6*pi]
set yrange [- n_max : n_max]

set grid lw 2
#plot  sin(x), sin(x)*exp(-i)
#plot exp(-1)

set terminal jpeg  enhanced font "Times" 15 size 600, 600

#show time

#ref http://www.gnuplot-cmd.com/chart/time.html
#set time 0, 0.5 # unrecognized option

#ref "Time Series timedata Format Specifiers" http://gnuplot.sourceforge.net/docs_4.2/node274.html
#ref localize time http://www.ss.scphys.kyoto-u.ac.jp/person/yonezawa/contents/program/gnuplot/date.html#time-func
#time_str = strftime("%y%m%d-%H%M%S", time(0)+9*3600)
#time_str = strftime("%y%m%d-%H%M%S", time(0))
time_label = "20171230_103820"
#time_label = "20170719_143118"
#time_label = "20170719_143244"
#time_label = "20170719_144218"
time_label = "20170719_144607"

dname_images = sprintf("images_%s", time_label)
#dname_images = "images_20170719_142533"

#ref https://stackoverflow.com/questions/33958944/make-an-output-directory-in-gnuplot
#dir = sprintf("output1_%s", time_str)
#command = "mkdir " . dir
#system command

outfile = sprintf("images/%s/test_%s.(%d)jpg", dname_images, time_str, n)
#outfile = sprintf("images/%s/test_%s.jpg", dname_images, time_str)
#outfile = sprintf("images/%s/test.jpg", dname_images)
#outfile = sprintf("images/images_20170719_144607/test.jpg")
#outfile = sprintf("images/%s/%s_%02d.jpg", time_label, dname_images, n)
#outfile = sprintf("images/%s_%02d.jpg", dname_images, n)
#outfile = sprintf("images/%s.jpg", strftime("%Y%m%d_%H%M%S", time(0)+9*3600))

set output outfile

###  TIMESTAMP
set timestamp "%y%m%d_%H%M%S" offset 80,20 font "Helvetica"
#set timestamp "%d/%m/%y %H:%M" offset 80,20 font "Helvetica"
#set timestamp "%d/%m/%y %H:%M" offset 80,-2 font "Helvetica"
unset timestamp

#n = 5

str_Title = sprintf("sum of sins : sin(x * %d)", n)

#ref https://stackoverflow.com/questions/22896632/how-to-set-the-current-date-in-the-gnuplot-title
set title str_Title .strftime("%y%m%d-%H%M%S", time(0) + 3600 * 9)
#set title str_Title .strftime("%y%m%d-%H%M%S", time(0))
#set title str_Title .strftime("%a %b %d %H:%M:%S %Y", time(0))


#plot exp(-x), sin(x)
#plot exp(-x) * sin(x), sin(x)
#plot sin(x), sin(x*2)
#plot for [i=1:5] sin(x * i)
#plot sum[i=1:5] sin(x * i)
#plot sum[i=1:5] cos(x * i)
#plot sum[i=1:n] cos(x * i)
plot sum[i=1 : (n + 1)] cos(x * i)

########################
#
# repeat
#
########################
#n_max = 20
#n_max = 210
#wait = 0.5
#wait = 0.1
wait = 0

if (n < n_max)  pause wait; n = n + 1; unset label; reread

n = 0
