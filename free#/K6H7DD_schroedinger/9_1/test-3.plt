#	load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/9_1/test-3.plt"
#	
#	2017/04/16 15:30:40
#	ref: http://www.ss.scphys.kyoto-u.ac.jp/person/yonezawa/contents/program/gnuplot/instraction.html#script "test.pltをテキストエディタ（xyzzy、秀丸など）"
#


set title "this is test"

set xrange [-20:20]

#plot sin(x)/x
plot sin(x)/(x*2)
