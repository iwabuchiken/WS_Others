set title "Fit function to values stored in an array"
set xtics nomirror

### NOT WORKING ##############################
#ref http://gnuplot.sourceforge.net/demo_cvs/array.html
#array A[100]
#do for [i=1:100] { A[i] = sin(2*pi*i/100.) + 0.1*rand(0) }
#a = b = c = 0.01
#set key title "before fit"
#plot A with points title "Array A", c+cos(a+b*x) with lines
