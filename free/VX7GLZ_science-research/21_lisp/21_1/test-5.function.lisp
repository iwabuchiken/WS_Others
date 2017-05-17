(defun msg ()
    (print "message"))

(defun conc (a b)
  (format t "~a~a" a b))
;  (print a)
;  (print b))

(msg)

;(conc 'abc 'def)
(terpri t)
(conc "aaa" "bbb")
