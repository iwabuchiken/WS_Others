(setq *WARN-ON-FLOATING-POINT-CONTAGION* nil)
;;; special variables
;(defvar *gnuplot* "C:\\bin\\gnuplot\\bin\\pgnuplot.exe")   ;(mark 1)
(defvar *gnuplot* "C:\\WORKS_2\\Programs\\gnuplot_4.6.7\\bin\\pgnuplot.exe")   ;(mark 1)
(defvar *fractal-data-file* "fractal.dat")
(defvar *fractal-plot-file* "fractal.plt")
(defvar *png-font-type* "Times New Roman")                         ;(mark 1a)
(defvar *png-font-size* 14)                                        ;(mark 1b)

;;; 2D vector
(defstruct v x y)                                                  ; (mark 2)

;;; send command to gnuplot                                        ; (mark 3)
(let (gp dir)
  (defun gplot (s)
    (or gp
	(setq gp (make-pipe-output-stream *gnuplot* :buffered t));setq
	);or  ;(mark 3a)
    (or dir                                                         ;(mark 3b)
	(setq dir (ext:cd)));or
    (let ((dir1 (ext:cd)))
      (unless (equal dir dir1)
	(setq dir dir1)
	(format gp "cd \'~A\'~%" (string-right-trim "\\" (format nil "~A" dir)))
	(force-output gp));unless
      );let
    (when (stringp s)
      (format gp "~A~%" s)                                           ;(mark 3c)
      (force-output gp)
      (when (string-equal s "exit")
	(close gp)
	(setq gp nil)
	);when
      );when
    );defun
  );let

;;; set autoscale
(defun auto ()                                                       ;(mark 3d)
  (gplot "set autoscale")
  (gplot "replot"))

      ;;;;;;;;;;;;;;;; TEST : Section : 4 ;;;;;;;;;;;;;;;;;;;;;;

;;; set range                                                        ;(mark 3e)
(defun range (xmin xmax ymin ymax)
  (and (realp xmin) (realp xmax) (gplot (format nil "set xrange [~A:~A]" xmin xmax)))
  (and (realp ymin) (realp ymax) (gplot (format nil "set yrange [~A:~A]" ymin ymax)))
  (gplot "replot"))

      ;;;;;;;;;;;;;;;; TEST : Section : 4 / TINK-1 ;;;;;;;;;;;;;;;;;;;;;;
(defun any (line)
  (gplot line)
  (gplot "replot"))


      ;;;;;;;;;;;;;;;; TEST : Section : 5 ;;;;;;;;;;;;;;;;;;;;;;

;;; output to png format, give fname without extension                (mark 3f)
(defun png (fname)
  (with-open-file (out "2png.plt" :direction :output)
    (if (system::getenv "GDFONTPATH")
	(format out "set terminal png font \"~A\" ~A size 800, 600~%" *png-font-type* *png-font-size*)
      (format out "set terminal png size 800, 600~%"))
    (format out "set output \"~A.png\"~%" fname)
    (format out "replot~%"))
  (gplot "load \"2png.plt\"")
  (end-plot)
  (format t "png => generated : ~A~%" fname)
  );defun

;;; end gnuplot                                                        (mark 3g)
(defun end-plot ()
  (gplot "exit"))

      ;;;;;;;;;;;;;;;; TEST : Section : 6 ;;;;;;;;;;;;;;;;;;;;;;
;;;multiplication or inner product 
(defun v* (v0 n)
    (make-v :x (* (v-x v0) n)
	    :y (* (v-y v0) n)))

;;;;;;;;;;;;;;;;;;;;;; SANDBOX ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(defun exec_test()
    ;(print "Executing test...")
  (setq v1 (make-v))
  (print "v1 =>")
  (print v1)
  
  ;;; set slot values
  (setf (slot-value v1 'x) 6.73)
  (setf (slot-value v1 'y) 2.21)
  (print "v1 is now =>")
  (print v1)

  ;;; v*
  (setq v2 (v* v1 3.11));setq
  (print "---------- setq v2 (v* v1 3.11)");setq

  (print "v2 => ")
  (print v2)
  
);defun

;(exec_test)


;(gplot "set xrange[-2*pi:2*pi]; plot sin(x)")

(print "done")
