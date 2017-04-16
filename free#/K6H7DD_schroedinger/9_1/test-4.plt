#	load "C:/WORKS_2/WS/WS_Others/free#/K6H7DD_schroedinger/9_1/test-4.plt"
#	
#	2017/04/16 15:50:17
#	ref: http://www.ss.scphys.kyoto-u.ac.jp/person/yonezawa/contents/program/gnuplot/loop.html
#


if (exist("n")==0 || n<0) n=0 #変数の初期化

set samples 1000
set xrange [0:2*pi]
set yrange [-1:1]
plot cos(2*x-2.0*n*pi/30.0)*exp(-0.4*x) title sprintf("n = %d", n)

#if (n<20) pause 0.1; n=n+1; \
#if (n < 40) pause 0.1; n=n+1; \	#=> freeze
if (n<20) pause 0.3; n=n+1; \

          reread        # スクリプトの再読み込み

n=-1
#end of script
