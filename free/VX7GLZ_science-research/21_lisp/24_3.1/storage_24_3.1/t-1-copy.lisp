(setq *WARN-ON-FLOATING-POINT-CONTAGION* nil)

(defvar *gnuplot* "C:\\WORKS_2\\Programs\\gnuplot_4.6.7\\bin\\pgnuplot.exe")

(let (gp dir)
  (defun gplot (s)
    (or
     (setq gp (make-pipe-output-stream *gnuplot* :buffered t));setq
     );or   ;=> '*** - OR: variable GP has no value'
    (or dir                                                         ;(mark 3b)
	(setq dir (ext:cd)));or
    (let ((dir1 (ext:cd)))
      (unless (equal dir dir1)
	(setq dir dir1)
	(format gp "cd \'~A\'~%" (string-right-trim "\\" (format nil "~A" dir)))
	(force-output gp));unless
      );let
     (when (stringp s)   ;=> *** - WHEN: variable S has no value
       (format gp "~A~%" s)                                           ;(mark 3c)
       (force-output gp)
       (when (string-equal s "exit")
	(close gp)
	(setq gp nil)
	);when
       );when
     );defun
  );let

(defun auto ()                                                       ;(mark 3d)
  (gplot "set autoscale")
  (gplot "replot"));defun


;(print "done")
