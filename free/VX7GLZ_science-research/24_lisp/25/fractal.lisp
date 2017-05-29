;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;                                                                  ;;;
;;;                         fractal.lisp                             ;;;
;;;                  drawing fractal curves using gnuplot            ;;;
;;;                           by T.Shido                             ;;;
;;;                         July 02, 2004                            ;;;
;;;    * Modify hilbert on August 31, 2005                           ;;;
;;;                                                                  ;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

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
	(setq gp (make-pipe-output-stream *gnuplot* :buffered t)))  ;(mark 3a)
    (or dir                                                         ;(mark 3b)
	(setq dir (ext:cd)))
    (let ((dir1 (ext:cd)))
      (unless (equal dir dir1)
	(setq dir dir1)
	(format gp "cd \'~A\'~%" (string-right-trim "\\" (format nil "~A" dir)))
	(force-output gp)))
    (when (stringp s)
      (format gp "~A~%" s)                                           ;(mark 3c)
      (force-output gp)
      (when
	  (string-equal s "exit")
	(close gp)
	(setq gp nil)
	);when
      );when
    );defun gplot
  );let

;;; set autoscale
(defun auto ()                                                       ;(mark 3d)
  (gplot "set autoscale")
  (gplot "replot"))

;;; set range                                                        ;(mark 3e)
(defun range (xmin xmax ymin ymax)
  (and (realp xmin) (realp xmax) (gplot (format nil "set xrange [~A:~A]" xmin xmax)))
  (and (realp ymin) (realp ymax) (gplot (format nil "set yrange [~A:~A]" ymin ymax)))
  (gplot "replot"))

;;; output to png format, give fname without extension                (mark 3f)
(defun png (fname)
  (with-open-file (out "2png.plt" :direction :output)
    (if (system::getenv "GDFONTPATH")
	(format out "set terminal png font \"~A\" ~A size 800, 600~%" *png-font-type* *png-font-size*)
      (format out "set terminal png size 800, 600~%"))
    (format out "set output \"~A.png\"~%" fname)
    (format out "replot~%"))
  (gplot "load \"2png.plt\"")
  (end-plot))

;;; end gnuplot                                                        (mark 3g)
(defun end-plot ()
  (gplot "exit"))

;;; make a flat list
(defun flatten (x)
  (labels ((rec (x acc)
             (cond ((null x) acc)
                   ((atom x) (cons x acc))
                   (t (rec (car x) (rec (cdr x) acc))))))
    (rec x nil))) 

;;;;;;;;;;;;;;; functions for 2D vectors  ;;;;;;;;;;;;;;;;;;;;;;;       (mark 4)
;;; add vectors
(defun v+ (&rest argvs)
  (make-v :x (apply '+ (mapcar #'v-x  argvs))
	  :y (apply '+ (mapcar #'v-y  argvs))))

;;; subtract vectors
(defun v- (&rest argvs)
  (make-v :x (apply '- (mapcar #'v-x  argvs))
	  :y (apply '- (mapcar #'v-y  argvs))))

;;;multiplication or inner product 
(defun v* (v0 n)
    (make-v :x (* (v-x v0) n)
	    :y (* (v-y v0) n)))

;;; square distance between two points
(defun vd2 (v1 v2)
  (let ((dx (- (v-x v1) (v-x v2)))
	(dy (- (v-y v1) (v-y v2))))
    (+ (* dx dx) (* dy dy))))

;;;convert initial input to a list of structure v
(defun l2v (ls0)
  (let (ls1)
    (dolist (c0 ls0 (nreverse ls1))
      (push (make-v :x (first c0) :y (second c0)) ls1))))

;;;vector to string
(defun v2str (vls)
  (apply 'concatenate 'string
         (mapcar #'(lambda (v)
                     (format nil "(~A,~A)," (v-x v) (v-y v)))
                 vls)))

;;;;;;;;;;;;;     C curve and  dragon curve    ;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; plotting the result of calculation of C/dragon
(defun plot-c/dragon (type ls0 ini n)
  (with-open-file (out *fractal-data-file* :direction :output)
    (dolist (v0 ls0)
      (format out "~A ~A~%" (v-x v0) (v-y v0))))
  (with-open-file (out *fractal-plot-file* :direction :output)
    (format out "set title \"~A Curve:\\ninitial coordination = ~S,  Nrep = ~D\"~%" type ini n)
    (format out "set key off~%")
    (format out "set size square~%")
    (format out "set size ratio -1~%")
    (format out "set autoscale~%")
    (format out "plot \"~A\" w l 1~%" *fractal-data-file*))
  (gplot (format nil "load \"~A\"" *fractal-plot-file*))
  t)

