set xrange [-1.5:1.5]
set yrange [0:3.5]
set nokey
set terminal gif animate optimize size 600, 480
set output "tree.gif"
set tics font 'Times,18'
max_n = 30

n=0
load "tree_sub1.plt"
