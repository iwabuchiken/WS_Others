if (exist("count") == 0 || count < 0) count = 0 #変数の初期化
if (exist("sequence") == 0 || sequence < 0) sequence = 0 #変数の初期化


set xrange[-3*pi : 3*pi]
set yrange[-2 : 2]

set grid lw 1

count_max = 100
#count_max = 10

tick = pi / 10
#tick = pi / count_max

str_session = "19_1"
set title sprintf("%s (count = %02d / tick = %f)", str_session, count, tick)

out_size_x = 1000
out_size_y = 1000

set terminal jpeg  enhanced font "Times" 15 size out_size_x, out_size_y
#set terminal jpeg  enhanced font "Times" 20 size out_size_x, out_size_y
#set terminal jpeg  enhanced font "Times" 20 size 600, 240

#set terminal font "Arial,10"

#ref font size http://www.eng.kagawa-u.ac.jp/~haruna/memo/gnuplot/gnutips.html#font
#set ylabel font "Arial,10"
#set ylabel font "Arial,5"
#set tics font "Arial,5"
#set tics font "Arial,15"

str_datetime = "20170502_173037"

outfile(n) = sprintf("f_%s/%d.jpg",str_datetime, n+1000)  #出力ファイル名

set output outfile(count)

set multiplot layout 4,1
#set multiplot layout 3,1

#set terminal jpeg  enhanced font "Times" 20 size 600, 240



#set output outfile(n)


plot sin(x + tick * count) lc "green", sin(x) lc "blue"
plot sin(x + tick * count) lc "green", sin(x) lc "blue", sin(x + tick * count) + sin(x) lc "red"
plot sin(x + tick * count) lc "green", sin(x + tick * count) + sin(x) lc "red"
plot sin(x + tick * count) + sin(x) lc "red"

#plot sin(x + tick * count)
#plot sin(x)

#ref http://stackoverflow.com/questions/25388994/how-to-output-a-file-in-gnuplot-multiplot-mode answered Aug 19 '14 at 17:29
unset multiplot
unset output

#wait = 0.5
wait = 0

if (count < count_max) pause wait;  count = count + 1; sequence = sequence + 1; reread

count = 0; sequence = 0
