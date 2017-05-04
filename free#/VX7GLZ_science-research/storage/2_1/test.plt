
##########################
#
# setup: animation
#
##########################
if (exist("n")==0 || n<0) n=0 #変数の初期化


##########################
#
# meta data
#
##########################
set samples 256
set parametric

multi = 1
#multi = 3
#multi = 2
trange_end = 5*pi * multi
#trange_end = 5*pi
#trange_end = 10*pi

#set size ratio 1.0

set trange [0:trange_end]
#set trange [0:5*pi]
#set trange [0:pi*2]

########## xtics, ytics ##########
#set xtics -1, 0.25, 1
#set xtics -1, 0.25, pi*2
xtic_value = 1
set xtics -1, xtic_value, trange_end
#set xtics -1, 0.25, trange_end
#set ytics -1, 0.25, 1
f2(t) = 1 - cos(t)

ytic_value = 0.5
#set ytics -1, 0.25, f2(pi * 2)   #=> grid not drawn
#set ytics -1, 0.25, 3
set ytics -1, ytic_value, 3

########## xrange, yrange ##########
set xrange [0:trange_end]
#set yrange [0:2]
yrange_end = 3
set yrange [0:yrange_end]
#set yrange [0:3]

#ref http://www.gnuplot-cmd.com/chart/grid.html
set grid lw 1

########## graph size ##########
set size ratio yrange_end / trange_end
#set size ratio 1.0


theta = pi/(20 * multi) * n
#theta = pi/20 * n

########## title ##########
#unset label

#title(n) = sprintf("t = %d (t = %f / theta = %f)",n, t, theta)  #タイトル名

#set label title(n)  font 'Times,20'  at 0 , 3.3 

########## calc ##########
fx(t) = t<=theta ? t-sin(t) : 1/0
fy(t) = t<=theta ? 1-cos(t) : 1/0

##########################
#
# save image
#
##########################
#set terminal jpeg
#set terminal jpeg  enhanced font "Times" 20 size 600, 240
#set tics font 'Times,18'

time_label = "20170425_140319"

outfile(n) = sprintf("images_%s/%d.jpg", time_label, n+1000)  #出力ファイル名

title(n, theta) = sprintf("t = %d / theta = %f",n, theta)  #タイトル名
#title(n) = sprintf("t = %d / theta = %f",n, theta)  #タイトル名
#title(n) = sprintf("t = %d (t = %f)",n, t)  #タイトル名

unset label 
set label title(n, theta)  font 'Times,20'  at 0 , 3.3 
#set label title(n)  font 'Times,20'  at 0 , 3.3 
#set output outfile(n)


##########################
#
# plot
#
##########################
#plot sin(t)
#plot sin(t), cos(t)

#plot t - sin(t), 1 - cos(t)

plot fx(t), fy(t)

##########################
#
# exec: animation
#
##########################
#if (n< 50)  n=n+1 ; reread

#if (n< 100)  n=n+1 ; reread
#if (n< (100 * 3))  n=n+1 ; reread
#if (n< (100 * multi * 2))  n=n+1 ; reread
#if (n<100 * multi)  n=n+1; pause 0.1; reread
if (n<100)  n=n+1; pause 0.05; reread
#if (n<100)  n=n+1; pause 0.1; reread
#if (n<100)  n=n+1; pause 1; reread

n = 0