;;; making a C curve, (c-curve '((x1 y1) (x2 y2)) n)               ;(mark 5)
(defun c-curve (ls0 n &optional (i 0) ini)
  (if (= i n)
      (plot-c/dragon "C" ls0 ini n)                                ;(mark 5a)
    (let ((ls0a (if (= i 0) (l2v ls0) ls0)))                       ;(mark 5b)
      (labels ((crep (rls0 c0 rls1)                                ;(mark 5c)
		 (if rls0
		     (let* ((c2 (car rls0))
			    (mid (v* (v+ c0 c2) 0.5))
			    (dif (v* (v- c0 c2) (if (evenp i) 0.5 -0.5)))  ;(mark 5d)
			    (c1 (make-v :x (- (v-x mid) (v-y dif))
					:y (+ (v-y mid) (v-x dif)))))
		       (crep (cdr rls0) c2 (cons c1 (cons c0 rls1))))
		   (cons c0 rls1))))
	(c-curve (crep (cdr ls0a) (car ls0a) nil) n (1+ i) (if (zerop i) ls0 ini))))))  ;(mark 5e)

;;; making a dragon curve, (dragon '((x1 y1) (x2 y2)) n)
(defun dragon (ls0 n &optional (i 0) ini)
  (if (= i n)
      (plot-c/dragon "Dragon" ls0 ini n)
    (let ((ls0a (if (= i 0) (l2v ls0)  ls0)))
      (labels ((drep (rls0 c0 rls1 j)
		 (if rls0
		     (let* ((even (evenp (+ i j)))
			    (c2 (car rls0))
			    (mid (v* (v+ c0 c2) 0.5))
			    (dif (v* (v- c0 c2) (if (evenp i) 0.5 -0.5)))
			    (c1 (make-v :x (funcall (if even '+ '-) (v-x mid) (v-y dif))
					:y (funcall (if even '- '+) (v-y mid) (v-x dif)))))
		       (drep (cdr rls0) c2 (cons c1 (cons c0 rls1)) (1+ j)))
		   (cons c0 rls1))))
	(dragon (drep (cdr ls0a) (car ls0a) nil 0) n (1+ i) (if (zerop i) ls0 ini))))))

;;;;;;;;;;;;;;;     hilbert curve   ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;;; plotting the result of hilbert
(defun plot-hilbert (ls ini n)
  (with-open-file (out *fractal-data-file* :direction :output)
    (dolist (gr ls)
      (dolist (v gr)
        (format out "~A ~A~%" (v-x v) (v-y v)))))
  (with-open-file (out *fractal-plot-file* :direction :output)
    (let* ((c (v* (apply 'v+ ini) 0.25))
           (vls (mapcar #'(lambda (v) (v+ c (v* (v- v c) 2.2))) ini)))
      (format out "set title \"Hilbert Curve:\\ninitial coordination = ~A   Nrep = ~D\"~%" (v2str ini) n)
      (format out "set key off~%")
      (format out "set size square~%")
      (format out "set size ratio -1~%")
      (format out "set xrange [~D:~D]~%"
              (apply 'min (mapcar #'v-x vls))
              (apply 'max (mapcar #'v-x vls)))
      (format out "set yrange [~D:~D]~%"
              (apply 'min (mapcar #'v-y vls))
              (apply 'max (mapcar #'v-y vls)))
      (format out "plot \"~A\" w l 1~%" *fractal-data-file*)))
  (gplot (format nil "load \"~A\"" *fractal-plot-file*))
  t)


(defun h-ori (ls)
  (let ((a (first ls))
        (d (fourth ls)))
    (list
     (list (first a) (fourth a) (third a) (second a))
     (second ls)
     (third ls)
     (list (third d) (second d) (first d) (fourth d)))))


(defun hilbert (ls0 n)
  (let ((vls0 (l2v ls0)))
    (labels ((hloop (ls i)
               (if (= i n)
                   (plot-hilbert ls vls0 n)
                 (hloop (h-map ls) (1+ i))))
             (h-map (ls)
               (mapcan #'(lambda (gr)
                           (let ((c (v* (apply 'v+ gr) 0.25)))
                             (h-ori
                              (mapcar #'(lambda (v0)
                                          (mapcar #'(lambda (v) (v+ (v* (v- v c) 0.5) v0))
                                                  gr))
                                      gr))))
                       ls)))
      (hloop (list vls0) 0))))

(defun e1 (ls0 n &optional (i 0) ini)
  (if (= i n)
      (progn
	(print "i == n")
	(print "ls0 =>")
	(print ls0)
	(terpri t)
      );progn
;      (plot-c/dragon "Dragon" ls0 ini n)
    (let
	(
	 (ls0a
	  (if (= i 0) (l2v ls0)  ls0)
	   );(
	  );let(
      	 ;; debug
	 (print "ls0a =>")
	 (print ls0a)

;	 (v- ls0a)
	 (print "(car ls0a) =>")
	 (print (car ls0a))

	 (terpri t)
	 (print "(car (cdr ls0a)) =>")
	 (print (car (cdr ls0a)))

	 ;; ;; (print "(v- (car ls0a) (car (cdr ls0a))) =>")
	 ;; ;; (print (v- (car ls0a) (car (cdr ls0a))))
	 ;; (print
	 ;;  "(v-
	 ;;   (car ls0a)
	 ;;   (car (cdr ls0a))
	 ;;   (car ls0a)
	 ;;      ) =>"
	 ;;  );print
	 ;; (print
	 ;;  (v-
	 ;;   (car ls0a)
	 ;;   (car (cdr ls0a))
	 ;;   (car ls0a)
	 ;;      );v-
	 ;;  );print   ;=> #S(V :X -5 :Y -10)
	 ;; (terpri t)

	 ;;;;;;;;;;;;;;; EXPERI-1 ;;;;;;;;;;;;;;;;;;;;;;
;; ;	 (setq l1 '((car ls0a) (car (cdr ls0a))))   ;=> ((CAR LS0A) (CAR (CDR LS0A)))
;; 	 (setq l1 (list (car ls0a) (car (cdr ls0a))))   ;=> (#S(V :X 1 :Y 3) #S(V :X 5 :Y 10))
;; 	 (print l1)

	 ;; (terpri t)
	 ;; (setq l1-mapcar (mapcar #'v-x l1))
	 ;; (print "(mapcar #'v-x l1) =>")
	 ;; (print l1-mapcar)   ;=> (1 5)
	 ;; (terpri t)

	 ;; (terpri t)
	 ;; (setq l1-mapcar (mapcar #'v-x ls0a))
	 ;; (print "(mapcar #'v-x ls0a) =>")
	 ;; (print l1-mapcar)   ;=> (1 5)
	 ;; (terpri t)

      (labels (
	       (drep (rls0 c0 rls1 j)
      		 (if rls0
      		     (let* (
			    (even (evenp (+ i j));evenp
			      );even
      			    (c2 (car rls0))
      			    (mid (v* (v+ c0 c2) 0.5))
      			    (dif
			     (v*
			      (v- c0 c2);v-
			      (if (evenp i) 0.5 -0.5);if
				);v*
			      );dif
      			    (c1 (make-v :x (funcall (if even '+ '-) (v-x mid) (v-y dif))
      					:y (funcall (if even '- '+) (v-y mid) (v-x dif))
					);make-v
			      );(c1
			    );let* (
      		       (drep (cdr rls0) c2 (cons c1 (cons c0 rls1)) (1+ j)
			     );drep
		       );let*
      		   (cons c0 rls1);cons
		   );if
		 );drep
	       );labels (
      	(e1
;      	(dragon
      	 (drep
      	  (cdr ls0a)   ; rls0
      	  (car ls0a)   ; c0
      	  nil          ; rls1
      	  0            ; j
      	  );drep
      	 n
      	 (1+ i)
      	 (if (zerop i) ls0 ini);if
      		);dragon
      	);labels

      );let
    );if

  ;; debug
  (print "e1 => done")
  
);defun
                              
;; ref http://jtra.cz/stuff/lisp/sclr/labels.html
(defun e2 ()
  (labels
      ((fact2x (x)
	 (fact (* 2 x));fact
	   );fact2x
	   (fact (x)
	     (if
	      (< x 2)
	      1
	      (* x (fact (1- x)));(*
		 );if
	     );fact
       );labels(
    (fact2x 3)
  );labels
  );defun e2

(defun e3 ()
  (labels
      ((msg (x)
	 ;(print x));msg
	 (add-string x));msg
       (add-string (x)
	 (format t "~a and y~%" x));add-string
       );labels(
    (msg "abc");msg   ;=> 'abc and y'
    );labels
  
);defun e3

(defun e4 (&rest args)
  (let ((result ()))
    (print "result =>")
    (print result)

    (print "args =>")
    (print args)(terpri t)

;    (dolist (x args result)
    (dolist (x args (nreverse result))
      (if (evenp x)
	  (progn
	    (format t "~d is even~%" x)
;	    (cons x result)
	    (setq result (cons x result))
	    (print "result =>")
	    (print result)(terpri t)
	    );progn
	  (format t "~d is odd~%" x)
	  );if
      );dolist
    );let
;; ;  (let (result ())
;;   (let ((result ());result
;; 	);let(
;;   (dolist (x args result)
;;     (if (evenp x)+
;; 	(cons x result)
;; 	(format t "~a is not even~%" x)
;; 	);if
;;     );dolist
;; ;	);let (
;;     );let
;  )
);defun e4
