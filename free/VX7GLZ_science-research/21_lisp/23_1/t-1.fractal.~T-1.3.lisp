;; C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\21_lisp\23_1\t-1.fractal.lisp
;; pushd C:\WORKS_2\WS\WS_Others\free\VX7GLZ_science-research\21_lisp\23_1

;;;;;;;;;;;; TINK-1 ;;;;;;;;;;;;
(print ";;;;;;;;;;;; TINK-1 ;;;;;;;;;;;;")

(defstruct (bar
	     (:constructor create-bar (a b))
	     (:constructor create-bar-x (x &aux (a (* x 10))
	     
					   (b (* x 20))))
	     (:constructor make-bar)
	     )
  a b
  )

(print "(create-bar 1 2) =>")
(print (create-bar 1 2))

(print "(create-bar-x 5) =>")
(print (create-bar-x 5))

(print "(make-bar) =>")
(print (make-bar))

;; (terpri t)
;; ;;;;;;;;;;;; TINK-1.1 &aux ;;;;;;;;;
;; (print ";;;;;;;;;;;; TINK-1.1 &aux ;;;;;;;;;;;;")
;; (terpri t)

;; (let* ((a 10) (b (* a 10)))
;;   (format t "a = ~d, b = ~d~%" a b))
;; ;; (let ((a 10) (b (* a 10)))
;; ;;   (format t "a = ~d, b = ~d~%" a b))	;=> *** - LET: variable A has no value

;; (terpri t)
;; ;;;;;;;;;;;; TINK-1.2 lambda ;;;;;;;;;
;; (print ";;;;;;;;;;;; TINK-1.2 lambda ;;;;;;;;;;;;")
;; (terpri t)

;; ref https://www.tutorialspoint.com/lisp/lisp_lambda_functions.htm
;; (write ((lambda (a b c x)
;;    (+ (* a (* x x)) (* b x) c))
;;    4 2 9 3)
;; )   ;=> 51

;; (terpri t)
;; ;;;;;;;;;;;; TINK-1.2.1 lambda ;;;;;;;;;
;; (print ";;;;;;;;;;;; TINK-1.2.1 lambda ;;;;;;;;;;;;")
;; (terpri t)
;; (do ((x '(1 2 3 4 5) (cdr x))
;;        (y nil))
;; ;    (print x)
;;       ((null x) (reverse y))
;;     (push (+ (car x) 2) y))

;; ;; ref http://www.n-a-n-o.com/lisp/cmucl-tutorials/LISP-tutorial-18.html
;; (do ((x 1 (+ x 1))
;;        (y 1 (* y 2)))
;;       ((> x 5) y)
;;     (print y)
;;     (print 'working)
;;   )

;; (terpri t)
;; ;;;;;;;;;;;; TINK-1.2.2 do ;;;;;;;;;
;; (print ";;;;;;;;;;;; TINK-1.2.2 do ;;;;;;;;;;;;")
;; (terpri t)

;; (do ((x 1 (+ x 1)))
;;     ((> x 5) x)
;;   (print "x is ")
;;   (print x))

;; (terpri t)
;; ;;;;;;;;;;;; TINK-1.2.3 do (cdr) ;;;;;;;;;
;; (print ";;;;;;;;;;;; TINK-1.2.3 do (cdr) ;;;;;;;;;;;;")
;; (terpri t)

;; (do (
;;      (x '(1 2 3 4) (cdr x)) ; x will be --> (1 2 3 4),
;;                             ;  (2 3 4)
;;                             ;  (3 4)
;;                             ;  (4)
;;                             ;  (null)
;;      )
;;     ((null x))
;;   (print "x is")
;;   (print x))

;; (terpri t)
;; ;;;;;;;;;;;; TINK-1.2.4 push ;;;;;;;;;
;; (print ";;;;;;;;;;;; TINK-1.2.4 push ;;;;;;;;;;;;")
;; (terpri t)

;; (setq z '(a b c))
;; (print "z =>")
;; (print z)

;; (push 'x z)
;; (print "z =>")
;; (print z)

;; ;; ref http://www.n-a-n-o.com/lisp/cmucl-tutorials/LISP-tutorial-21.html
;; (do ((x '(1 2 3 4 5) (cdr x)) ; initial value of x is
;;                               ; '(1 2 3 4 5);
;;                               ; At the end of each 
;;                               ; iteration, perfom
;;                               ;(setq x (cdr x))
;;        (y nil))
;;       ((null x) (reverse y)) ; condition is (null x);
;;                              ; when condition met,
;;                              ; return (reverse y)
;;     (print "(car x) =>")
;;     (print (car x))
;;     (push (+ (car x) 2) y) ; push at the top of y
;;                            ; the result of
;;                            ; (car x) + 2
;;     (print "y =>")
;;     (print y)
;;     (print (reverse y))
;;   )


(terpri t)
;;;;;;;;;;;; TINK-1.3 &aux ;;;;;;;;;
(print ";;;;;;;;;;;; TINK-1.3 &aux ;;;;;;;;;;;;")
(terpri t)

;; (write
;;  (
;;  (lambda
;;     (a b &aux (c (car a)))
;;     (list a b c));lambda => lambda function
;;                  ;          defined
;; ; '(aa bb) 'x   ; argument part
;;             ;=> ((AA BB) X AA)
;;  '(aa bb) '(cc dd)   ; argument part
;;                      ;=> ((AA BB) (CC DD) AA)

;;  );(
;; );write

;; ; &aux ‚ÌŽg—p—á
;; ((lambda (a b &aux (c (car a))) (list a b c)) '(10 20) 30)
;; ((10 20) 30 10)

;; (write
;;  ((lambda (a b &aux (c (car a))) (list a b c)) '(10 20) 30)
;; )
;;    ;=> ((10 20) 30 10)

;; (terpri t)

;; (write
;;  (
;;   (lambda (a b &aux c) (list a b c));lambda
;;   '(10 20) 30);(
;; )
;;    ;=> ((10 20) 30 NIL)



;; (write
;;  (
;;   (lambda
;;      (a b c)
;;    (format t "~a ~a ~a~%" a b c)
;;    );lambda
;;  "xxx" "yyy" "zz");(
;;  )   ; xxx yyy zz
;;      ; NIL





;;;;;; eof
(print "done")




