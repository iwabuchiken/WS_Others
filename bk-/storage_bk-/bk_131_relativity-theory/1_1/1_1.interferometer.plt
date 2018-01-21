if (exist("n") == 0 || n < 0) n = 0 #変数の初期化

a = 3
set xrange[-pi*a:pi*a]; set yrange[-2 : 2]

set grid lw 1

#unset key

set sample 500

max = n
#max = 100

str_title = sprintf("interferometer : n = %d", n)
set title str_title

######
#set terminal jpeg  enhanced font "Times" 15 size 600, 600

dname_images = "images_20170610_160826"

outfile(n) = sprintf("images/%s/%03d.jpg", dname_images, n)  #出力ファイル名

#unset label 

#set output outfile(n)



######## plot
A = 0.25

f1(x) = A * sin(x)
f2(x) = A * sin(x + pi / 30 * n)
f3(x) = f1(x) + f2(x)

#plot f1(x), f2(x), f3(x)

plot A * sin(x), A * sin(x + pi / 30 * n), A * sin(x) + A * sin(x + pi / 30 * n)

#plot for[j=1 : max] sum[i=1:j] sin(x + i) 
#plot for[j=1 : 100] sum[i=1:j] sin(x + i) 


n_max = 240
#n_max = 210
wait = 0.1

if (n < n_max)  pause wait; n = n + 1; unset label; reread

n = 0
