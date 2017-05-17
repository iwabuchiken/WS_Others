;; ref http://cl-cookbook.sourceforge.net/loop.html "The "return" action both stops the loop"

(let ((s "alpha45"))
  (loop for i from 0 below (length s)
	for ch =  (char s i)
	when (find ch "0123456789" :test #'eql)
	return ch) )

(let ((s "components"))
  
  (format t "length = ~d" (length s))
  (terpri t)
   (format t "s = '~a'" s))

(let ((s "components"))
  (terpri t)
  (loop for i from 0 below (length s)
       for ch = (char s i)
     ;; ref compare char to char : http://clhs.lisp.se/Body/f_chareq.htm
          do (print ch)
             ;(terpri t)
          when (eq ch #\p)
             do
                (print "found")
                (terpri t)
                (format t "chr = '~c' / i = ~d" ch i)))

;                return ch))
             
;       do (format t "ch = '~c'" (char s i))))
;       do (print i)
;       (terpri t)))
;       (format "ch = '~a'" (char s i))))

