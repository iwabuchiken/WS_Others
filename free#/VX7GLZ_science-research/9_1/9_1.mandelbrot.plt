set title "Mandelbrot function"
set isosamples 60
compl(a,b)=a*{1,0}+b*{0,1}
mand(z,a,n) = n<=0 || abs(z)>100 ? 1:mand(z*z+a,a,n-1)+1
splot [-2:1][-1.5:1.5] mand({0,0},compl(x,y),30)
