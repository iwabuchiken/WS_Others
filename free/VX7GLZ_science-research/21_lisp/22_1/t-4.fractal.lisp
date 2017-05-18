(setq L1 '(1 2 3 4 5))

(setq L2 '(6 7 8 9 10))

(write-line "L1")

(print L1)				; (1 2 3 4 5)

(mapcar #'+ L1 L2)

(setq res (mapcar #'+ L1 L2))

(print res)				;(7 9 11 13 15)

;;;;; experiment : defstruct ;;;;;
(defstruct v (x 0.0 :type single-float) (y 0.0 :type single-float)) 

(setq vlist '(1.1 2.2 3.3))

;(mapcar #'v-x vlist)   ;=> n.w.
;(mapcar #'v-x '('(1.1) '(2.2)))   ;=> n.w.
;(mapcar #'v-x '((1.1) (2.2)))   ;=> n.w.
;(mapcar #'v-x '((x 1.1) (y 2.2)))   ;=> n.w. '*** - SYSTEM::%STRUCTURE-REF: (X 1.1) is not a structure of type V'

;; ref http://www.geocities.jp/m_hiroi/xyzzy_lisp/abclisp09.html "defstruct はデータ型を定義して"
(defstruct foo (a 10) (b nil) c)

(setq z1 (make-foo))
(print z1)   ;=> #S(FOO :A 10 :B NIL :C NIL)

(setq z2 (make-foo :b 20 :c 30))
(print "z2 => ")
(print z2)

(print "(foo-a z1) =>")
(print (foo-a z1))
(print "(* (foo-a z1) (foo-b z1)) =>")
(print (* (foo-a z2) (foo-b z2)))

(print "----------------")
(setf (foo-a z1) 100)
(print "(foo-a z1) =>")
(print (foo-a z1))

;;;;;;;;;;;; TINK-5.1 ;;;;;;;;;;;;
(print ";;;;;;;;;;;; TINK-5.1 ;;;;;;;;;;;;")

(defstruct (bar
	     (:conc-name get-)
	     (:constructor create-bar))
		
		(a 10) (b 20))

(setq z1 (create-bar))
(print "z1 =>")
(print z1)

(print "(get-b z1) => ")
(print (get-b z1))

;;;;;;;;;;;; TINK-5.2 ;;;;;;;;;;;;
(print ";;;;;;;;;;;; TINK-5.2 ;;;;;;;;;;;;")

(defstruct foo (a 10) (b 20))

(defstruct (bar
	     (:include foo)
	     )
		
		(c 30))

(setq z1 (make-foo))
(setq z2 (make-bar))

(print "(foo-a z1) =>")
(print (foo-a z1))
(print "(bar-a z2) =>")
(print (bar-a z2))

;(print "(foo-c z1) =>")
;(print (foo-c z1))			;'*** - EVAL: undefined function FOO-C'

;; (print "redefining bar...")
;; (defstruct (bar
;; 	     (:include foo)
;; 	     )
;; 		(a 12)
;; 		(c 30))  ;=> '*** - DEFSTRUCT BAR: There may be only one slot with the name A.'

;; (print "'bar' => redefined")

;; (setq z1 (make-bar))

;; (print "(bar-a z1) =>")
;; (print (bar-a z1))

;;;;;;;;;;;; TINK-5.3 ;;;;;;;;;;;;
(print ";;;;;;;;;;;; TINK-5.3 ;;;;;;;;;;;;")

(defstruct (bar
	     (:include foo (a 34)))
  (c 32))

(print (setq z2 (make-bar)))		;=> #S(BAR :A 34 :B 20 :C 32)

(print (setq z1 (make-foo)))		;=> #S(FOO :A 10 :B 20)

;;;;;;;;;;;; TINK-5.4;;;;;;;;;;;;
(print ";;;;;;;;;;;; TINK-5.4;;;;;;;;;;;;")
(defstruct (foo
	     (:constructor create-foo
			   (a b)))
  a b)
; )
;; (defstruct (foo
;;             (:constructor create-foo (a b)))
;;   a b)
;; (print "create-foo) =>")
;; (print (create-foo))			;=> *** - EVAL/APPL
;; Y: Too few arguments (0 instead of at least 2) given to CREATE-FOO
;; (print "(make-foo) =>")
;; (print (make-foo))			;=> *** - EVAL: undefined function MAKE-FOO

;;;;;;;;;;;; TINK-5.5;;;;;;;;;;;;
(print ";;;;;;;;;;;; TINK-5.5;;;;;;;;;;;;")

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



;;;;;; eof
(print "done")




