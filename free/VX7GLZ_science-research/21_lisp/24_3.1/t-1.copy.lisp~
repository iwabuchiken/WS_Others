(defvar *gnuplot* "C:\\WORKS_2\\Programs\\gnuplot_4.6.7\\bin\\pgnuplot.exe")

(let (gp dir)
  ;; (print gp)   ;=> NIL
  ;; (terpri t)
  (defun gplot (s)
    (or
					;gp
     (setq gp (make-pipe-output-stream *gnuplot* :buffered t));setq
					;gp
     );or   ;=> '*** - OR: variable GP has no value'
    (print "gp => ")
    (print gp)   ;=> #<OUTPUT BUFFERED PIPE-OUTPUT-STREAM CHARACTER 1124>

    (or dir                                                         ;(mark 3b)
	(setq dir (ext:cd)));or
;    (print "dir => ")(print dir)   ;=> #P"C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research\\21_lisp\\24_3.1\\"

    (let ((dir1 (ext:cd)))
      ;; (print "dir1 => ")
      ;; (print dir1)

      ;;;;;;;;;;;;;;;; TEST : Section : 2 ;;;;;;;;;;;;;;;;;;;;;;
      ;; (terpri t)
      ;; (print "dir1 in string => ")
      ;; (print (namestring dir1))

      (unless (equal dir dir1)
	(setq dir dir1)
	(format gp "cd \'~A\'~%" (string-right-trim "\\" (format nil "~A" dir)))
	(force-output gp));unless


      ;(string-right-trim "\\" dir1)
      ;=> *** - SYSTEM::STRING-BOTH-TRIM: argument
      ;; #P"C:\\WORKS_2\\WS\\WS_Others\\free\\VX7GLZ_science-research\\21_lisp\\24_3.1\\" should be a
      ;; string, a symbol or a character

;;       ;; ref http://opamp.hatenablog.jp/entry/2015/01/30/024616
;;       (print
;;        (make-pathname
;; 	:directory '(:absolute "var" "log")
;; 	:name "pacman"
;; 	:type "log");make-...
;;        );print   ;=> '#P"\\var\\log\\pacman.log"'

;;       (print "no 'absolute' keyword...")
;;       (print
;;        (make-pathname
;; ;	:directory '("var" "log")   ;=> *** - MAKE-PATHNAME: Illegal :DIRECTORY argument ("var" "log")
;; 	:directory '(:relative "var" "log")   ;=> #P"var\\log\\pacman.log" (NOTICE : no separator char at the head)
;; 	:name "pacman"
;; 	:type "log");make-...
;;        );print   ;=> '#P"\\var\\log\\pacman.log"'
      
      );let

     (when (stringp s)   ;=> *** - WHEN: variable S has no value
       (format gp "~A~%" s)                                           ;(mark 3c)
       (force-output gp)
       (when (string-equal s "exit")
	(close gp)
	(setq gp nil));when

       );when
);defun
  );let

;(setq gp)   ;=> *** - SETQ: odd number of arguments: (GP)

      ;;;;;;;;;;;;;;;; TEST : Section : 3 ;;;;;;;;;;;;;;;;;;;;;;
;; (print "gplot => ")
;; (print gplot)   ;=> *** - EVAL: variable GPLOT has no value
(defun auto ()                                                       ;(mark 3d)
  (gplot "set autoscale")
  (gplot "replot"));defun


(print "done")
