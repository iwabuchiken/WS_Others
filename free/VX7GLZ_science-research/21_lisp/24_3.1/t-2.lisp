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

(print "done")
