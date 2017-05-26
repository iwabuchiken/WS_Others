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


      ;;;;;;;;;;;;;;;; TEST : Section : 7 ;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;; functions for 2D vectors  ;;;;;;;;;;;;;;;;;;;;;;;       (mark 4)
;;; add vectors
(defun v+ (&rest argvs)
  (make-v :x (apply '+ (mapcar #'v-x  argvs))
	  :y (apply '+ (mapcar #'v-y  argvs))))

;;; subtract vectors
(defun v- (&rest argvs)
  (make-v :x (apply '- (mapcar #'v-x  argvs))
	  :y (apply '- (mapcar #'v-y  argvs))))

      ;;;;;;;;;;;;;;;; TEST : Section : 8 ;;;;;;;;;;;;;;;;;;;;;;
;;; making a dragon curve, (dragon '((x1 y1) (x2 y2)) n)
(defun dragon (ls0 n &optional (i 0) ini)
  ;;debug
  (print "--------------- ls0")
  (print "ls0 =>")
  (print ls0)   ;=> ((1 1) (10 10))
  (terpri t)

  ;; (print "ini =>")
  ;; (print ini)   ;=> NIL

  ;; (print "(car ls0) =>")
  ;; (print (car ls0))   ;=> (1 1)

  ;; (print "(car (car ls0))=>")
  ;; (print (car (car ls0)))   ;=> 1

  ;; (print "(car (car (car ls0))) =>")
  ;; (print (car (car (car ls0))))  ;=> *** - CAR: 1 is not a list

  (if (= i n)
      (plot-c/dragon "Dragon" ls0 ini n)
    (let (
	  (ls0a
	   (if
	    (= i 0)
	    (l2v ls0)
	    ls0
	       );if
	    );ls0a   ;; "'((x1 y1)(x2 y2))" ;ref http://www.shido.info/lisp/fractal.html "ƒhƒ‰ƒSƒ“‹Èü‚ð•`‚©‚¹‚é"
	  );let(
      
      ;;debug
      (print "ls0a =>")
      (print ls0a)   ;=> (#S(V :X 1 :Y 1) #S(V :X 10 :Y 10))

      );let
    
    ;; ;;debug
    ;; (print "ls0a =>")
    ;; (print ls0a)


    );if

    ;; ;;debug
    ;; (print "ls0a =>")
    ;; (print ls0a)

  ;; debug : l2v
  (print "(l2v ls0) =>")
  (print (l2v ls0))   ;=> (#S(V :X 1 :Y 1) #S(V :X 10 :Y 10))

  
);defun

;;;convert initial input to a list of structure v
(defun l2v (ls0)
  (let (ls1)
    (dolist (c0 ls0 (nreverse ls1))
      (push (make-v :x (first c0) :y (second c0)) ls1))))


;;;;;;;;;;;;;;;;;;;;;; SANDBOX ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(defun exec_test()
    ;(print "Executing test...")
  (setq v1 (make-v))
  (print "v1 =>")
  (print v1)

;;   (print "v1-x =>")
;; ;  (print v1-x)   ;=> *** - EXEC_TEST: variable V1-X has no value
;;   (print (v1-x v1))
  
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

  ;;; v-
  (print "---------- setq vminus (v- v1 v2)")
  (setq vminus (v- v1 v2))

  (print "vminus =>")
  (print vminus)

;  (print (mapcar #'v-x '(v1 v2)))   ;=> *** - SYSTEM::%STRUCTURE-REF: V1 is not a structure of type V
;  (print (mapcar #'v-x 'v1 v2))   ;=> *** - MAPCAR: A proper list must not end with V1
;  (print (mapcar #'v-x (v1 v2)))   ;=> *** - FUNCALL: undefined function V1
  (print "v1-x =>")
;  (print v1-x)   ;=> *** - EXEC_TEST: variable V1-X has no value
;  (print (v1-x v1))
  (print (v-x v1))

);defun

;(exec_test)


;(gplot "set xrange[-2*pi:2*pi]; plot sin(x)")

(print "done")
