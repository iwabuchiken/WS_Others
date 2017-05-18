(print "test-3.gnuplot.lisp")

(load "fractal")

(gplot "plot sin(x)")

(sleep 3)

;; ref http://clhs.lisp.se/Body/f_sleep.htm
;  (command "pline" )
;  (while (= (logand (getvar "cmdactive") 1) 1)(command pause))


